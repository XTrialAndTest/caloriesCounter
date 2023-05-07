from django.db import models


class CaloriesCounter(models.Model):

    food = models.CharField(max_length=200)
    calories = models.FloatField(max_length=200)
    TIME = (('Break fast', 'Break fast'), ('Lunch', 'Lunch'),
            ('Evening', 'Evening'), ('Dinner', 'Dinner'))

    time = models.CharField(max_length=200, choices=TIME, default='Breakfast')

    def __str__(self):
        return self.food
