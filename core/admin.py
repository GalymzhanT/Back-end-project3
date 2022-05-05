from django.contrib import admin
from .models import Term
# Register your models here.

class TermModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request,obj=None):
        return True
    
admin.site.register(Term, TermModelAdmin)