from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def contact(request):

    if request.method == 'POST':
        message = request.POST['message']

        send_mail('From E-shop Contact Form',message,settings.EMAIL_HOST_USER,['raul.gongora66@gmail.com','jtuteja.du@gmail.com','Atenso5@gmail.com','rakshi.saseni@gmail.com'], fail_silently=False)

    return render(request, 'contact.html')



