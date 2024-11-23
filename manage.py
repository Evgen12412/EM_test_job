import uvicorn


def start_server():
    uvicorn.run(
        app="app.main:app",
        host="localhost",
        port=8888,
        workers=1
    )

if __name__=="__main__":
    start_server()