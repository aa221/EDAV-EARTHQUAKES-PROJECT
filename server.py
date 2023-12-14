import http.server
import socketserver

# Define the CORSRequestHandler
class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Create an instance of the server with the custom CORSRequestHandler
with socketserver.TCPServer(("", 8000), CORSRequestHandler) as httpd:
    print("Serving at port 8000")
    httpd.serve_forever()