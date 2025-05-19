import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    cust = Customer("Webz")
    cof = Coffee("Cappuccino")
    order = Order(cust, cof, 5.5)
    assert order.customer == cust
    assert order.coffee == cof
    assert order.price == 5.5

def test_invalid_customer_type():
    cof = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("NotACustomer", cof, 3.0)

def test_invalid_coffee_type():
    cust = Customer("RudeBoi")
    with pytest.raises(TypeError):
        Order(cust, "JustAString", 2.0)

def test_invalid_price_type():
    cust = Customer("Skilli")
    cof = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(cust, cof, 15.0)

def test_price_not_float():
    cust = Customer("Skilli")
    cof = Coffee("Americano")
    with pytest.raises(ValueError):
        Order(cust, cof, "10")  
