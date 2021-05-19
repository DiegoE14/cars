from django.contrib import admin
from .models import Brand, BrandReference, Auto

class PostAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo_marca', 'created_at')

#Automobile APP
admin.site.register(Brand, PostAdmin)
admin.site.register(BrandReference)
admin.site.register(Auto)



