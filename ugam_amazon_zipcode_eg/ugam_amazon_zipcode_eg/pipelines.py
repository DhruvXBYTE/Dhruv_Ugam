# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from ugam_amazon_zipcode_eg.config import *
import pymysql
import time

class UgamAmazonZipcodeEgPipeline:

    try:
        print('hello')
        con = pymysql.connect(host=db_host, user=db_user, password=db_passwd)
        db_cursor = con.cursor()
        create_db = f"create database if not exists `{db_name}` CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
        db_cursor.execute(create_db)
        time.sleep(3)
        con.close()
        con = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name, autocommit=False,
                              use_unicode=True, charset="utf8")
        cursor = con.cursor()
        print(cursor)
        # create branch table
        try:
            product_create = f"CREATE TABLE " + product_table + """(
                                                                `ID` int(10) NOT NULL AUTO_INCREMENT,
                                                                  `Status` varchar(10) DEFAULT NULL,
                                                                  `page_Status` text,
                                                                  `cat_id` int(11) DEFAULT NULL,
                                                                  `HtmlPath_search` text,
                                                                  `HtmlPath` text,
                                                                  `product_name` text,
                                                                  `Product_URL` text,
                                                                  `postcode` text,
                                                                  `ProductID` varchar(200) DEFAULT NULL,
                                                                  `base_unique_id` text,
                                                                  `Ships_from` text,
                                                                  `Sold_by` text,
                                                                  `earliest_delivery_date` text,
                                                                  `Fastest_delivery` text,
                                                                  `extraction_date` text,
                                                                  `promo_message` text,
                                                                  `Stock_Status` text,
                                                                  `site_category_path` text,
                                                                  `Price` text,
                                                                  PRIMARY KEY (`ID`),
                                                                  KEY `NewIndex1` (`Status`),
                                                                  KEY `NewIndex2` (`ProductID`)
                                                                ) ENGINE=MyISAM AUTO_INCREMENT=262141 DEFAULT CHARSET=utf8"""

            insert_table=f"""INSERT INTO {product_table} (`Product_URL`,`postcode`) SELECT `Final_url`,`zipcode` FROM {db_input_sku}"""
            print(product_create)

            print(product_create)
            cursor.execute(product_create)
            cursor.execute(insert_table)
            con.commit()
        except Exception as e:
            print(e)
            print(" TABLE ALREADY CREATED! ")

    except Exception as e:
        print(e)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        try:
            field = []
            value = []
            for key in item:
                field.append(f"{str(key)}")
                value.append(f"{str(item[key])}")
            update = ",".join([key + ' = ' + f'"{value}"' for key, value in zip(field[1:], value[1:])])
            # print("data print:", item[key])
            print(update)
            self.cursor.execute(f"UPDATE {product_table} SET {update} where ID='{item['ID']}'")
            self.con.commit()

        except Exception as e:
            print(e)



