from django.contrib import admin
from .models import Category, Image, Product, Rating, RatingAnswer


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Rating)
admin.site.register(RatingAnswer)