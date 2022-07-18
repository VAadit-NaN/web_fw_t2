import logging
from django.contrib import admin, messages
from .models import CountryData
from django.urls import path, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'population')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls
        
    def upload_csv(self):
        return None



admin.site.register(CountryData, CountryAdmin)
