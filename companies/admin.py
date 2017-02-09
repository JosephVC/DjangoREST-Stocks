from django.contrib import admin

from .models import Stock

admin.site.register(Stock) # make sure we can add/delete stocks from the admin panel