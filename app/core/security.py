import os
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from jose import  jwt, JWTError
    

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

password_hash = PasswordHash.recommended()

# Password Hashing
def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_pasword(
            plain_password: str,
            hashed_pasword: str,
)->bool:
      return password_hash.verify(plain_password, hashed_pasword)


def create_access_token(user_id:int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id),
        "exp": expire      
    }


    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)