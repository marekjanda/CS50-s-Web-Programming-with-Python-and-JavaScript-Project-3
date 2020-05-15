from django.db import models
from datetime import datetime

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    pizza_type = models.CharField(max_length=16)
    toppings_option = models.SmallIntegerField(default=0)
    price_small = models.FloatField()
    price_large = models.FloatField()
    html_id = models.CharField(max_length=16, default="new")

    def __str__(self):
        if self.pizza_type == 'Regular':
            return f"{self.pizza_type} Pizza with {self.toppings_option} toppings"
        if self.pizza_type == 'Sicilian':
            return f"{self.pizza_type} Pizza with {self.toppings_option} items"
        

class Sub(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.FloatField(default=0)
    price_large = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    add_on = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} with {self.add_on}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Platter(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.FloatField(default=0)
    price_large = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}"

class OrderItem(models.Model):
    menuItem = models.CharField(max_length=64)
    meal = models.CharField(max_length=64)
    pizza_type = models.CharField(max_length=16, blank=True, default="None")    
    options = models.ManyToManyField(Topping, blank=True)
    size = models.CharField(max_length=16)
    price = models.FloatField()

    def __str__(self):
        if self.menuItem == "pizza":
            myoptions = ""
            disp_options = self.options.all()
            for x in disp_options:
                if myoptions:
                    myoptions += ", "
                    myoptions += str(x)
                else:
                    myoptions = str(x)
            return f"{self.pizza_type} {self.meal}, {self.size} with {myoptions}"
        elif self.menuItem == "pasta" or self.menuItem == "salad":
            return f"{self.meal}"
        else:
            return f"{self.meal}, {self.size}"

class OnlineOrder(models.Model):
    placed = models.DateTimeField('date placed', default=datetime.today())
    customer = models.CharField(max_length=64)
    items = models.ManyToManyField(OrderItem, blank=True, related_name="order")
    total_price = models.FloatField(default=0.00)
    status = models.CharField(max_length=16, default="unplaced")

    def __str__(self):
        return f"Placed: {self.placed}, Customer: {self.customer}, Total: ${self.total_price}, Status: {self.status}"
    




    




