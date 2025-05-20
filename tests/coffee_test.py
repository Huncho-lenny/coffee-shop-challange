import pytest
from coffee import Coffee

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_too_short():
    with pytest.raises(ValueError):
        Coffee("Hi") 

def test_coffee_name_not_string():
    with pytest.raises(ValueError):
        Coffee(123) 

def test_coffee_name_is_imixmutable():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Mocha" 
