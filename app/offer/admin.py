from django.contrib import admin
from .models import *

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    pass

admin.site.register(Offer, OfferAdmin)


class ResumeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resume, ResumeAdmin)