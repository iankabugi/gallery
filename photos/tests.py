from django.test import TestCase
from .models import Photographer
import datetime as dt

# Create your tests here.
class PhotographerTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.james= Photographer(first_name = 'James', last_name ='Muriuki', email ='james@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Photographer))
    # Testing Save Method
    def test_save_method(self):
        self.james.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)

