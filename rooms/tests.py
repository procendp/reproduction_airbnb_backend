from rest_framework.test import APITestCase

# just simple test
class TestAmenities(APITestCase):
    def test_two_plus_two(self):        # test_ 로 시작해야함 꼭
        self.assertEqual(2 + 2, 4, "The math is wrong.")