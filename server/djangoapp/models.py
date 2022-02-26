from django.db import models
from django.utils.timezone import now

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    ids = models.AutoField(primary_key=True)
# - Name
    name = models.CharField(max_length=25)
# - Description
    description = models.CharField(max_length=25)
# - Any other fields you would like to include in car make model
    year = models.DateField(max_length=6)
    color = models.CharField(max_length=25)
# - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
class CarModel(models.Model):
    ids = models.AutoField(primary_key=True)
# - Name
    name = models.CharField(max_length=25)
# Foreign key
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Dealer id, used to refer a dealer created in cloudant database
    id_dealer = models.IntegerField()
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    list_choice = [
        (1, ('Sedan')), 
        (2, ('SUV')), 
        (3, ('WAGON'))
        ]
    types = models.CharField(max_length=30, null=True)
# - Year (DateField)
    year = models.DateField()
# - Any other fields you would like to include in car model
    seler = models.CharField(max_length=25)
# - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip, state):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
        # Delaer state
        self.state = state
    def __str__(self):
        return "Dealer name : " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        # Review name
        self.name = name
        # Review purchase
        self.purchase = purchase
        # Review content
        self.review = review
        # Review purchase date
        self.purchase_date = purchase_date
        # Car make
        self.car_make = car_make
        # Car model
        self.car_model = car_model
        # Car year
        self.car_year = car_year
        # Seniment
        self.sentiment = sentiment
        # Review id
        self.id = id



if __name__ == "__main__":
    pass