from datetime import datetime, timedelta
from typing import Optional

from jose import jwt


def sign_token(data: dict, secret_key, algorithm, expires_delta: Optional[timedelta] = None):
    """ 
    Args:
        data: dictionary of data
        secret_key: string of secret key
        algorithm: string indicating the algorithm to sign with
        expires_delta: unix timestamp of when JWT expires

    Returns:
        encoded jwt

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def decode_token(token: str, secret_key: str, algorithm: str):
    """ decode JWT and return payload

    Args:
        token: JWT
        secret_key: string secret key
        algorithm: string const representing algorithm

    Returns:
        dict: payload containing data

    """
    return jwt.decode(token, secret_key, algorithms=[algorithm])
