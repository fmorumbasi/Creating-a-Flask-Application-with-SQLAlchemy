'''
We import all modules that needed by our application. 
We import Flask to create an instance of a web application, 
request to get request data, jsonify to turns the JSON output 
into a Response object with the application/json mimetype, 
SQAlchemy from flask_sqlalchemy to accessing database, 
and Marshmallow from flask_marshmallow to serialized object.
'''


from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

# intialize the flask application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pmysql://<mysql_username>:<mysql_password>@mysql_host'
db - SQLAlchemy(app)

'''
we configure the SQLAlchemy database URI to use our MySQL DB URI, 
and then we create an object of SQLAlchemy named as db, which will 
handle our ORM-related activities.
'''

#CREATE A DATABASE

'''
We’ll now create a product database application that will provide RESTful 
CRUD APIs. All the products will be stored in a table titled "products".

After the declared DB object, add the following lines of code to declare 
a class as Product which will hold the schema for the products table:
'''


###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,title,productDescription,productBrand,price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
    def __repr__(self):
        return '' % self.id
db.create_all()

'''

we have created a model titled "Product" which has five fields— ID is a self-generated and auto-incremented integer which will serve as a primary key. “db.create_all()” which instructs the application to create all the tables and database specified in the application.
'''

#DESIGNING ENDPOINTS FOR CRUD

'''
After setting up our model and return schema, we can jump to creating our endpoints. Let’s create our first GET /products endpoint to return all the 
'''

# THE GET METHOD

@app.route('/products', methods = ['GET'])
def index():
    get_products = Product.query.all()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))

'''
In this method, we are fetching all the products in the DB, dumping it in the ProductSchema, and returning the result in JSON.
'''



