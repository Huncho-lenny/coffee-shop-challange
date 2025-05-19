from customer import Customer

def test_customer_name():
    c = Customer("Skilli")
    assert c.name == "Skilli"

    try:
        c.name = "This name is too long"
    except ValueError:
        assert True
    else:
        assert False
