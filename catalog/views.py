from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm, VersionForm
from .models import Product

class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        # Fetch active versions for each product
        for product in products:
            product.active_version = product.get_active_version()
        context['products'] = products
        return context


class AboutView(TemplateView):
    template_name = 'catalog/about.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalog:index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalog:index')


class VersionCreateView(View):
    template_name = 'catalog/version_form.html'
    form_class = VersionForm

    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(pk=product_id)
        form = self.form_class(initial={'product': product})
        return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(pk=product_id)
        form = self.form_class(request.POST, initial={'product': product})
        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            version.save()
            return redirect('catalog:index')
        return render(request, self.template_name, {'form': form, 'product': product})
