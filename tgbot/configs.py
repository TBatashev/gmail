class Config :


    admin_ids : list = [
        111,222 ] 
    

    SQLALCHEMY_URL : str = 'sqlite+aiosqlite:///db.sqlite3'


    PostgreUSER : dict =  {
        'user' : 'posrgresql',
        'password' : 'islam95',
        'host' : 'localhost',
        'port' : '5432'
    }


