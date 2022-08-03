# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from ugam_Amazon_QA.config import *
import pymysql
import time

class UgamAmazonQaPipeline:

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
            question = f"CREATE TABLE " + quetion + """(
                                                                `Id` INT(10) NOT NULL AUTO_INCREMENT,
                                                                `ID1` text,
                                                                `created_time` text,
                                                                `master_ASIN` text,
                                                                `vote` text,
                                                                `ask_before_days` text,
                                                                `question` text,
                                                                `question_ID` text,
                                                                `question_date` text,  
                                                                `question_url` text,
                                                                `answer_available` text,
                                                                `htmlpath_all_Que` text,
                                                                `htmlpath_particular_Que` text,
                                                                `Product_url` text,
                                                                `Status` text,                                                                               
                                                                 PRIMARY KEY (`Id`),
                                                                 KEY `NewIndex2` (`Id`)
                                                        )"""
            print(question)
            cursor.execute(question)

            answer = f"CREATE TABLE " + answer + """(
                                                                            `Id` INT(10) NOT NULL AUTO_INCREMENT,
                                                                            `ID1` text,
                                                                            `created_time` text,
                                                                            `master_ASIN` text,
                                                                            `answer` text,
                                                                            `answer_id` text,
                                                                            `answer_date` text,
                                                                            `answer_by` text,
                                                                            `author` text,  
                                                                            `question_id` text,
                                                                            `question_url` text,
                                                                            `htmlpath_all_Que` text,
                                                                            `htmlpath_particular_Que` text,
                                                                            `Status` text,                                                                               
                                                                             PRIMARY KEY (`Id`),
                                                                             KEY `NewIndex2` (`Id`)
                                                                    )"""
            # print(product_create)
            cursor.execute(answer)
            con.commit()
        except Exception as e:
            print(e)
            print(" TABLE ALREADY CREATED! ")
    except Exception as e:
        print()

    def process_item(self, item, spider):
        return item

    # def store_db(self, item):
    #
    #     if isinstance(item, questions):
    #
    #         try:
    #             field_list = []
    #             value_list = []
    #             for field in item:
    #                 field_list.append(f'`{str(field)}`')
    #                 value_list.append(str(item[field]).replace("'", "’"))
    #             fields = ','.join(field_list)
    #             values = "','".join(value_list)
    #             insert_db = "insert into " + quetion + "( " + fields + " ) values ( '" + values + "' )"
    #             print(insert_db)
    #             self.cursor.execute(insert_db)
    #             self.con.commit()
    #             print("Data inserted", item['Rank'])
    #
    #         except Exception as e:
    #             print('pipeline process item', e)
    #             logging.error("you have an Error in while inserting data:{}".format(e))
    #
    #     elif isinstance(item, answers):
    #
    #         try:
    #             field_list = []
    #             value_list = []
    #             for field in item:
    #                 field_list.append(f'`{str(field)}`')
    #                 value_list.append(str(item[field]).replace("'", "’"))
    #             fields = ','.join(field_list)
    #             values = "','".join(value_list)
    #             insert_db = "insert into " + answer + "( " + fields + " ) values ( '" + values + "' )"
    #             print(insert_db)
    #             self.cursor.execute(insert_db)
    #             self.con.commit()
    #             print("Data inserted", item['Rank'])
    #
    #         except Exception as e:
    #             print('pipeline process item', e)
    #             logging.error("you have an Error in while inserting data:{}".format(e))
