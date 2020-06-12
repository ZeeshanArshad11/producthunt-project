from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Product, Voting
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            product  = Product()
            product.title = request.POST['title']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            product.body = request.POST['body']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/product/' + str(product.id))
        else:
            return render(request, 'accounts/create.html', {'error':'All fields must be required!'})
        return
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})


# @login_required(login_url="/account/signup")
# def upvote(request, product_id):
#     if request.method == 'POST':
#         product = get_object_or_404(Product, pk=product_id)
#         product.votes_total += 1
#         product.save()
#         return redirect('/product/' + str(product.id))

@login_required(login_url="/account/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        try:
            vote = Voting.objects.get(products_id = product_id , user=request.user )
            return redirect('/product/' + str(product.id))
        except vote.DoesNotExist:
            vote = Voting.objects.create(user = request.user, products_id=product_id)
            product.votes_total += 1
            product.save()
            vote.save()
            return redirect('/product/' + str(product.id))
    else:
        return render(request, 'products/home.html')
