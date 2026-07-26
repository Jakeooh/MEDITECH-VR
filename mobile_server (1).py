import http.server
import socketserver
import socket
import os
import sys
import ssl

PORT = 8080

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def print_qr(url):
    # Simple QR code generation using only standard library prints is hard without large lookup tables.
    # We will just print the URL clearly.
    print("\n" + "="*60)
    print("  MEDICARD VR MOBILE SERVER")
    print("="*60)
    print(f"\n  To view on your mobile phone:")
    print(f"  1. Ensure your phone is on the SAME WiFi network as this PC.")
    print(f"  2. Open your mobile browser (Chrome/Safari).")
    print(f"  3. Type this address exactly:\n")
    print(f"     >>   http://{get_ip()}:{PORT}   <<\n")
    print("="*60 + "\n")

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    ip = get_ip()
    
    # Change directory to script location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check for SSL
    cert_file = "cert.pem"
    key_file = "key.pem"
    use_ssl = os.path.exists(cert_file) and os.path.exists(key_file)
    
    protocol = "https" if use_ssl else "http"
    url = f"{protocol}://{ip}:{PORT}"
    
    print_qr(url)
    
    print(f"Serving at port {PORT} ({protocol.upper()})")
    
    try:
        # Create TCP Server first
        httpd = socketserver.TCPServer(("", PORT), Handler)
        
        if use_ssl:
            print("  [SECURE MODE ENABLED]")
            print("  Accept the 'Not Secure' warning on your device to proceed.")
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile=cert_file, keyfile=key_file)
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
