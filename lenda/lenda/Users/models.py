from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Seller(models.Model):
	seller_Name = models.CharField(max_length = 80)
	Price = models.IntegerField()
	Description = models.TextField(max_length = 200)
	Date_Time = models.DateTimeField(auto_now=False, auto_now_add=True)
	Contact = models.TextField(max_length = 150)
	Item_Name = models.TextField(max_length = 200) 
	image = models.ImageField(null=True, blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

def __unicode__(self):
		return self.Item_Name



