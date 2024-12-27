from rest_framework.test import APITestCase
from . import models

class TestAmenities(APITestCase):
        
    NAME = "Amenity Test"
    DESC = "Amenity Description"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):        # DB set up할 곳..      다른 모든 test들 실행되기 전 실행될 것
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
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

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."
        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )
        response = self.client.post(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)

class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):
        updated_amenity_name = "Updated Amenity"
        updated_amenity_description = "Updated Amenity desc"

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": updated_amenity_name,
                "description": updated_amenity_description,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            updated_amenity_name,
        )
        self.assertEqual(
            data["description"],
            updated_amenity_description,
        )

        updated_amenity_name = "Updated Amenity 2"

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": updated_amenity_name,
            },
        )
        data = response.json()
        self.assertEqual(
            data["name"],
            updated_amenity_name,
        )
        self.assertEqual(
            data["description"],
            updated_amenity_description,
        )

        updated_amenity_description = "Updated Amenity desc 2"

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "description": updated_amenity_description,
            },
        )
        data = response.json()
        self.assertEqual(
            data["name"],
            updated_amenity_name,
        )
        self.assertEqual(
            data["description"],
            updated_amenity_description,
        )

        invalid_name = "name" * 40
        invalid_desc = "desc" * 40
        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": invalid_name,
                "description": invalid_desc,
            },
        )
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 204)        