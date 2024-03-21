from product import Product
from category import Category
import pytest

# Тесты для класса Product
def test_product_price_setter_valid():
    product = Product("Phone", "Smartphone", 500, 10)
    product.price = 600
    assert product.price == 600

def test_product_price_setter_invalid():
    product = Product("Phone", "Smartphone", 500, 10)
    product.price = -100
    assert product.price == 500  # Убедимся, что цена осталась прежней

# Тесты для класса Category
def test_category_add_product():
    category = Category("Category", "Description")
    product1 = Product("Phone", "Smartphone", 500, 10)
    product2 = Product("Laptop", "Laptop", 1000, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert len(category._products) == 2

def test_category_products_getter():
    category = Category("Category", "Description")
    product1 = Product("Phone", "Smartphone", 500, 10)
    product2 = Product("Laptop", "Laptop", 1000, 5)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Phone, 500 руб. Остаток: 10 шт.\nLaptop, 1000 руб. Остаток: 5 шт."
    assert category.products == expected_output

def test_category_total_unique_products():
    category = Category("Category", "Description")
    product1 = Product("Phone", "Smartphone", 500, 10)
    product2 = Product("Laptop", "Laptop", 1000, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert Category.total_unique_products == 6

# Проверка сообщения об ошибке при попытке установить недопустимую цену
def test_product_price_setter_invalid_message(capfd):
    product = Product("Phone", "Smartphone", 500, 10)
    product.price = -100
    out, _ = capfd.readouterr()
    assert "Ошибка: Цена должна быть больше нуля." in out

# Проверка общего количества категорий после добавления
def test_total_categories_after_addition():
    category1 = Category("Category1", "Description1")
    category2 = Category("Category2", "Description2")
    assert Category.total_categories == 5

# Проверка общего количества уникальных продуктов после добавления
def test_total_unique_products_after_addition():
    category = Category("Category", "Description")
    product1 = Product("Phone", "Smartphone", 500, 10)
    product2 = Product("Laptop", "Laptop", 1000, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert Category.total_unique_products == 8

