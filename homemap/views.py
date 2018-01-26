from django.shortcuts import render,redirect
from .modelsmap import Restaurant
from .models import restaurantInfo

# Create your views here.
def index(request):
    title = "Food Table"
    restaurant = Restaurant()
    restaurantss = restaurant.all()
    return render(request,'homemap/index.html',locals())

def create(request):
    if request.method == "POST":
        id = request.POST['id']
        restaurantname = request.POST['restaurantname']
        foodtype = request.POST['foodtype']
        address = request.POST['address']
        phone = request.POST['phone']
        website = request.POST['website']
    
        #資料新增
        restaurant = Restaurant()
        datas = tuple([id,restaurantname,foodtype,address,phone,website])
        restaurant.create(datas)
        
        return redirect("/")

    title = "餐廳新增"
    return render(request,'homemap/create.html',locals())

def delete(reqeust, id):
    restaurant = Restaurant()
    restaurant.delete(id)
    return redirect("/")

def update(request,id):
    if request.method == "POST":
        id = request.POST['id']
        restaurantname = request.POST['restaurantname']
        foodtype = request.POST['foodtype']
        address = request.POST['address']
        phone = request.POST['phone']
        website = request.POST['website']

        #資料修改
        restaurant = Restaurant()
        datas = tuple([id,restaurantname,foodtype,address,phone,website,id])
        restaurant.update(datas)

        return redirect("/")

    title = "餐廳修改"
    restaurant = Restaurant()
    restaurantss = restaurant.all()


    restaurant = Restaurant()
    singlepicked = restaurant.single(id)

    return render(request,'homemap/update.html',locals())

def select(request):
    address=request.GET['select']
    restaurant = Restaurant()
    restaurantslc = restaurant.select(address)
    return render(request,'homemap/index.html',locals())

def foodcollection(request):
    title='find the delicious around'
    return render(request,'homemap/foodcollection.html',locals())

def about(request):
    title='We dedicate your Cuisine Recommend'
    return render(request,'homemap/about.html',locals())