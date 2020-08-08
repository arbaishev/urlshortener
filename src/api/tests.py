import json

from django.test import TestCase

from shortenerapp.models import URL

TEST_URL = "https://www.example.com/a-b-c/d-e-f"
TEST_SHORTCODE = "qwerty"


class TestAPI(TestCase):
    def test_create_short_link_without_custom_alias(self):
        response = self.client.post("/api/short/", data={"url": TEST_URL})
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["error"], "")
        self.assertTrue(response_data["data"], )

    def test_create_short_link_with_custom_alias(self):
        response = self.client.post("/api/short/",
                                    data={"url": TEST_URL, "custom": "True", "custom_shortcode": TEST_SHORTCODE})
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response_data["error"])
        self.assertTrue(response_data["data"], )
        self.assertEqual(response_data["data"]["shortcode"], TEST_SHORTCODE)

    def test_get_all_objects(self):
        URL.objects.create(url=TEST_URL, custom=True, shortcode=TEST_SHORTCODE.upper())
        URL.objects.create(url=TEST_URL, custom=True, shortcode=TEST_SHORTCODE)
        URL.objects.create(url=TEST_URL)
        response = self.client.get("/api/")
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(response_data["data"])
        self.assertEqual(response.status_code, 200)

    def test_get_link_stats(self):
        URL.objects.create(url=TEST_URL, custom=True, shortcode=TEST_SHORTCODE)

        response = self.client.get("/api/" + TEST_SHORTCODE)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(response_data["data"])
        self.assertEqual(response_data["data"]["url"], TEST_URL)
        self.assertEqual(response_data["data"]["shortcode"], TEST_SHORTCODE)
        self.assertFalse(response_data["error"])
        self.assertEqual(response.status_code, 200)
