from django.contrib import admin
from .models import People,Address,Doctor,Product,Bio

# Register your models here.
admin.site.register(People)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Product)
admin.site.register(Bio)