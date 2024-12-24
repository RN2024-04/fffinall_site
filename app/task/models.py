from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ManyToManyField(Customer, related_name='products')


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    e_mail = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.e_mail

# python manage.py shell
# from task1.models import Buyer
# Buyer.objects.create(name='Nikita', balance= 100.00, age= 14)
# Buyer.objects.create(name='Masha', balance= 20.99, age= 40)
# Buyer.objects.create(name = 'Arseniy', balance= 3000, age= 52)


# from task1.models import Game
# Game.objects.create(title = 'Cyberpunk 2077', cost =31, size = 46.2, description= 'Game of the year', age_limited = True)
# Game.objects.create(title= 'Mario', cost=5, size=0.5, description = 'Old game', age_limited = False)
# Game.objects.create(title='Hitman', cost = 12, size = 36.6, description = 'Who kills Mark?', age_limited = True)

# buyer1=Buyer.objects.get(id=2)
# buyer2=Buyer.objects.get(id=3)
# buyer3=Buyer.objects.get(id=4)

# Game.objects.get(id=1).buyer.set((buyer1, buyer2))
# Game.objects.get(id=2).buyer.set((buyer2, buyer3))
# Game.objects.get(id=3).buyer.set((buyer1, buyer2))

 # python manage.py makemigrations
 # python manage.py migrate
