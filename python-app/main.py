from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = os.getenv("MESSAGE")
        self.wfile.write(bytes(message, "utf-8"))
        return


def run(server_class=HTTPServer, handle_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handle_class)
    print(f"starting http server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
