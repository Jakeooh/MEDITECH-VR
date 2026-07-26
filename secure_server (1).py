import http.server
import ssl
import os
import socket
from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import ipaddress
from cryptography.hazmat.primitives import serialization

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def generate_self_signed_cert(ip_addr):
    # Generate private key
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # Generate a self-signed cert
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Meditech"),
        x509.NameAttribute(NameOID.COMMON_NAME, ip_addr),
    ])
    
    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.utcnow()).not_valid_after(datetime.utcnow() + timedelta(days=365)).add_extension(x509.SubjectAlternativeName([x509.DNSName(u"localhost"), x509.IPAddress(ipaddress.IPv4Address(ip_addr))]), critical=False).sign(key, hashes.SHA256())
    
    with open("key.pem", "wb") as f:
        f.write(key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
    
    with open("cert.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
        
    print(f"Certificate generated for {ip_addr}: cert.pem, key.pem")

# Main Execution
current_ip = get_local_ip()
print(f"Detected Local IP: {current_ip}")

# Always regenerate if IP changes or cert missing
generate_self_signed_cert(current_ip)

# Create server
# Use a custom handler to ensure .fbx and .obj files have correct MIME types if needed
class MedicalAssetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"[{datetime.now().time()}] Request: {self.path} from {self.client_address[0]}")
        if self.path == '/' or self.path == '/v10':
            self.path = '/app_v10.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

# Server setup
port = 8080
import mimetypes
mimetypes.add_type('application/octet-stream', '.fbx')
mimetypes.add_type('text/plain', '.obj')
mimetypes.add_type('text/plain', '.mtl')
mimetypes.add_type('model/gltf-binary', '.glb')
mimetypes.add_type('model/gltf+json', '.gltf')

httpd = http.server.HTTPServer(('0.0.0.0', port), MedicalAssetHandler)

# Wrap with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"\n🚀 MEDICARD VR SERVER RUNNING!")
print(f"🔗 Mobile Access: https://{current_ip}:{port}")
print(f"🔗 Local Access:  https://localhost:{port}")
print("\nPress Ctrl+C to stop.")
httpd.serve_forever()
