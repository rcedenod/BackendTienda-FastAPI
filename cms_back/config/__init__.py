import os
from dotenv import load_dotenv

# activamos las variables de entorno
load_dotenv()

config = {
    'DATABASE_URI': os.environ['DATABASE_URI'],
    'BCRYPT_SALT': os.environ['BCRYPT_SALT'],
    'JWT_KEY': os.environ['JWT_KEY'],
    'CLOUDINARY_URL': os.environ['CLOUDINARY_URL'],
    'CLOUDINARY_CLOUD_NAME' : os.environ['CLOUDINARY_CLOUD_NAME'],
    'CLOUDINARY_API_KEY' : os.environ['CLOUDINARY_API_KEY'],
    'CLOUDINARY_API_SECRET' : os.environ['CLOUDINARY_API_SECRET']
}
