import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import CustomUser
from store.models import Category, Product

# Crea utenti demo
if not CustomUser.objects.filter(username='manager_demo').exists():
    manager = CustomUser.objects.create_user(
        username='manager_demo',
        email='manager@demo.com',
        password='manager12345',
        role='manager'
    )
    print('Manager creato')

if not CustomUser.objects.filter(username='user_demo').exists():
    customer = CustomUser.objects.create_user(
        username='user_demo',
        email='user@demo.com',
        password='user12345',
        role='customer'
    )
    print('Customer creato')

# Crea categorie
cat1, _ = Category.objects.get_or_create(name='Elettronica', slug='elettronica')
cat2, _ = Category.objects.get_or_create(name='Abbigliamento', slug='abbigliamento')
cat3, _ = Category.objects.get_or_create(name='Libri', slug='libri')
print('Categorie create')

# Crea prodotti
prodotti = [
    {'name': 'Iphone 10', 'category': cat1, 'description': 'Ottimo smartphone.', 'price': 299.99, 'stock': 10},
    {'name': 'Cuffie Bluetooth', 'category': cat1, 'description': 'Cuffie wireless.', 'price': 49.99, 'stock': 25},
    {'name': 'Macbook Pro', 'category': cat1, 'description': 'Laptop potente.', 'price': 899.99, 'stock': 5},
    {'name': 'T-Shirt Google', 'category': cat2, 'description': 'Per veri developer.', 'price': 19.99, 'stock': 50},
    {'name': 'Felpa Gucci', 'category': cat2, 'description': 'Calda e comoda.', 'price': 34.99, 'stock': 30},
    {'name': 'Corso Python', 'category': cat3, 'description': 'Impara Python.', 'price': 24.99, 'stock': 15},
    {'name': 'Django for Beginners', 'category': cat3, 'description': 'Impara Django.', 'price': 29.99, 'stock': 12},
]

for p in prodotti:
    Product.objects.get_or_create(
        name=p['name'],
        defaults={
            'category': p['category'],
            'description': p['description'],
            'price': p['price'],
            'stock': p['stock'],
            'available': True
        }
    )
print('Prodotti creati')
print('Database popolato con successo!')