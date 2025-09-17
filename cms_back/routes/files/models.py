from db import engine
from utils.logger import logger
from fastapi import UploadFile, File
from pathlib import Path
from config import config
import cloudinary
from cloudinary.uploader import upload
import requests
import urllib.request
import urllib.error

cloudinary.config(
  cloud_name = config['CLOUDINARY_CLOUD_NAME'], 
  api_key = config['CLOUDINARY_API_KEY'],  
  api_secret = config['CLOUDINARY_API_SECRET'], 
  secure = True
)

async def upload_file_cloud(file: UploadFile = File(...)):

    try:
        name = file.filename
        file_content = await file.read()
        result = upload(file_content, public_id=name[:name.index(Path(name).suffix)])
    
    except Exception as e:
        logger.debug(msg=e)
        return None
    
    return result['secure_url']

def upload_file_db(filename: str, filetype: str, url: str):
    
    try:
        with engine.connect() as connection:

            query = '''
                INSERT INTO file
                (
                FileName,
                FileType,
                FileURL
                )
                values
                (
                %s,
                %s,
                %s
                )
            '''

            values = (filename, filetype, url)
            result = connection.exec_driver_sql(query, values)

            if result.rowcount > 0:
                connection.commit()
                return True
            
            return False

    except Exception as e:
        logger.debug(msg=e)
        return None
    
def download_file(save_as: str, download_url: str):
    
    try:

        request = requests.get(download_url)
        logger.debug(request.content)

        if save_as:
            save_as += request.url[download_url.rfind('.'):]
        else:
            save_as = request.url[download_url.rfind('/') + 1:]

        with open(f'downloads/{save_as}', 'wb') as f:
            f.write(request.content)

        return True
  
    except Exception as e:
        logger.debug(msg=e)
        return None