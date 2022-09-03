from fastapi.responses import HTMLResponse
from fastapi import FastAPI


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def hello_world():
    return """
    <html>
        <head>
            <title>RanchAround</title>
        </head>
        <body>
            <h1>Welcome to the rancharound website...</h1>
            <p>Under development, </p>
            <p>thanks for visiting,</p>
            <p>come back later.</p>
        </body>
    </html>
    """

@app.get("/api", response_class=HTMLResponse)
async def api_root():
    return """    
    <html>
        <head>
            <title>RanchAround API</title>
        </head>
        <body>
            <h1>Welcome to the rancharound api...</h1>
            <p>Under development, </p>
            <p>thanks for visiting,</p>
            <p>come back later.</p>
        </body>
    </html>
    """