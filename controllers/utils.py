from passlib.context import CryptContext

# Create a password context object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Hash the password
def hash_pass(password:str):
    return pwd_context.hash(password)