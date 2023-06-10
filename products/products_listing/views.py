from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
from .utils import ean13_to_dun14
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages



def index_view(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(user=request.user)
        return render(request, 'products_listing/home.html', {'products': products})
    else:
        return redirect('login')

@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request=request)
        if form.is_valid():
            product = form.save(commit=False)
            units_number = form.cleaned_data.get('units_number')
            ean13 = form.cleaned_data.get('ean13')
            dun14 = ean13_to_dun14(ean13, units_number)
            product.dun14 = dun14
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm(request=request)
    return render(request, 'products_listing/product_create.html', {'form': form})
    


@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_listing/product_detail.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('product_list'))
    else:
        form = UserCreationForm()
    return render(request, 'products_listing/register.html', {'form': form})


def home_view(request):
    return render(request, 'products_listing/product_list.html')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products_listing/product_create.html'
    success_url = reverse_lazy('product_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Product updated successfully.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please correct the errors below.')
        return response

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')