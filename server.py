#!/usr/bin/env python3
"""
Localhost Development Server for Aspire College Taunsa Website
"""
import http.server
import socketserver
import os
import sys
import webbrowser
import socket

# Ensure working directory is the script directory
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_DIR)

DEFAULT_PORT = 8000

def find_available_port(start_port=8000, max_attempts=20):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

def run(port=None, auto_open=True):
    if port is None:
        port = find_available_port(DEFAULT_PORT)

    handler = CustomHandler
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}"
        print("=" * 65)
        print("   ASPIRE COLLEGE TAUNSA - LOCALHOST WEB SERVER")
        print("=" * 65)
        print(f"  * Main Website:   {url}/")
        print(f"  * Student Portal: {url}/portal.html")
        print(f"  * Serving from:   {PROJECT_DIR}")
        print("=" * 65)
        print("Press Ctrl+C to stop the server at any time.\n")
        sys.stdout.flush()

        if auto_open:
            webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
            print("Server stopped.")

if __name__ == "__main__":
    port_arg = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    no_open = "--no-browser" in sys.argv
    run(port=port_arg, auto_open=not no_open)
