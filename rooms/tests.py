from rest_framework.test import APITestCase
from . import models

# just simple test
class TestAmenities(APITestCase):
    # def test_two_plus_two(self):        # test_ 로 시작해야함 꼭
        
    NAME = "Amenity Test"
    DESC = "Amenity Description"

    def setUp(self):        # DB set up할 곳..      다른 모든 test들 실행되기 전 실행될 것
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )
    def test_all_amenities(self):
        response = self.client.get("/api/v1/rooms/amenities/")
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )