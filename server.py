"""
Desc: ackend for the online store
AUthor: Gary Galvin
"""

from flask import Flask, abort, request 
from test1 import about_me
from mock_data import catalog
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi There!!"

@app.route("/about")
def about():
    return f"{about_me['name']} {about_me['last']}"


"""
API ENDPOINTS
"""

@app.route("/api/catalog")
def retrieve_catalog():
    return json.dumps(catalog) 


@app.route("/api/catalog", methods=["post"])
def save_catalog():
    product = request.get_json()
    print(product)

    product._id = ["234"]
    catalog.append(product)

    return json.dumps(product)


@app.route("/api/product/<id>")
def get_product(id):

    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    return abort(404)


@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    res = []
    
    for prod in catalog:
        if prod["category"] == category:
            res.append(prod)



    return json.dumps(res)


@app.route("/api/products/cheapest")
def get_cheapest_product():
    cheapest_prod = catalog[0]

    for prod in catalog:
        if(prod["price"] < cheapest_prod["price"]):
            cheapest_prod = prod
    return json.dumps(cheapest_prod)


@app.route("/api/products/categories")
def get_unique_categories(): 
    categories = []
    for prod in catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)
    return json.dumps(categories)

# REMOVE BEFORE DEPLOYING
app.run(debug=True)