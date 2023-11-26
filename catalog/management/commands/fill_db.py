from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, args, *kwargs):
        # Clear old data
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Populate categories
        phones = Category.objects.create(name='Phones', description='All about phones')
        tablets = Category.objects.create(name='Tablets', description='All about tablets')

        # Populate products
        iphone_xr = Product.objects.create(name='iphone xr', description='descr for iphone xr', category=phones, price=10)
        iphone_15 = Product.objects.create(name='iphone 14', description='descr for iphone 14', category=phones, price=11)
        ipad_8 = Product.objects.create(name='ipad 8', description='descr for ipad 8', category=tablets, price=9)
        ipad_air = Product.objects.create(name='ipad air', description='descr for ipad air', category=tablets, price=12)

        self.stdout.write(self.style.SUCCESS('Data successfully populated'))
