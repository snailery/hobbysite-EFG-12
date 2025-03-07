from merchstore.models import Product, ProductType

product_types = [
    {
        "name": "Tops",
        "desc": "Clothing usually worn on the upper torso."
    },
    {
        "name": "Bottoms",
        "desc": "Clothing usually worn on the lower torso or legs."
    },
    {
        "name": "Shoes",
        "desc": "Protective coverings for the feet."
    }
]

products = [
    {
        "name": "Argyle sweater",
        "desc": "Simple & Elegant, Everyday/Comfy",
        "price": 1200,
        "prod_type": "Tops"
    },
    {
        "name": "Baseball shirt",
        "desc": "Active & Simple, Sporty/Work",
        "price": 1120,
        "prod_type": "Tops"
    },
    {
        "name": "Denim painter's pants",
        "desc": "Simple, Everyday/Outdoorsy",
        "price": 1560,
        "prod_type": "Bottoms"
    },
    {
        "name": "Tweed frilly skirt",
        "desc": "Cute & Simple, Everyday/Fairytale/Formal",
        "price": 1560,
        "prod_type": "Bottoms"
    },
    {
        "name": "Rain boots",
        "desc": "Simple, Everyday/Outdoorsy",
        "price": 490,
        "prod_type": "Shoes"
    },
    {
        "name": "Flower sandals",
        "desc": "Cute, Fairytale/Outdoorsy/Vacation",
        "price": 1200,
        "prod_type": "Shoes"
    }
]

for product_type in product_types:
    pt = ProductType()
    pt.name = product_type["name"]
    pt.desc = product_type["desc"]
    pt.save()
    print(f"Successfully added {pt}")

for product in products:
    p = Product()
    p.name = product["name"]
    p.desc = product["desc"]
    p.price = product["price"]
    p.prod_type = ProductType.objects.get(name=product["prod_type"])
    p.save()
    print(f"Successfully added {p}")

print("Successfully populated database.")
print(ProductType.objects.all())
print(Product.objects.all())

# exec(open("merchstore/populate_db.py").read())