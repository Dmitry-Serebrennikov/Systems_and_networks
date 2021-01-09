import rsa
import base64

(public_key, private_key) = rsa.newkeys(1024)

def check_rsa():
    message = b'Rivest, Shamir and Adleman'
    crypto = rsa.encrypt(message, public_key)
    print(crypto)
    message = rsa.decrypt(crypto, private_key)
    print(message)

def encrypt_rsa_with_base64(message: str) -> bytes:
    crypto = rsa.encrypt(message.encode(), public_key)
    return base64.b64encode(crypto)

def decrypt_rsa_with_base64(crypto: bytes) -> str:
    raw = base64.b64decode(crypto)
    return str(rsa.decrypt(raw, private_key))

if __name__ == '__main__':
    crypto_message = encrypt_rsa_with_base64('Rivest, Shamir and Adleman')
    print(crypto_message)
    print(decrypt_rsa_with_base64(crypto_message))