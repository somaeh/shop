from django.contrib import admin
from .models import Product, Size, Color, Informations
from .import models

class InformationAdmin(admin.StackedInline):
    model = models.Informations
    
@admin.register(models.Product)   
class ProductAdmin(admin.ModelAdmin):
    list_display=("title", "price")   
    inlines=(InformationAdmin,)
    
    
    


admin.site.register(Size)
admin.site.register(Color)

