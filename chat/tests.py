from django.test import TestCase

class InventoryAgentTests(TestCase):

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inventory Agent")
