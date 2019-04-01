from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
import uvicorn

app = Starlette(debug=True)

@app.route('/test-app')
async def test_app(request):
    return JSONResponse({'app':'working'})

@app.route('/')
async def homepage(request):
    return HTMLResponse(
        # from https://github.com/simonw/cougar-or-not/blob/master/cougar.py
        """
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select image to upload:
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>
        Or submit a URL:
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
        """
    )

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
