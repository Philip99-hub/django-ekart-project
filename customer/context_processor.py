from eKart_admin.models import Category
from customer.models import Cart
def get_category_list(self):
    category_list = Category.objects.all()

    return dict(category_list = category_list)


def get_cart_count(request):
    
    if 'customer' in request.session:
        cart_count = Cart.objects.filter(customer = request.session['customer']).count()
        if cart_count:
            count = cart_count
        else:
            count = 0
        return dict({'cart_count': count,})
    else:
        return dict({'cart_count': 0})