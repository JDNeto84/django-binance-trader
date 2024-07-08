from cryptography.fernet import Fernet
from django.conf import settings
import base64
import hashlib

def get_fernet():
    secret_key = settings.SECRET_KEY.encode()
    key = base64.urlsafe_b64encode(hashlib.sha256(secret_key).digest())
    return Fernet(key)

def encrypt(text):
    fernet = get_fernet()
    return fernet.encrypt(text.encode()).decode()

def decrypt(token):
    fernet = get_fernet()
    return fernet.decrypt(token.encode()).decode()
