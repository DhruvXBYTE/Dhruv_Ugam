# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from ugam_lenovo_ca_price_daily.config import *
from ugam_lenovo_ca_price_daily.items import UgamLenovoCaPriceDailyItem
import pymysql

class UgamLenovoCaPriceDailyPipeline:
    try:
        print('hello')
        con = pymysql.connect(host=db_host, user=db_user, password=db_pass)
        db_cursor = con.cursor()
        create_db = f"create database if not exists {db_name} CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
        db_cursor.execute(create_db)
        con.close()
        con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, autocommit=True,
                              use_unicode=True, charset="utf8")
        cursor = con.cursor()

        """ ----create input_sku table--- """
        try:
            create_table = "create table if not exists " + db_category_table + """(
                                                                                      `Id` int(11) NOT NULL AUTO_INCREMENT,
                                                                                      `Retailer` varchar(200) DEFAULT NULL,
                                                                                      `Product ID` varchar(20) DEFAULT NULL,
                                                                                      `Product URL` mediumtext,
                                                                                      PRIMARY KEY (`Id`)
                                                                                      )"""
            cursor.execute(create_table)

        except Exception as e:
            logger.error('create input_sku error in pip:{}'.format(e))

        try:
            create = catpdp.create_table()
            query = [i for i in create.split(';') if i]
            for i in query:
                cursor.execute(i)
                con.commit()

            # insert = f"INSERT INTO {db_data_table} (`Retailer`,`Product ID`,`Product URL`) SELECT `Retailer`,`Product ID`,`Product URL` FROM input_sku"
            # cursor.execute(insert)
            # con.commit()

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
