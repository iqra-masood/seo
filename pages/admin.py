from django.contrib import admin
from .models import Order
from .models import joiners
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
  list_display = ("name", "email","phone", "company","service", "subject", "message")
  
admin.site.register(Order, OrderAdmin)



# admin.site.register(joinUs)
class joinersAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "phone","domain","file", "subject", "message")
  
admin.site.register(joiners, joinersAdmin)


