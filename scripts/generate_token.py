
import base64
import hashlib
import hmac
import json
import time

SECRET = "http-hands-on-demo-secret-change-before-production"
ISSUER = "student-key"


def base64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def generate_token(secret=SECRET, expires_in=3600):
    header = {"alg": "HS256", "typ": "JWT"}

    now = int(time.time())
    payload = {
        "iss": ISSUER,
        "iat": now,
        "exp": now + expires_in,
    }

    encoded_header = base64url(
        json.dumps(header, separators=(",", ":")).encode()
    )
    encoded_payload = base64url(
        json.dumps(payload, separators=(",", ":")).encode()
    )

    message = f"{encoded_header}.{encoded_payload}"

    signature = hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256,
    ).digest()

    return f"{message}.{base64url(signature)}"


if __name__ == "__main__":
    print(generate_token())

