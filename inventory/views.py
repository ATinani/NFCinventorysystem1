from django.shortcuts import render, redirect
from django.http import HttpResponse

# Example view function
def used_stock(request):
    if request.method == "POST":
        # Add logic to handle the stock update
        return HttpResponse("Stock updated successfully!")
    return render(request, "inventory/used_stock.html")



# Create your views here.
