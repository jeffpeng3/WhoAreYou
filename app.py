import fastapi
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import FileResponse
from starlette.requests import Request
from pprint import pprint
app = fastapi.FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request:Request, exc):
    print("="*20)
    pprint(request.scope)
    return FileResponse("static/index.html")

@app.get("/img/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
