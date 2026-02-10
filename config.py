import os


import dotenv


dotenv.load_dotenv(".env")

PROXY= os.environ.get("PROXY")
PROXY_USER= os.environ.get("PROXY_USER")
PROXY_PASSWORD= os.environ.get("PROXY_PASSWORD")
PROXY_IP= os.environ.get("PROXY_IP")
PROXY_PORT= os.environ.get("PROXY_PORT")