import unittest

from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.shops.exceptions import ShopNotFoundException
from app.tests.shops.fakes import shop1, shop2, shop3
from app.tests.shops.forms import FakeShopsForm
from app.tests.test_basic_repositories import BasicRepositoryTests


class ShopsRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLShopsRepository()

    def test_get_with_no_shop_should_raise_shop_not_found_exception(self):
        self.reset_repositories()
        self.assertRaises(ShopNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_shop_should_raise_shop_not_found_exception(self):
        self.assertRaises(ShopNotFoundException, self.repository.get, -1)

    def test_get_should_get_shop(self):
        shop = self.repository.get(shop1.id)
        self.assertEqual(shop1, shop)
        shop = self.repository.get(shop2.id)
        self.assertEqual(shop2, shop)
        shop = self.repository.get(shop3.id)
        self.assertEqual(shop3, shop)

    def test_get_all_with_no_shop_get_no_shop(self):
        self.reset_repositories()
        shops = self.repository.get_all()
        self.assertEqual(0, len(shops))

    def test_get_all_get_shops(self):
        shops = self.repository.get_all()
        self.assertIn(shop1, shops)
        self.assertIn(shop2, shops)
        self.assertIn(shop3, shops)

    def test_get_all_with_name_filter_shops(self):
        form = FakeShopsForm(shop1.name)
        shops = self.repository.get_all(form)
        self.assertIn(shop1, shops)
        self.assertNotIn(shop2, shops)
        self.assertNotIn(shop3, shops)


if __name__ == "__main__":
    unittest.main()
