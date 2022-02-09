from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarMake)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5
# CarModelAdmin class
class  CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'carmake', 'id_delear', 'list_choice', 'types', 'year', 'seler']
    inlines = [CarModelInline]
#admin.site.register(CarModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline

# Register models here
