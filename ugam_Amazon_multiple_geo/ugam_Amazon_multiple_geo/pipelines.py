# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from ugam_Amazon_multiple_geo.config import *

class UgamAmazonMultipleGeoPipeline:
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
                                                                `category_path` text,
                                                                `estimated_installation_features` text,
                                                                `product_name` text,
                                                                `available_options` text,
                                                                `cookie` text,
                                                                `url` text,
                                                                `regular_price` text,
                                                                `stock_status` text,
                                                                `sku_variant` text,
                                                                `add_to_cart` text,
                                                                `product_image` text,
                                                                `product_id` text,
                                                                `zipcode_site` text,
                                                                `features` text,
                                                                `review_count` text,
                                                                `average_rating` text,
                                                                `parent_url` text,
                                                                `zipcode_input` text,
                                                                `Market_Number` text,
                                                                `Market_Name` text,
                                                                `Store_Number` text,
                                                                `Status` varchar(10) DEFAULT 'Pending',                                                                                         
                                                                 PRIMARY KEY (`Id`),
                                                                 KEY `NewIndex2` (`Id`)
                                                        )"""


            insert_table=f"""INSERT INTO {product_table} (`url`,`uniqueIdentifier`,`zipcode_input`) SELECT `product_url`,`uniqueIdentifier`,`zipcode_input` FROM {db_input_sku_7}"""

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
            self.cursor.execute(f"UPDATE {product_table} SET {update} where Id='{item['Id']}'")
            self.con.commit()

        except Exception as e:
            print(e)
