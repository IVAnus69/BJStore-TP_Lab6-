from django.contrib import admin
from .models import Company, Training, Profile, ProfileToCompanies

admin.site.register(Company)
admin.site.register(Training)
admin.site.register(Profile)
admin.site.register(ProfileToCompanies)
