from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SellerForm
from .models import Seller

def items_Listing(request):
	items = Seller.objects.all()
	context = {
	"items": items
	}
	return render(request,'items_list.html', context)
	

def items_New(request, id):
	if request.method == "POST":
		form = SellerForm(request.POST, request.FILES or None)
		if form.is_valid():
			post = form.save()
	    	post.save()
	else:
		form = SellerForm()
	return render(request, 'forms.html', {'form': form})

def items_Detail(request, id):
	objects = get_object_or_404(Seller, id=id)
	context = {
		"title": objects.Item_Name,
		"object": objects, 
	}
	return render(request, "Item_detail.html", context)
