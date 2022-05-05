from django.db import models


class Term(models.Model):
    id = models.AutoField(primary_key=True)
    details = models.CharField(max_length=500)
    last_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.details
    