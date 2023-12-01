from functools import lru_cache
import os

class Config:

    TG_APP_ID:int  = 23260418
    TG_APP_HASH :str  = '15418b8765dc3484bd9d6c7777304f27'
    SESSION_STRING     = '1BVtsOKYBu5TsanhejRFuPf-VghXzv6P72uccWWF6DjRk26P1tDwLn7e1WIwY0kJOttuTW1Kk00EZms4C43rTeNyK3cwbHIP2yTplxdvTMnUm5T_25Ck2NJwvsGj4eJe7XGRZAddmvqfbJ57WifGak25F-QkZvh_zJ5zgPWt9NGBdmnzgxVI98S-cjUStFbOqLvUV4WIb1E7tma7gtGpG_PKOFrsJsHgvdj226uAD8EtubTJfdWNSK4mHaVh42owGe8r3PKwnOcMuY2Ld741X5avnwQR1dU8TiNZEiXcnubCDkFBO-ugbS7fVzR5b6FS0pqom-116d8dSB1S76c6nqJ7rA84hgOU='
    ADMIN_UID:int
    
    DATABASE_URL    = 'postgres://malludb_user:fw4KhBitR5fqljBd9Y84YTz9NVScpZ0X@dpg-clk0e3t8td7s73d9k32g-a.singapore-postgres.render.com/malludb'


    APP_NAME        = 'Movie Blog'
    APP_DESC        = 'A simple telegram indexer for movie channel'
    APP_URL         = 'https://tgflix.herokuapp.com'

    BUFFER_SIZE:int                 = 1024
    MAX_ITEMS_PER_PAGE:int          = 20
    DOWNLOAD_ENABLED:bool           = True
    MAX_SIMULTANIOUS_DOWNLOAD:int   = 20
    
    DEFAULT_COVER_IMG:int   = 1
    DEBUG:bool              = True
    
    def __init__(self):
        for i in dir( self):
            if not i.startswith('__'):
                try:
                    self.__setattr__(i, os.getenv(i,self.__getattribute__(i)))
                except:
                    raise Exception('required env variables missing')


@lru_cache()
def get_config():
	return Config()

CONFIG = get_config()
