from http.server import BaseHTTPRequestHandler
import json

'''
@app.route("/")
def form(request):
    return HTMLResponse(
        # copied from https://github.com/simonw/cougar-or-not/blob/master/cougar.py
        """
        Submit a URL:
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)

'''
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        #self.wfile.write(str("Hello from Python on Now 2.0!").encode())
        json_string = json.dumps({'test':'get'})
        self.wfile.write(json_string.encode(encoding='utf_8'))
        return

    def do_POST(self):
        self.send_response(201)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.request
        json_string = json.dumps({'test': 'post'})
        self.wfile.write(json_string.encode(encoding='utf_8'))
        return
