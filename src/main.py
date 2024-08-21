from fastapi import FastAPI
from routes.user import router as create_user_router
from routes.board import router as board_router

app = FastAPI()


app.include_router(create_user_router, prefix="/v1", tags=["user"])
app.include_router(board_router, prefix="/v1", tags=["board"])

@app.get("/gaechu")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)