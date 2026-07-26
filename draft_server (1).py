import http.server
import ssl
import os

# Generates a temporary self-signed cert
def generate_cert():
    from datetime import datetime, timedelta
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives import serialization
        
        print("Rendering Secure Certificate...")
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Test"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"Test"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Test"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
        ])
        cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.utcnow()).not_valid_after(datetime.utcnow() + timedelta(days=1)).add_extension(x509.SubjectAlternativeName([x509.DNSName(u"localhost")]), critical=False).sign(key, hashes.SHA256())
        
        with open("cert.pem", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        with open("key.pem", "wb") as f:
            f.write(key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
        return True
    except ImportError:
        print("Cryptography module not found. Using ad-hoc SSL if available or failing.")
        return False

# Since we might not have cryptography installed, let's try a simpler approach if we can,
# or just rely on a premade cert if we absolutely had to. 
# BUT, we can use the 'ssl' module's internal capabilities if we had a cert.
# Let's try to find 'openssl' again? No.

# Plan B: We can't easily generate a cert without OpenSSL or Cryptography lib.
# HOWEVER, we can stick to standard lib if we have a cert. 
# I will create a dummy cert using a Powershell command which IS available on Windows.

pass
