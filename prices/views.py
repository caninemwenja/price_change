from django.shortcuts import (render, redirect,
        get_object_or_404)
from django.core.urlresolvers import reverse

from .models import Price
from .forms import PriceForm

def all_prices(request):
    prices = Price.ordered.all()
    return render(request, 'index.html', { 'prices': prices })


def add_price(request):
    price_form = PriceForm(request.POST) or None

    if price_form.is_valid():
        price_form.save()
        return redirect(reverse('all_prices'))

    return render(request, 'add_price.html', { 'price_form': price_form })


def remove_price(request, price_id):
    price = get_object_or_404(Price, pk=price_id)
    price.delete()

    return redirect(reverse('all_prices'))
