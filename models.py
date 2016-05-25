from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name    = models.CharField(max_length=50, blank=False)
    
    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.company_name

# Extra user information in addition to the standard django user stuff
class Employee(models.Model):
    company     = models.ForeignKey(Company)
    user        = models.OneToOneField(User, blank=True, null=True)
    email       = models.EmailField(blank=False, unique=True)
        
    def __str__(self):
        if (self.user):
            return self.user.get_full_name() + ' (' + self.user.get_username() + ')'
        else:
            return "Awaiting Confirmation" + ' (' + self.email + ')'