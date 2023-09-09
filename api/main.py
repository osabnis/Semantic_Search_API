from fastapi import FastAPI
import uvicorn
from api.app.routers import modeling, preprocessing

app = FastAPI(title="Semantic Search API 😊",
              description="This API hosts all the endpoints for the SemSe application with different namespaces for preprocessing and modeling!")

# app.include_router(preprocessing.router)
app.include_router(modeling.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
