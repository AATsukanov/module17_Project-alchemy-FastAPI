from fastapi import FastAPI
from routers import category
import uvicorn

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})

app.include_router(category.router)

@app.get('/')
async def welcome():
    return {'message': 'My Shop'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7500, log_level='info')