from sqlalchemy import MetaData
from databases import Database
from .config import CONFIG

try:
    db = Database(CONFIG.DATABASE_URL)
    
except Exception as e:
    raise Exception('Invalid or missing database URL') from e

metadata = MetaData()
