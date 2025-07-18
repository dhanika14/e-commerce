from django.shortcuts import render # type: ignore

from customer.models import Customer
from state.models import State
from franchise.models import Franchise
from district.models import District
from taluka.models import Taluka
from village.models import Village
from slider.models import Slider
from category.models import Category
from brands.models import Brands
from contactus.models import Contactus
from product.models import Product
from wishlist.models import Wishlist
from cart.models import Cart

from checkout.models import Checkout
from order.models import Order
from django.contrib import messages # type: ignore
from django.shortcuts import redirect # type: ignore





def contactus(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
    }

    return render(request, 'contactus.html', data)
    
  
def sub(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        enquiry = request.POST.get("enquiry", "")

     
        insert = Contactus(
            contact_name=name,
            contact_email=email,
            contact_enquiry=enquiry
        )
        insert.save( )
        
    
    return render(request, "contactus.html") 




def about(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/login")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
    }

    return render(request, 'about.html', data)
    
def home(request):
    user_id = request.session.get('user_id')  
    user_name = request.session.get('user_name', None)

    # Check if the user is logged in
    if user_id:
        try:
            customer = Customer.objects.get(c_id=user_id)
        except Customer.DoesNotExist:
            return redirect("/")  # Redirect to home or login page if customer does not exist
        wishlistdata = Wishlist.objects.filter(c_id=customer)
        cartdata = Cart.objects.filter(c_id=customer)
    else:
        wishlistdata = []  # Empty list if not logged in
        cartdata = []  # Empty cart if not logged in

    sliderdata = Slider.objects.all()
    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    productdata = Product.objects.all()[:4]  
    plist = Product.objects.all()[86:90]  

    # Calculate discount
    for product in productdata:
        product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))
    for product in plist:
        product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))

    # Calculate total price for logged-in users
    cart_items = []
    total_price = 0

    if user_id:
       for item in cartdata:
        # Ensure cart_quantity is a valid integer
        cart_quantity = str(item.cart_quantity).strip()  # Convert to string and strip spaces
        cart_quantity = int(cart_quantity) if cart_quantity.isdigit() else 0

        # Ensure sale price is a valid float
        try:
            sale_price = float(item.product_id.sale)
        except (ValueError, TypeError):
            sale_price = 0.0  # Default to 0.0 if conversion fails

        # Calculate total price
        item_total = cart_quantity * sale_price
        total_price += item_total

        # Append to cart items
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': cart_quantity,
            'sale_price': sale_price,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })


    data = {
        "list": sliderdata,
        "category": categorydata,
        "brand": branddata,
        "cart": cart_items,  
        "wishlist": wishlistdata,  
        "total_price": total_price,
        "user_name": user_name,
        "plist": productdata,
        "product": plist  
    }

    return render(request, 'home.html', data)


def logout(request):
    request.session.flush()  # Clear session data
    return redirect("/")  # Redirect to home page
 


def registration(request):
    if request.method == "POST":
        full_name_eng = request.POST.get("fullNameEng")
        full_name_marathi = request.POST.get("fullNameMarathi")
        mobile = request.POST.get("mobile")
        birth_date = request.POST.get("birthDate")
        state_id = request.POST.get("state")
        franchise_id = request.POST.get("franchise")
        district_id = request.POST.get("district")
        taluka_id = request.POST.get("taluka")
        village_id = request.POST.get("village")
        pin_code = request.POST.get("pinCode")
        email = request.POST.get("email")
        password = request.POST.get("password")

        state = State.objects.get(state_id=state_id)
        franchise = Franchise.objects.get(franchise_id=franchise_id)
        district = District.objects.get(district_id=district_id) 
        taluka = Taluka.objects.get(taluka_id=taluka_id) 
        village = Village.objects.get(village_id=village_id)

        customer = Customer(
            c_fullNameEng=full_name_eng,
            c_fullNameMarathi=full_name_marathi,
            c_mobile=mobile,
            c_birthDate=birth_date,
            state=state,
            franchise=franchise,
            District=district,
            taluka=taluka,
            village=village,
            c_pinCode=pin_code,
            c_email=email,
            c_password=password
        )
        customer.save()
        return redirect("/login/")

    states = State.objects.all()
    franchises=Franchise.objects.all()
    districts = District.objects.all()
    talukas = Taluka.objects.all()
    villages = Village.objects.all()
    return render(request, "registration.html", {
        "states": states,
        "districts": districts,
        "talukas": talukas,
        "villages": villages,
        "franchises":franchises
    })
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
    user_name = request.session.get('user_name', None)
    cartdata=Cart.objects.all()
    wishlistdata=Wishlist.objects.all()
    cartdata = Cart.objects.filter(c_id=request.session.get('user_id')) if user_name else []
    wishlistdata = Wishlist.objects.filter(c_id=request.session.get('user_id')) if user_name else []

    data={
       
        "category":categorydata,
        "brand":branddata,
        "user_name": user_name,
        "cart":cartdata,
        "wishlist":wishlistdata
        
   }
    return render(request,'regestration.html',data)  


def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        try:
            customer = Customer.objects.get(c_email=email, c_password=password)


            request.session['user_email'] = email
            request.session['user_name'] = customer.c_fullNameEng  

            request.session['user_id'] = str(customer.c_id)
            print(f"DEBUG: Customer ID from session: {request.session.get('user_id')}")
  

            return redirect("/")  
        except Customer.DoesNotExist:
            error_message = "Invalid email or password. Please try again."
    
    return render(request, 'login.html', {"error": error_message})
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
    user_name = request.session.get('user_name', None)
    cartdata=Cart.objects.all()
    wishlistdata=Wishlist.objects.all()
    cartdata = Cart.objects.filter(c_id=request.session.get('user_id')) if user_name else []
    wishlistdata = Wishlist.objects.filter(c_id=request.session.get('user_id')) if user_name else []
    data={
       
        "category":categorydata,
        "brand":branddata,
        "user_name": user_name,
        "cart":cartdata,
        "wishlist":wishlistdata
        
   }
    return render(request,'login.html',data)      
def general(request):
    # if 'user_id' not in request.session: 
        # return redirect("/")  
    user_id = request.session.get('user_id')  
    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  
    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)
    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price
    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })
    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata=Product.objects.all()[18:92]  

    for product in productdata:
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
        "general":productdata
    }

    return render(request, 'general.html', data)
     

def grocery(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)


    productdata = Product.objects.filter(category__category_name="Grocery")

    for product in productdata:
       
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))


    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,


        "grocery":productdata

    }

    return render(request, 'grocery.html', data)
    


def Spices(request):
#    if 'user_id' not in request.session: 
        # return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata = Product.objects.filter(category__category_name="Spices")

    for product in productdata:
       
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))
    


    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
        "Spices" : productdata
    }

    return render(request, 'Spices.html', data)
    
    

def cosmetic(request):
   
    # if 'user_id' not in request.session: 
        # return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata = Product.objects.filter(category__category_name="Cosmetic")

    for product in productdata:
       
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
        "cosmetic": productdata
    }

    return render(request, 'cosmetic.html', data)

def fooditems(request):
#    if 'user_id' not in request.session: 
        # return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata = Product.objects.filter(category__category_name="Food Items")

    for product in productdata:
       
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
        "fooditems": productdata
    }

    return render(request,'fooditems.html', data)
    
def shop(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata=Product.objects.all()
    user_name = request.session.get('user_name', None)



    for product in productdata:
        product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))
        

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,

        "plist":productdata,

       
       

    }

    return render(request, 'shop.html', data)

def stationary(request):
    # if 'user_id' not in request.session: 
        # return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)
    productdata = Product.objects.filter(category__category_name="Stationary")

    for product in productdata:
       
       product.discount = "{:.2f}".format(float(product.mrp) - float(product.sale))
    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
        "stationary":productdata
    }

    return render(request, 'stationary.html', data)
    

   
def submit(request):
     if request.method == "POST":
      fullNameEng = request.POST.get('fullNameEng')
      fullNameMarathi = request.POST.get('fullNameMarathi')
      mobile = request.POST.get('mobile')
      birthDate = request.POST.get('birthDate')
      pinCode = request.POST.get('pinCode')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirmPassword = request.POST.get('confirmPassword')
      state = request.POST.get('state')
      district = request.POST.get('district')
      taluka = request.POST.get('taluka')
      village = request.POST.get('village')
      franchise = request.POST.get('franchise')
      insertquery=Customer(
          fullNameEng=fullNameEng,
          fullNameMarathi=fullNameMarathi,
          mobile=mobile,
          birthDate=birthDate,
          pinCode=pinCode,
          email=email,
          password=password,
          confirmPassword=confirmPassword,
          state=state,
          district=district,
          taluka=taluka,
          village=village,
          franchise=franchise,

      )
      insertquery.save()
      return redirect("/login/")
     else:
        return render(request,'registration.html')
     


def cart_submit(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        cart_quantity = request.POST.get("cart_quantity", 1)
        cart_price = request.POST.get("cart_price")
        redirect_url = request.POST.get("redirect_url", "/")  # Default to homepage if not provided

        c_id = request.session.get('user_id')
        if not c_id:
            return redirect(redirect_url)

        try:
            customer = Customer.objects.get(c_id=int(c_id))
            product = Product.objects.get(product_id=product_id)
        except (Customer.DoesNotExist, Product.DoesNotExist):
            return redirect(redirect_url)

        Cart.objects.create(
            product_id=product,
            c_id=customer,
            cart_quantity=cart_quantity,
            cart_price=cart_price
        )

        return redirect(redirect_url)

    return redirect("/")




def view_cart(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0

    if user_id:
       for item in cartdata:
        # Ensure cart_quantity is a valid integer
        cart_quantity = str(item.cart_quantity).strip()  # Convert to string and strip spaces
        cart_quantity = int(cart_quantity) if cart_quantity.isdigit() else 0

        # Ensure sale price is a valid float
        try:
            sale_price = float(item.product_id.sale)
        except (ValueError, TypeError):
            sale_price = 0.0  # Default to 0.0 if conversion fails

        # Calculate total price
        item_total = cart_quantity * sale_price
        total_price += item_total

        # Append to cart items
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': cart_quantity,
            'sale_price': sale_price,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })
 

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
    }

    return render(request, 'view_cart.html', data)

def wishlist(request):
    if 'user_id' not in request.session: 
        return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)

    # Calculate total price
    cart_items = []
    total_price = 0  # Initialize total price

    for item in cartdata:
        item_total = int(item.cart_quantity) * float(item.product_id.sale)  # Multiply quantity and price
        total_price += item_total
        cart_items.append({
            'product_img': item.product_id.product_img,
            'product_name': item.product_id.product_name,
            'cart_quantity': item.cart_quantity,
            'sale_price': item.product_id.sale,
            'total_price': item_total,
            'cart_id': item.cart_id,
        })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
    }

    return render(request, 'wishlist.html', data)


def wishlistdelete(request, id):
    wishlist= Wishlist.objects.get(wish_id=id)
    wishlist.delete()
    return redirect("/wishlist/")


def wishlist_add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        c_id = request.session.get('user_id')

        if not c_id:
            return redirect("/") 

        try:
            customer = Customer.objects.get(c_id=int(c_id)) 
        except Customer.DoesNotExist:
            return redirect("/") 

        
        if Wishlist.objects.filter(c_id=customer, product_id=product_id).exists():
            return redirect("/") 

       
        insert = Wishlist(
            product_id=Product.objects.get(product_id=product_id),
            c_id=customer
        )
        insert.save()
        
    return redirect("/")

def cartdelete(request, id):
    items= Cart.objects.get(cart_id=id)
    items.delete()
    return redirect("/view_cart/")

def slider(request):
    sliderdata= slider.objects.all()
    data={
        "list":sliderdata
    }
    return render(request,'home.html',data)


def showitem(request):
    if 'user_id' not in request.session:  # Ensure user is logged in
        return redirect("/") 

    user_id = request.session.get('user_id')  # Get logged-in user ID


    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")

    # Fetch cart data for the logged-in user only
    cartdata = Cart.objects.filter(c_id=customer)
    
    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    user_name = request.session.get('user_name', None)
    
    wishlistdata = Wishlist.objects.filter(c_id=customer)  # Only logged-in user's wishlist

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cartdata,
        "wishlist": wishlistdata,
    }

    return render(request, 'checkout.html', data)



def checkout(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        coupon_code = request.POST.get('coupon_code')
        card_number = request.POST.get('card_number')
        agree_terms = request.POST.get('agree_terms') == 'on'
       
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect("/")  # Ensure user is logged in

        try:
            customer = Customer.objects.get(c_id=user_id)
        except Customer.DoesNotExist:
            messages.error(request, "Customer not found!")
            return redirect("/")

        cart_items = Cart.objects.filter(c_id=customer)
        if not cart_items:
            messages.error(request, "Your cart is empty!")
            return redirect("/cart/")

        # Delete previous orders to avoid duplication
        Order.objects.filter(c_id=customer).delete()

        # Create a new checkout entry
        checkout_entry = Checkout.objects.create(
            
            first_name=first_name,
            email=email,
            telephone=phone,
            address=address,
            payment_method=payment_method,
            coupon_code=coupon_code,
            card_number=card_number,
             agree_terms=agree_terms,
 )

        # Process cart items into orders
        for item in cart_items:
            cart_quantity = item.cart_quantity
            if cart_quantity is None or str(cart_quantity).strip() == "":
                cart_quantity = 1  # Default to 1 if missing

            Order.objects.create(
                c_id=customer,
                product_id=item.product_id,
                price=item.cart_price,
                quantity=int(cart_quantity),
            )

        # Store checkout ID in session
        request.session['latest_checkout_id'] = checkout_entry.checkout_id

        # Clear cart after checkout
        cart_items.delete()

        messages.success(request, "Order placed successfully! Your bill is ready.")
        return redirect("/thankyou/")  

    else:
        if 'user_id' not in request.session: 
            return redirect("/")  

    user_id = request.session.get('user_id')  

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        return redirect("/")  

    # Fetch cart data for the logged-in customer
    cartdata = Cart.objects.filter(c_id=customer)
    cart_items = []
    total_price = 0

    if user_id:
        for item in cartdata:
            cart_quantity = str(item.cart_quantity).strip()
            cart_quantity = int(cart_quantity) if cart_quantity.isdigit() else 1  # Ensure valid quantity

            try:
                sale_price = float(item.product_id.sale)
            except (ValueError, TypeError):
                sale_price = 0.0  # Default to 0.0 if conversion fails

            item_total = cart_quantity * sale_price
            total_price += item_total

            cart_items.append({
                'product_img': item.product_id.product_img,
                'product_name': item.product_id.product_name,
                'cart_quantity': cart_quantity,
                'sale_price': sale_price,
                'total_price': item_total,
                'cart_id': item.cart_id,
                
            })

    categorydata = Category.objects.all()
    branddata = Brands.objects.all()
    wishlistdata = Wishlist.objects.filter(c_id=customer)

    user_name = request.session.get('user_name', None)

    data = {
        "category": categorydata,
        "brand": branddata,
        "user_name": user_name,
        "cart": cart_items,
        "total_price": total_price,
        "wishlist": wishlistdata,
    }

    return render(request, 'checkout.html', data)


def bill(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect("/")

    try:
        customer = Customer.objects.get(c_id=user_id)
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found!")
        return redirect("/")

    # Get the latest checkout ID from session
    latest_checkout_id = request.session.get('latest_checkout_id')

    if not latest_checkout_id:
        messages.error(request, "No recent order found!")
        return redirect("/")

    
    checkout_entry = Checkout.objects.get(checkout_id=latest_checkout_id)

    
    orders = Order.objects.filter(c_id=customer)

    if not orders.exists():
        request.session.pop('latest_checkout_id', None)
        messages.warning(request, "Your bill has been cleared as no items exist!")
        return redirect("/")

    
    total_amount = sum(order.price * order.quantity for order in orders)

    context = {
        'checkout': checkout_entry,
        'orders': orders,
        'total_amount': total_amount
    }

    return render(request, 'bill.html', context)



def thankyou(request):
 return render(request,'thankyou.html')
 

