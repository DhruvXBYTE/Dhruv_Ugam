# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Amazon_review.config import *
import pymysql
import time
from Amazon_review.items import *


class AmazonReviewPipeline:
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
                                                                `Id` INT(10) NOT NULL AUTO_INCREMENT,
                                                                `Master ASIN` text,
                                                                `ASIN` text,
                                                                `HtmlPath` text,
                                                                `Product_url` text,
                                                                `star_rating` text,
                                                                `review_title` text,
                                                                `review_detail` text,
                                                                `web_review_ID` text,  
                                                                `Author` text,
                                                                `reviewed_by` text,
                                                                `Review_Date` text,
                                                                `created_time` text,
                                                                `Response_Available` text,
                                                                `Scrape_date` text,
                                                                `Status` text,                                                                                  
                                                                 PRIMARY KEY (`Id`),
                                                                 KEY `NewIndex2` (`Id`)
                                                        )"""
            print(product_create)
            cursor.execute(product_create)
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
            field_list = []
            value_list = []
            for field in item:
                field_list.append(str(field))
                value_list.append(str(item[field]).replace("'", "’"))

            print(value_list)
            print(field_list)
            fields = ','.join(field_list)
            values = "','".join(value_list)
            # print(fields)
            # print(values)
            url = f" INSERT INTO {product_table}({fields}) VALUES('{values}')"
            print(url)
            self.cursor.execute(url)
            self.con.commit()
        except Exception as e:
            print(e)

    def insert_into(self, item):
        con = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name, autocommit=True,
                              use_unicode=True, charset="utf8")
        cursor = con.cursor()
        if isinstance(item, AmazonReviewItem):

            try:
                field_list = []
                value_list = []
                for field in item:
                    field_list.append(str(f'`{field}`'))
                    value_list.append(str(item[field]).replace("'", "’"))
                fields = ','.join(field_list)
                values = "','".join(value_list)
                # time.sleep(2)
                insert_db = "insert into " + product_table + "( " + fields + " ) values ( '" + values + "' )"
                print("insert===", insert_db)

                cursor.execute(insert_db)
                con.commit()
                print(insert_db)
                # self.insert_count += 1
                # print("\rData_Count ...%s" % str(self.insert_count), end="")
            except Exception as e:
                print('pipeline process item', e)
                logging.error("you have an Error in while inserting data:{}".format(e))

