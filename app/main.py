import uvicorn
from gachi_backend.asgi import application

# run through ASGI 
if __name__ == "__main__":
    config = uvicorn.Config(application, log_level="info")
    server = uvicorn.Server(config)
    server.run()
