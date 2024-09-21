def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def calculate_discount(products):
    total = 0
    for product in products:
        total += product["price"] - product["price"] * product["discount"] / 100
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12

def test_calculate_discount_with_empty_list():
    assert calculate_discount([]) == 0

def test_calculate_discount_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5, "discount": 10
        }
    ]
    assert calculate_discount(products) == 4.5

def test_calculate_discount_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10, "discount": 10
        },
        {
            "name": "Pen", "price": 2, "discount": 20
        }
    ]
    assert calculate_discount(products) == 10.6

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()

    test_calculate_discount_with_empty_list()
    test_calculate_discount_with_single_product()
    test_calculate_discount_with_multiple_product()
