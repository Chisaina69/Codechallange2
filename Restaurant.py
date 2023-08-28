class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def restaurants(self):
        reviewed_restaurants = []
        for review in self.reviews:
            reviewed_restaurants.append(review.get_restaurant())
        return reviewed_restaurants

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
            if customer.get_first_name() == name:
                matching_customers.append(customer)
        return matching_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_val = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name_val

    def get_reviews(self):
        return self.reviews

    def customers(self):
        reviewed_customers = []
        for review in self.reviews:
            reviewed_customers.append(review.get_customer())
        return reviewed_customers

    def average_star_rating(self):
        total_ratings = sum(review.get_rating() for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews
    
    @classmethod
    def all (cls):
        return cls.all_restaurants
    


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_val = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating_val

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


# Creating instances
restaurant1 = Restaurant("Chum Bucket")
restaurant2 = Restaurant("Crusty Crub")

customer1 = Customer("Quincy", "Alexandria")
customer2 = Customer("Ashley", "Chuumwe")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 3)

# Adding reviews
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 2)

# Accessing data
print(customer1.full_name())
print(restaurant2.get_name())
print(review2.get_rating())
print([restaurant.get_name() for restaurant in customer2.restaurants()])
print(restaurant1.average_star_rating())

# Accessing all instances
print(Customer.all())
print(Restaurant.all())
print(Review.all())
