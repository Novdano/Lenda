from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
	list_display = ["Item_Name", "seller_Name", "Price"]
	list_filter = ["Price"]
	search_fields = ["Item_Name", "seller_Name"]
	class Meta:
		model = Seller

admin.site.register(Seller, SellerAdmin)
# Register your models here.
