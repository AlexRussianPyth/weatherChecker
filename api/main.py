import uvicorn
import config
from fastapi import FastAPI

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000, # так как порт 8000 уже занят нашей админкой
    )
