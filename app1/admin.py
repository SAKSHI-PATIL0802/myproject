from django.contrib import admin
from . models import Product,Offer
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_displays=('name','price','img',)

class offerAdmin(admin.ModelAdmin):
	list_display=('code',)



admin.site.register(Product)
admin.site.register(Offer)
