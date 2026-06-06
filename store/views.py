from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from .models import Product, Category, Order, OrderItem
from .forms import ProductForm

# Lista prodotti (con ricerca e filtro categoria)
class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        query = self.request.GET.get('q')
        category_slug = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(name__icontains=query)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# Dettaglio prodotto
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# Aggiungi al carrello (salvato in sessione)
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    messages.success(request, f'"{product.name}" aggiunto al carrello!')
    return redirect('store:cart')

# Visualizza carrello
@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        total += subtotal
        items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'store/cart.html', {'items': items, 'total': total})

# Rimuovi dal carrello
@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(str(pk), None)
    request.session['cart'] = cart
    return redirect('store:cart')

# Crea ordine dal carrello
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Il carrello è vuoto.')
        return redirect('store:cart')
    order = Order.objects.create(customer=request.user)
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )
    request.session['cart'] = {}
    messages.success(request, f'Ordine #{order.id} creato con successo!')
    return redirect('store:order_list')

# Lista ordini del customer
@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'store/order_list.html', {'orders': orders})

# Gestione prodotti per il manager
@login_required
def manager_dashboard(request):
    if not request.user.is_manager():
        messages.error(request, 'Non hai i permessi per accedere a questa pagina.')
        return redirect('store:product_list')
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'store/manager_dashboard.html', {'products': products, 'orders': orders})

@login_required
def product_create(request):
    if not request.user.is_manager():
        return redirect('store:product_list')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prodotto creato!')
            return redirect('store:manager_dashboard')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form, 'title': 'Nuovo Prodotto'})

@login_required
def product_edit(request, pk):
    if not request.user.is_manager():
        return redirect('store:product_list')
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prodotto aggiornato!')
            return redirect('store:manager_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'title': 'Modifica Prodotto'})

@login_required
def product_delete(request, pk):
    if not request.user.is_manager():
        return redirect('store:product_list')
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Prodotto eliminato!')
        return redirect('store:manager_dashboard')
    return render(request, 'store/product_confirm_delete.html', {'product': product})


