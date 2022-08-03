# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from ugam_amazon_geo.config import *


class UgamAmazonGeoPipeline:

    try:
        print('hello')
        con = pymysql.connect(host=db_host, user=db_user, password=db_passwd)
        db_cursor = con.cursor()
        create_db = f"create database if not exists `{db_name}` CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
        db_cursor.execute(create_db)
        con = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name, autocommit=False,
                              use_unicode=True, charset="utf8")
        cursor = con.cursor()
        print(cursor)
        # create branch table
        try:
            product_create = f"CREATE TABLE " + product_table + """(
                                                                `Id` INT(10) NOT NULL AUTO_INCREMENT,
                                                                `htmlpath` text,
                                                                `uniqueIdentifier` text,
                                                                `extraction_date` text,
                                                                `category_path` text,
                                                                `Product_image` text,
                                                                `Product_Name` text,
                                                                `Markdown_Price` text,
                                                                `regular_price` text,
                                                                `url` text,  
                                                                `product_id` text,
                                                                `Manufacturer_Part_Number` text,
                                                                `Brand_Name` text,
                                                                `Color_Finish` text,
                                                                `Capacity` text,
                                                                `Installation_type` text,
                                                                `Detailed_Specification` text,
                                                                `zipcode_site` text,
                                                                `Product_Description` text,
                                                                `zipcode_input` text,
                                                                `Status` varchar(10) DEFAULT 'Pending',                                                                                         
                                                                 PRIMARY KEY (`Id`),
                                                                 KEY `NewIndex2` (`Id`)
                                                        )"""

            # insert_table=f"""INSERT INTO {product_table} (`url`,`uniqueIdentifier`,`zipcode_input`) SELECT `product_url`,`uniqueIdentifier`,`zipcode` FROM {db_input_sku}"""
            # print(product_create)

            try:
                data_post_code = f"select zipcode from cookies"
                cursor.execute(data_post_code)
                core_list = [column for column in cursor.fetchall()]
                for i in core_list:
                    post_code = i[0]

                    data_url = f"select `url`,`uniqueIdentifier` from {db_input_sku}"
                    cursor.execute(data_url)
                    core_list_url = [column for column in cursor.fetchall()]
                    for j in core_list_url:
                        url = j[0]
                        uniqueIdentifier=j[1]
                        # print(post_code)
                        # print(url)

                        """Inset Url and up to zip code"""
                        insert_query = f"""insert into {product_table} (`url`,`uniqueIdentifier`,`zipcode_input`) values ("{url}","{uniqueIdentifier}","{post_code}")"""
                        print(insert_query)
                        cursor.execute(insert_query)
                        con.commit()

                    print(core_list)

            except Exception as e:
                print(e)

            print(product_create)
            cursor.execute(product_create)
            # cursor.execute(insert_table)
            con.commit()
        except Exception as e:
            print(e)
            print(" TABLE ALREADY CREATED! ")



        # cursor.execute(insert_table)
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
            self.cursor.execute(f"UPDATE {product_table} SET {update} where Id='{item['Id']}'")
            self.con.commit()

        except Exception as e:
            print(e)

        # try:
        #     field = []
        #     value = []
        #     for key in item:
        #         field.append(f"{str(key)}")
        #         value.append(f"{str(item[key])}")
        #     update = ','.join([key + " = " + f"'{value}'" for key, value in zip(field[1:], value[1:])])
        #     # print("data print:", item[key])
        #     print(update)
        #     self.cursor.execute(f"UPDATE {product_table} SET {update} where Id='{item['Id']}'")
        #     self.con.commit()
        #
        # except Exception as e:
        #     print(e)
# d=UgamAmazonGeoPipeline()