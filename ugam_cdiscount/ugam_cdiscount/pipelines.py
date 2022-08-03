# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from ugam_cdiscount.config import *
import pymysql


class UgamCdiscountPipeline:

    try:
        print('hello')
        con = pymysql.connect(host=db_host, user=db_user, password=db_pass)
        db_cursor = con.cursor()
        create_db = f"create database if not exists {db_name} CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
        db_cursor.execute(create_db)
        con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, autocommit=True,
                              use_unicode=True, charset="utf8")
        cursor = con.cursor()
        # create branch table
        # try:
        #     createtable = catpdp.create_table()
        #     cursor.execute(createtable)
        # except Exception as e:
        #     logger.error('create brand error in pip:{}'.format(e))
        # create link data table
        try:
            create = catpdp.create_table()
            query = [i for i in create.split(';') if i]
            for i in query:
                cursor.execute(i)
                con.commit()
            # print(productcreatetable)
            # cursor.execute(productcreatetable)
        except Exception as e:
            # print('create linkdata error in pip:', e)
            logger.error('create linkdata error in pip:{}'.format(e))
        if db_cursor:
            print('data base already exists ............')
            if cursor:
                print('table already exists ................')
            else:
                pass
        else:
            pass
    except Exception as e:
        # print('connection error in pip:', e)
        logger.error('connection error in pip:{}'.format(e))


    def process_item(self, item, spider):
        return item

# UgamCdiscountPipeline()