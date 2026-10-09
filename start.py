import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Make sure the server runs from this script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"

    print(f"Website running at {url}")

    webbrowser.open(url)

    httpd.serve_forever()
