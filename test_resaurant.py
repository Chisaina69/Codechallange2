import pytest
from Restaurant import Customer, Restaurant, Review

# Test Customer class methods


def test_customer_methods():
    customer = Customer("Quincy", "Alexandria")
    assert customer.full_name() == "Quincy Alexandria"
    assert customer.restaurants() == []
    assert customer.num_reviews() == 0

# Test Restaurant class methods


def test_restaurant_methods():
    restaurant = Restaurant("Chum Bucket")
    assert restaurant.get_name() == "Chum Bucket"
    assert restaurant.get_reviews() == []
    assert restaurant.average_star_rating() == 0

# Test Review class methods


def test_review_methods():
    customer = Customer("Ashley", "Chuumwe")
    restaurant = Restaurant("Crusty Crub")
    review = Review(customer, restaurant, 5)
    assert review.get_rating() == 5
    assert review.get_customer() == customer
    assert review.get_restaurant() == restaurant

# Test interactions between classes


def test_interactions():
    restaurant = Restaurant("Chum Bucket")
    customer = Customer("Quincy", "Alexandria")
    customer.add_review(restaurant, 4)
    assert len(customer.restaurants()) == 1
    assert customer.num_reviews() == 1
    assert len(restaurant.customers()) == 1
    assert restaurant.average_star_rating() == 4


# Run tests
if __name__ == "__main__":
    pytest.main()
