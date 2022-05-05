#from typing_extensions import Self
#from core.tests 
from django.test import TestCase
from .models import Term
from django.contrib.admin.sites import AdminSite
from .admin import TermModelAdmin

#First test
class TestMode(TestCase):
    
    def test_correct_term_created(self):
        self.term =Term.objects.create(details='test details edited')
        self.assertEquals(str(self.term), 'test detailes edited')
        


class OurRequest(object):
    def __init__(self, user=None):
        self.user=user

#Second test
class ModelAdminTest(TestCase):
    def setUp(self):
        self.termsModelAdmin = TermModelAdmin(model=Term,admin_site=AdminSite())
    
    def test_has_add_permission(self):
        self.assertEquals(self.termsModelAdmin.has_add_permission(OurRequest),False)
        
    def test_has_delete_permission(self):
        self.assertEquals(self.termsModelAdmin.has_delete_permission(OurRequest),False)