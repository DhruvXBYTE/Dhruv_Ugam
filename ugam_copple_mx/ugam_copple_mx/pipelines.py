# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from ugam_copple_mx.config import *

class UgamCoppleMxPipeline:

    try:
        con = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd)
        db_cursor = con.cursor()
        create_db = f"create database if not exists {db_name} CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
        db_cursor.execute(create_db)
        con = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_name, use_unicode=True,
                              charset="utf8")

        cursor = con.cursor()

        # create link data table
        try:
            create_table_query = dllobj.create_table()
            # cursor.execute(create_table_query)
            query = [i for i in create_table_query.split(';') if i]
            print(query)
            for result in query:
                cursor.execute(result)
                con.commit()

        except Exception as e:
            logger.error('create product_data_table error in pip:{}'.format(e))
            print(e)

    except Exception as e:
        logger.error('connection error in pip:{}'.format(e))


## ---------------- ----------  SCREENSHOT CHECK FOR MORE  ------------------------------

def screenshotcheckqa_for_more():
    UgamCoppleMxPipeline.cursor.execute(f"select screenshotpath,additional_header_2 from {product_data_table}")
    pathss=UgamCoppleMxPipeline.cursor.fetchall()
    # print(pathss)
    listimg = os.listdir(SCREENSHOT_FOLDER_PATH)
    sslist=[]
    for ih in pathss:
        sslist.append(ih[1])

    counter=0

    for i in listimg:
        if i not in sslist:
            print(i)
            print(f'{SCREENSHOT_FOLDER_PATH}\\{i}')
            counter+=1
            os.remove(f'{SCREENSHOT_FOLDER_PATH}\\{i}')
    print(counter)


