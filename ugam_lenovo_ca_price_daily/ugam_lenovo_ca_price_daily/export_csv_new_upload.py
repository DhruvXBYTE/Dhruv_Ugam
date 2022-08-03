"""coding is export tsv form export tsv referen in dowload file export tsv.py
QA file
"""
from datetime import datetime
import csv
from ugam_lenovo_ca_price_daily.pipelines import UgamLenovoCaPriceDailyPipeline
import datetime
import os
import shutil
import time
import pymysql
import re
import pandas as pd
from numpy.ma import count
from ugam_lenovo_ca_price_daily.config import *
# from common_code_100_site_project import ugam_3_Category_PDP
# from worlddutyfree_menu.unique_process import

# check directory exists or not and make csv file in the bellow directory
class Export_Csv:
    def __init__(self):
        try:
            """--localpath--"""
            Csv_local_Output_File_Path = "D:\\Daily Scheduler\\0. UGAM\\0. CSV\\CATEGORY_DAILY\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
            self.Csv_local_Output_File_Path = Csv_local_Output_File_Path + "\\CSV"

            """--uploadpath--"""
            Csv_upload_Output_File_Path = "\\\\192.168.1.120\\d\\Ugam-Project\\UGAM-Daily_Price\\CA\\Output\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
            # Csv_upload_Output_File_Path = "\\\\192.168.1.120\\d\\Ugam-Project\\UGAM-Daily_Price\\India Output\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
            # Csv_upload_Output_File_Path = "\\\\192.168.1.129\\d\\Ugam-Project\\UGAM-Daily_Price\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
            self.Csv_upload_Output_File_Path = Csv_upload_Output_File_Path + "\\Delivered Data"

            try:
                """--local_directory--"""
                if not os.path.exists(Csv_local_Output_File_Path):
                    os.makedirs(Csv_local_Output_File_Path)
                if not os.path.exists(self.Csv_local_Output_File_Path):
                    os.makedirs(self.Csv_local_Output_File_Path)

                """--upload_directory--"""
                if not os.path.exists(Csv_upload_Output_File_Path):
                    os.makedirs(Csv_upload_Output_File_Path)
                if not os.path.exists(self.Csv_upload_Output_File_Path):
                    os.makedirs(self.Csv_upload_Output_File_Path)

            except Exception as e:
                logger.error("make dir in constructor method error:{}".format(e))
        except Exception as e:
            logger.error("main constructor in export csv class error:{}".format(e))

    """ ---export csv method--- """
    def export_csv(self):
        try:
            conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, use_unicode=True, charset="utf8")
            cursor = conn.cursor()

            today_date = datetime.now().strftime('_%d_%m_%Y')

            # select link data table sequence of headers
            try:
                cursor.execute(f"""select id from {db_data_table} where Status!='Pending'""")
                rows = cursor.fetchall()
                print(len(rows))
                fetch_row_count = int(count(rows))
                # print(fetch_row_count)
                print('select table :', db_data_table)

                select_sql_query = catpdp.export_csv_query()
                # print(select_sql_query)
                # select_sql_query = f"""-- SELECT `Date of Crawl`,`Retailer`,`Product ID`,`Product Title`,`Product URL`,`List Price`,`Markdown Price`,`Seller Name`,`Stock Status`,`Lead time` FROM {db_data_table} where Status<>'Pending'"""

                # cursor.execute(select_sql_query)
                # conn.commit()
                # print(select_sql_query)

                data_frame = pd.read_sql(select_sql_query, conn)
                # data_frame=data_frame.astype(str)

                # csv_file_date = datetime.now().strftime("%Y-%m-%d")

                # csv_file_date = datetime.now().strftime("%m%d%Y")
                csv_file_date = datetime.now().strftime("%d%m%y")

                """-------creating csv in local path-------"""
                save_in_local_dir = self.Csv_local_Output_File_Path
                save_in_upload_dir = self.Csv_upload_Output_File_Path

                csv_filename_local = save_in_local_dir + f"\\Lenovo_{csv_file_date}.csv"
                csv_filename_local_new = save_in_local_dir + f"\\PDP_lenovo_CA_output_{csv_file_date}.csv"
                csv_filename_upload_new = save_in_upload_dir + f"\\PDP_lenovo_CA_output_{csv_file_date}.csv"


                if os.path.exists(csv_filename_local):
                    os.remove(csv_filename_local)
                if os.path.exists(csv_filename_local_new):
                    os.remove(csv_filename_local_new)

                # todo: "," in csv-------------------********-----------------------

                df3 = pd.DataFrame()

                df2 = data_frame
                allcolumns = df2.columns.values.tolist()

                for column in allcolumns:
                    # print(column)
                    # df3[column] = '"' + df2[column].astype(str) + '"'
                    df3[column] = '"' + df2[column].astype(str) + '"'

                df3.to_csv(csv_filename_local, index=False, encoding='utf-8-sig')

                text = open(csv_filename_local, "r", encoding='utf-8')
                with open(csv_filename_local_new, 'w', encoding='utf-8') as f1:
                    for i in text:
                        # print(i.replace('"""', '"'))
                        f1.write(i.replace('"""', '"'))
                text.close()

                # todo: "," in csv------------------------------------------

                # data_frame.to_csv(csv_filename_local, index=False, encoding='utf-8-sig')

                with open(file=csv_filename_local, mode='r', encoding='utf8') as f:
                    csv_reader = csv.reader(f, delimiter=",")
                    data = list(csv_reader)
                    row_count = len(data)

                if fetch_row_count == row_count - 1:
                    if os.path.exists(csv_filename_upload_new):
                        os.remove(csv_filename_upload_new)

                    shutil.copy(csv_filename_local_new,csv_filename_upload_new)
                    print("Both Row Checked !")
                    print("Successfully..... ")
                else:
                    os.remove(csv_filename_local)
                    print('File Recreating...')
                    Export_Csv.export_csv(self)

                print("Successfully Done............!")
                # print("Going for QA............!")
                # print("QA Done............!")

            except Exception as e:
                logger.error('export csv method link data table select error:{}'.format(e))

        except Exception as e:
            logger.error("export csv method sql connection error:{}".format(e))

c = Export_Csv()
c.export_csv()
