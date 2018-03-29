import os,json
from xlrd import open_workbook
from xml.etree import ElementTree as ET
from public.logger import Logger
from public.confighttp import ConfigHttp
from comman.file_path import DATA_PATH
from public.configDB import MyDB

localConfigHttp = ConfigHttp()
logger = Logger(logger_name='base_api').getlog()

def get_xls(xls_name,sheet_name):
    xls = []

    xlspath = os.path.join(DATA_PATH,'excel',xls_name)
    file = open_workbook(xlspath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_name':
            xls.append(sheet.row_values(i))
    return xls

database = {}
def get_xml_sql_dict():
    if len(database)== 0:
        sql_path = os.path.join(DATA_PATH,'SQL.xml')
        tree = ET.parse(sql_path)
        for db in tree.findall('database'):
            db_name = db.get('name')
            print(db_name)
            print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get('name')
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get('id')
                    sql_text = data.text
                    sql[sql_id] = sql_text.strip()
                table[table_name]=sql
            database[db_name] = table
    return database

def get_sql_dict(database_name,table_name):
    database=get_xml_sql_dict()
    sql_dict = database[database_name][table_name]
    return sql_dict

def get_sql(database_name,table_name,sql_id):
    db = get_sql_dict(database_name,table_name)
    sql = db.get(sql_id)
    return sql


def get_value_from_db(sql):
    mydb = MyDB()
    #sql ='''SELECT top 5 DeviceId,OfficeId,Name,Model FROM Device'''
    s =mydb.executeSQL(sql)
    values=mydb.get_all(s)
    # sql_result = []
    # for device in values:
    #     device = list(device)
    #     deviceid = str(device[0])
    #     officeid = str(device[0])
    #     device[0]=deviceid
    #     device[1]=officeid
    #     sql_result.append({'deviceId':deviceid})
    return values


def get_api_from_xml(name):
    api_list = []
    api_path = os.path.join(DATA_PATH,'interfaceURL.xml')
    tree = ET.parse(api_path)
    for url in tree.findall('url'):
        url_name = url.get('name')
        #print(url_name)
        if url_name == name:
            for c in url.getchildren():
                if c.text:
                    api_list.append(c.text)
            api = '/'.join(api_list)

    return api

def show_return_msg(response):
    """
    show msg detail
    :data response:
    :return:
    """
    url = response.url
    reason = response.text
    print("\n请求地址："+url)
    # 可以显示中文
    print("\n请求返回值："+'\n'+json.dumps(json.loads(reason), ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    get_xml_sql_dict()
    get_sql_dict('Backoffice', 'Device')



