from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_name(self):
        data = self.data1
        self.assertEqual(str(data), "django")


class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="tutta")
        self.data1 = Product.objects.create(category_id=1, title="django product",
                                            created_by_id=1, slug="django-product",
                                            price="20.00", image="django")

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django product")
