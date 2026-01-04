from fastapi import FastAPI,Request
app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the World of python FastApi's"


@app.get("/about")
def about():
    return "ABout of pasge routing checking bolte ."


from mockdata import products
@app.get("/products")
def products_list():
    return products


## path parameter and query parameter
@app.get("/products/{count}")
def product_detail(count: int):
    for i in products:
        if i["count"] == count:
            return i
    return {"error": "Product not found"}    


# @app.get("/greet")
# def greet(name: str):
#     return f"hello, {name}!"


# @app.get("/greet")
# def greet(name:str,age:int):
#     return {"message":f"hello, {name}! you are {age} years old."}

# it's time to test the request param today 
@app.get("/greet")
def greet(req:Request):
    # return f"returning the name {req.query_params('name')} and age is {req.query_params.get('age')}"
    return f"hello,{req.query_params['name']}! you are {req.query_params['age']} years old.   "
    # q = dict(req.query_params)
    # return q
