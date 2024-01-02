from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
 return {"message": "Hello World"}

@app.get("/hello/{user}")
async def greeting(user):
 return {"Hello": user}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
