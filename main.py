from fastapi import FastAPI
app = FastAPI() #create an app object

@app.get("/")   #Tell us where the API is co
async def root():
    return {"message" : "No World"}

from fastapi import FastAPI

app = FastAPI() # Create an app object.

@app.get("/") # Tell us where the API is connecting.
async def root():
    return {"message": "ttttWorld"}

# Example of get.
@app.get("/about") # Then access http://127.0.0.1:8000/about
async def about():
    return {'Data': 'about'}

# Example of put.
@app.put("/putdata")
async def PutData():
    return {'Data': 'Values'}
async def DeletingData():
    return {'Data': 'Values'}

# Example of get with variables.
# Save then check http://127.0.0.1:8000/items/foo 
#@app.get("/items/{item_id}")
#async def read_item(item_id):
#    return {"item_id": item_id}

# Same as above but demanding that the parameter has a type.
# Save and run http://127.0.0.1:8000/items_int/foo again.
# Then try http://127.0.0.1:8000/items_int/3 . See the difference?
@app.get("/items_int/{item_id}")
async def read_item(item_id: int):
    if item_id == 42:
        return {'That is': 'The answer'}
    else:
        return {"item_id": item_id}
