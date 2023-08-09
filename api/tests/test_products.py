from django.test import TestCase
from django.test import Client
from api.models.product import Product
from api.models.inventory import Inventory

class GetAllProductsTest(TestCase):
    def setUp(self):
        # Create some test data
        inventory = Inventory.objects.create(Quantity=10)
        Product.objects.create(Product_Name='Product 1', Price=10, FK_Inventory_Id=inventory)
        Product.objects.create(Product_Name='Product 2', Price=20, FK_Inventory_Id=inventory)

    def test_get_all_products(self):
        # Create a test client
        client = Client()
        # Call the get_all_products view function
        response = client.get('/get-all-products/1')
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check the response data
        data = response.json()
        self.assertEqual(data['response'], 'success')
        # self.assertEqual(data['count'], 2)
        # self.assertEqual(len(data['data']), 2)