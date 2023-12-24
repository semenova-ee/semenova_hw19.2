from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogPostForm
from .forms import ProductForm
from .models import Product

class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
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
