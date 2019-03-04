from django.db import models
import datetime as dt


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, category):
        category = cls.objects.get(pk=id)
        category = cls(category=category)
        category.save()


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_category(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,name,description,location,category):
        image = cls.objects.get(pk=id)
        image = cls(name=name,description=description,location=location,category=category)
        image.save()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(pk=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__category=search_term)
        return photos
