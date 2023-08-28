class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        Customer.all_customers.append(self)

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def restaurants(self):
        reviewed_restaurants = []
        for review in self.reviews:
            reviewed_restaurants.append(review.restaurant)
        return list(set(reviewed_restaurants))

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        reviewed_customers = []
        for review in self.reviews:
            reviewed_customers.append(review.customer)
        return list(set(reviewed_customers))

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews
