from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Listings)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comment)