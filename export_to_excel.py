import os
import django
import pandas as pd

# Step 1: Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shivsamrajyaecommerce.settings')  #project name 
django.setup()

# Step 2: Import all models
from product.models import Product
from brands.models import Brands
from cart.models import Cart
from category.models import Category
from checkout.models import Checkout
from contactus.models import Contactus
from customer.models import Customer
from district.models import District
from order.models import Order
from taluka.models import Taluka
from tax.models import Tax
from village.models import Village
from wishlist.models import Wishlist
# Step 3: Define models in a dictionary
models = {
    "Products": Product,
    "Customers": Customer,
    "Orders": Order,
    "Checkout": Checkout,
    "Cart": Cart,
    "Wishlist": Wishlist,
    "Brands":Brands,
    "Contactus":Contactus,
    "District":District,
    "Taluka":Taluka,
    "Tax":Tax,
    "Village":Village,
}

# Step 4: Write all models to one Excel file with different sheets
with pd.ExcelWriter("all_model_data.xlsx", engine='openpyxl') as writer:
    for sheet_name, model in models.items():
        data = model.objects.all().values()
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("✅ All models exported to all_model_data.xlsx successfully.")

