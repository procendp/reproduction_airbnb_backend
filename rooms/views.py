<<<<<<< HEAD
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly    # GET만 pass, 나머지 POST, PUT, DELETE은 인증 필요
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from categories.models import Category
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateRoomBookingSerializer

class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class AmenityDetail(APIView):

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class Rooms(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True, context={"request":request})
        return Response(serializer.data)
    
    def post(self, request):
            serializer = RoomDetailSerializer(data = request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'")
                except Category.DoesNotExist:
                    raise ParseError("Category not found")
                try:
                    with transaction.atomic():  # transaction.atomic() : 보통 쿼리가 코드 실행할 때마다 DB에 즉시 반영되는데, 이 안에 넣으면 장고는 변경사항들을 리스트로 만들고 에러 없으면 DB에 반영할 것
                        room = serializer.save(owner=request.user, category=category)  # room은 owner가 꼭 필요함.. 따라서 owner와 함께 방 생성    --> create 재정의 해주지 않아도 됨... ** create나 save의 validated_data에 추가로 데이터를 추가하고 싶다면 save할 때 데이터 추가해주자
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)     # ManyToMany
                        serializer = RoomDetailSerializer(
                        room,
                        context={"request": request},
                    )
                        return Response(serializer.data)
                except Exception as e:
                    raise ParseError("Amenity not found")

            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class RoomDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room, context={"request":request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = self.get_object(pk)
        if room.owner != request.user:
            raise PermissionDenied
        
        serializer = RoomDetailSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                    raise ParseError("The category kind should be rooms")
            except Category.DoesNotExist:
                    raise ParseError(detail="Category not found")
            try:
                with transaction.atomic():
                    if category_pk:
                        room = serializer.save(category=category)
                    else:
                        room = serializer.save()
                    amenities = request.data.get("amenities")
                    if amenities:
                        room.amenities.clear()
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    else:
                            room.amenities.clear()
                    return Response(RoomDetailSerializer(room, context={"request":request}).data)
            except Exception as e:
                print(e)
                raise ParseError("amenity not found")
        else:
            return Response(serializer.errors)


    def delete(self, request, pk):
        room = self.get_object(pk)
        if room.owner != request.user:          # 2. owner와 user가 같은지
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class RoomReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)      # default page = 1
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializers = ReviewSerializer(room.reviews.all()[start:end], many=True)        # 한 페이지에 보여줄 리뷰 개수
        return Response(serializers.data)
    
    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(user=request.user, room=self.get_object(pk))
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        
class RoomAmenities(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except:
            raise NotFound
    def get(self, request, pk):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializer = AmenitySerializer(
            room.amenities.all()[start:end],
            many=True,
        )
        return Response(serializer.data)
    
class RoomPhotos(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)
        if request.user != room.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class RoomBookings(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except:
            raise NotFound
        
    def get(self, request, pk):
        room = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()   # 날짜만
        bookings = Booking.objects.filter(room=room, kind=Booking.BookingKindChoices.ROOM, check_in__gt=now,)   # check_in__gt=now : 비교해서 미래 예약만 받도록
        # bookings = Booking.objects.filter(room__pk=pk)      # room__pk=pk : 이렇게 표현하면 get_object로 정의하지 않아도 됨..   *** user가 존재하는 room의 pk를 보낼거라고 확신하면 쓰자, 그럼 room에 대한 조회를 먼저 할 필요 없으니까
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        room = self.get_object(pk)
        serializer = CreateRoomBookingSerializer(data=request.data)
        # serializer = CreateRoomBookingSerializer(
        #     data=request.data,
        #     context={"room": room},
        # )
        if serializer.is_valid():
            booking = serializer.save(
                room=room,
                user=request.user,
                kind=Booking.BookingKindChoices.ROOM,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    # def put(self, request, pk):
    # def delete(self, request, pk):

# class RoomBookingCheck(APIView):
#     def get_object(self, pk):
#         try:
#             return Room.objects.get(pk=pk)
#         except:
#             raise NotFound
#     def get(self, request, pk):
#         room = self.get_object(pk)
#         check_out = request.query_params.get("check_out")
#         check_in = request.query_params.get("check_in")
#         exists = Booking.objects.filter(
#             room=room,
#             check_in__lte=check_out,
#             check_out__gte=check_in,
#         ).exists()
#         if exists:
#             return Response({"ok": False})
#         return Response({"ok": True})

def make_error(request):
    division_by_zero = 1 / 0
=======
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer

class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)

class AmenityDetail(APIView):

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)
        

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class Rooms(APIView):

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RoomDetailSerializer(data = request.data)
        if serializer.is_valid():
            room = serializer.save()
            serializer = RoomDetailSerializer(room)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)

        
>>>>>>> 8212159 (setting the functions of the experiences. [GET, POST])
