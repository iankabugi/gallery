from django.db import models
import datetime as dt


# Create your models here.
# class Photographer(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=10, blank=True)

#     def __str__(self):
#         return self.first_name

#     def save_photographer(self):
#         self.save()

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos
    