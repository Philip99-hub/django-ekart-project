from django.shortcuts import render,redirect
from .models import Customer
from seller.models import Seller,Product
from django.db.models import Q
 
# Create your views here.


def customer_home(request):
    return render(request, 'customer/customer_home.html')


def store(request):
    query = request.GET.get('query')

    if query == 'all':
        products = Product.objects.all()
     
    else:
         
        products = Product.objects.filter(category = query)


    if  'search_text' in request.GET:
        search_text = request.GET.get('search_text')
        products = Product.objects.filter(Q(category__category__icontains = search_text) | Q(product_name__icontains = search_text))
    count = products.count()    
    context = {
        'products': products,
        'product_count': count
    }

    return render(request, 'customer/store.html',context)


def product_detail(request,product_id):
    product = Product.objects.get(id = product_id)

    context = {
        'product': product,
    }

    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    
    message = ''
    status = False
    if request.method == 'POST':  
        first_name = request.POST['fname'] 
        last_name = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        company_name = request.POST['cmp_name']
        city = request.POST['city']
        country = request.POST['country']
        account_no = request.POST['acc_no']
        bank_name = request.POST['bank_name']
        branch = request.POST['branch']
        ifsc = request.POST['ifsc']
        pic = request.FILES['pic']
        seller_exist = Seller.objects.filter(email = email).exists()

        if not seller_exist: 

                seller = Seller(first_name = first_name, last_name = last_name, company_name = company_name,    gender = gender, email = email, 
                                city = city, country = country, account_no = account_no, bank_name = bank_name,
                                branch_name = branch, ifsc = ifsc, pic = pic)
                seller.save()
                message = 'Registration Succesful'
                status = True

            
        else:
                message = 'Email Exists'
    return render(request, 'customer/seller_register.html', {'message': message})



def seller_login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['seller_id']
        password = request.POST['password']

        seller = Seller.objects.filter(login_id = username, password = password)

        if seller.exists():
            request.session['seller'] = seller[0].id
            request.session['seller_name'] = seller[0].first_name + ' ' + seller[0].last_name
            return redirect('Seller:seller_home')

        else:

            message = 'Invalid Username Or Password'

    return render(request, 'customer/seller_login.html')
   


def customer_signup(request):
    message = ''
    if request.method == 'POST':  # when user submit the form
        # here fname is the name attribute given in form input
        # fetching values from form data and storing in variable
        first_name = request.POST['fname'] 
        last_name = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        
        # use exists() method to check whether the user with given email exists, it returns boolean
        customer_exist = Customer.objects.filter(email = email).exists()

        if not customer_exist: 

            customer = Customer(first_name = first_name, last_name = last_name, gender = gender, email = email, 
                            city = city, country = country, password = password)
            customer.save()
            message = 'Registration Succesful'

        
        else:
            message = 'Email Exists'
   

    return render(request, 'customer/customer_signup.html', {'message': message})


def customer_login(request):
    return render(request, 'customer/customer_login.html')


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')
