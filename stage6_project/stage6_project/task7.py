from .models import product
# 2. Within your project folder, create a new python file and save it as task7.py. Import the Product model to this file, and illustrate the following with the use of Django ORM:
# I. Insert a new record into the Product Model
x = product(product_name="yam", product_price="500")
x.save()
# ii. Get all the records in the Product table
all_entries = product.objects.all()
all_entries

# iii. Filter products by their name
x = product(product_name="yam").filter( product_price="500").last()

   
# iv. Get a single record from the product table
one_entry=product.objectsget(product_name="yam")
one_entry.save()

# v. Change a product price
one_entry.product_price="600"
one_entry.save()

# N/B: Use the .save() method where necessary

git remote add origin https://github.com/michae1l/django_stage6.git
git branch -M main
git push -u origin main