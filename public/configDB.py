import pymssql,os,json
import configparser
from public.logger import Logger
from comman.file_path import CONFIG_PATH

logger = Logger(logger_name='MyDB').getlog()

class MyDB:
    global host,username,password,database,dbconfig
    config = configparser.ConfigParser()
    config.read(os.path.join(CONFIG_PATH,'config.ini'))
    host = config.get('dataBase','host')
    username = config.get('dataBase','username')
    password = config.get('dataBase', 'password')
    database = config.get('dataBase','database')

    dbconfig = {
        'host':str(host).strip(),
        'username':username,
        'password':password,
        'database':database
    }

    def __init__(self):
        self.database = None
        self.cursor = None

    def connectDB(self):
        try:
            self.conn = pymssql.connect(host,username,password,database)
            self.cursor = self.conn.cursor(as_dict=True)
            logger.info('DB connect successfully!')
        except ConnectionError as ex:
            logger.error(str(ex))

    def executeSQL(self,sql):
        self.connectDB()
        self.cursor.execute(sql)
        #self.conn.commit()
        return self.cursor

    def get_all(self,cursor):
        value = cursor.fetchall()
        return value

    def get_one(self,cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.database.close()
        logger.info('DATABASE CLOSED!')

if __name__ == '__main__':
    d = MyDB()
    print(username)
    sql ='''SELECT top 5 DeviceId,OfficeId,Name,Model FROM Device'''
    s =d.executeSQL(sql)

    a=d.get_all(s)
    print(a)
    b=json.dumps(str(a))
    b=b.replace('UUID','')
    print(json.loads(b))
    for device in a:
        device = list(device)
        print(device)

