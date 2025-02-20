#!/usr/bin/python3
"""Develop a simple API using Python's http.server module"""
import http.server
import socketserver
import json


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    """This is a subclass of http.server.BaseHTTPRequestHandler"""
    def do_GET(self):
        """Handles GET requests with a text message"""
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/":
            self.send_response(200, message="Hello, this is a simple API!")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def start_server():
    """Starts the HTTP server on port 8000"""
    port = 8000
    with socketserver.TCPServer(("", port), SimpleRequestHandler) as httpd:
        print(f"Server on port {port}...")
        httpd.serve_forever()


if __name__ == "__main__":
    start_server()
