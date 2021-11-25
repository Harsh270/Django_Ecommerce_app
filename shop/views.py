from django.shortcuts import *
from .models import Product,Contact
from math import ceil

def shop(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds = [[products, range(1, len(products)), nSlides]]
    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)

    return render(request, "shop/index.html", params)


def products(request):
    products = Product.objects.all()
    allproduct = []
    category = Product.objects.values('category')
    cats = {item["category"] for item in category}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allproduct.append([prod, range(1, nSlides), nSlides])
    dict = {"allproduct": allproduct}
    return render(request, "shop/product.html", dict)

def search(request):
    return HttpResponse('search')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, "shop/contact.html")
def Detail(request):
    name=request.POST.get("name",'')
    email = request.POST.get("email",'')
    phone = request.POST.get("phone",'')
    query = request.POST.get("query",'')
    submit=request.POST.get("submit")
    contact = Contact(name=name, email=email,phone=phone,query=query)
    contact.save()
    if contact.save()==True:
        print("data ")
    print("data entered ")
    return redirect("/shop/contact us")

def Mobile(request):
    products=Product.objects.filter(category="Mobile")
    pro={"product":products}
   # return HttpResponse(products)
    return render(request, "shop/Mobile.html",pro)

def Home(request):
    products = Product.objects.filter(category="Home Appliances")
    pro = {"product": products}
    return render(request, 'shop/Home_Appliances.html', pro)

def Laptop(request):
    products = Product.objects.filter(category="Laptop")
    pro = {"product": products}
    return render(request, 'shop/laptop.html', pro)
def Accessories(request):
    products = Product.objects.filter(category="Accessories")
    pro = {"product": products}
    return render(request, 'shop/Accessories.html', pro)




def checkout(request):
    return HttpResponse('checkout')

