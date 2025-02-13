import http.server
import socketserver
import socket

class GzipRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.gz'):
            self.send_header("Content-Encoding", "gzip")
        super().end_headers()

# Automatically find an available port
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))  # Bind to any free port
        return s.getsockname()[1]

PORT = find_free_port()
Handler = GzipRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()