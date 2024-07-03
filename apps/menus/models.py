from django.db import models
from restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus', on_delete=models.CASCADE)
    day = models.DateField()

    class Meta:
        unique_together = ('restaurant', 'day')

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.day}"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.menu.restaurant.name} - {self.menu.day}"