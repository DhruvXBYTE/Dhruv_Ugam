# """coding is export tsv form export tsv referen in dowload file export tsv.py
# QA file
# """
#
# from datetime import datetime
# import csv
# import datetime
# import os
# import shutil
# import time
# import re
# import pymysql
# import pandas as pd
# from numpy.ma import count
# from ugam_copple_mx.config import *
# dt = datetime.now()
# # t=t.now()
# # from worlddutyfree_menu.unique_process import
#
#
# # check directory exists or not and make csv file in the bellow directory
# class Export_TSV:
#
#     def __init__(self):
#         try:
#             # Tsv_Output_File_Path = "D:\\Daily Scheduler\\0. UGAM\\0. TSV\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
#             Tsv_Output_File_Path = "D:\\Daily Scheduler\\0. UGAM\\0. TSV\\" + time.strftime('%Y') + "\\" + time.strftime("%m") + "\\" + time.strftime("%d")
#
#             self.Tsv_Output_File_Tsv = Tsv_Output_File_Path
#
#             try:
#                 if not os.path.exists(Tsv_Output_File_Path):
#                     os.makedirs(Tsv_Output_File_Path)
#                 if not os.path.exists(self.Tsv_Output_File_Tsv):
#                     os.makedirs(self.Tsv_Output_File_Tsv)
#
#             except Exception as e:
#                 # logger.error("make dir in constructor method error:{}".format(e))
#                 print('make dir in constructor method error------------',e)
#         except Exception as e:
#             # logger.error("main constructor in export csv class error:{}".format(e))
#             print('main constructor in export csv class error-------------',e)
#
#     # export csv method
#     def export_tsv(self):
#
#         try:
#             conn = pymysql.connect(host=db_host,user=db_user,passwd=db_passwd,database=db_name, use_unicode=True, charset="utf8")
#             cursor = conn.cursor()
#
#             # today_date = dt.strftime('_%d_%m_%y')
#             # linkdata_table_name = db_data_table + today_date
#
#             # select link data table sequence of headers
#             try:
#                 # cursor.execute("Select id from " + data_table)
#                 cursor.execute(f"Select id from {product_data_table} where status='Done'")
#                 rows = cursor.fetchall()
#                 fetch_row_count = int(count(rows))
#                 # print(fetch_row_count)
#                 print('select table :',product_data_table)
#                 select_sql_query = dllobj.export_csv_query()
#
#                 data_frame = pd.read_sql(select_sql_query, conn)
#
#                 # csv_file_date = dt.strftime("%Y-%m-%d")
#                 csv_file_date = dt.strftime("%m%d%y")
#
#                 save_in_dir = self.Tsv_Output_File_Tsv
#                 # 'PDP_crazykangaroo.com_UK&I_output_MMddYY.tsv'
#
#                 # tsv_filename = save_in_dir + f"\\PDP_Coppel.com_mx_output_{csv_file_date}.tsv"
#                 # 'PDP_amazon.co.uk_UK&I_output_091321'
#                 tsv_filename = save_in_dir + f"\\PDP_Coppel.com_mx_output_{csv_file_date}.tsv"
#                 if os.path.exists(tsv_filename):
#                     os.remove(tsv_filename)
#
#                 data_frame.to_csv(tsv_filename, index=False, sep='\t', encoding='utf-8-sig')
#
#
#                 with open(tsv_filename, 'r+',encoding='utf8') as f:
#                     text = f.read()
#                     # text = re.sub('"Availability_preferred_producommon_code_100_site_projectct_""badge"""',
#                     #               'Availability_preferred_product_"badge"', text)
#                     text = re.sub('"Availability_preferred_product_""badge"""',
#                                   'Availability_preferred_product_"badge"', text)
#                     f.seek(0)
#                     f.write(text)
#                     f.truncate()
#                 with open(file=tsv_filename, mode='r', encoding='utf8') as f:
#                     csv_reader = csv.reader(f, delimiter='\t')
#                     data = list(csv_reader)
#                     row_count = len(data)
#                     # print('row_count:', row_count - 1)
#                 if fetch_row_count == row_count - 1:
#                     print("Both Row Checked !")
#                     print("Successfully..... ")
#                 else:
#                     os.remove(tsv_filename)
#                     print('File Recreating...')
#                     Export_TSV.export_tsv(self)
#                 if os.path.exists(tsv_filename):
#                     src = os.path.realpath(tsv_filename)
#                     zip_filename = save_in_dir + f"\\PDP_Coppel.com_mx_output_{csv_file_date}"
#                     zip_filename_2 = save_in_dir + f"\\PDP_Coppel.com_mx_output_{csv_file_date}.zip"
#                     if os.path.exists(zip_filename_2):
#                         os.remove(zip_filename_2)
#                     zip_output_path_tsv, tail = os.path.split(src)
#                     shutil.make_archive(base_name=zip_filename, format='zip',
#                                         root_dir=zip_output_path_tsv, base_dir=tail)
#
#                 from ugam_copple_mx.QA import QA
#                 print("Going for QA....")
#                 QA()
#                 print("Successfully Done............!")
#
#             except Exception as e:
#                 # logger.error('export tsv method link data tabl select error:{}'.format(e))
#                 print('export tsv method link data tabl select error------------',e)
#         except Exception as e:
#             # logger.error("export tsv method sql connection error:{}".format(e))
#             print('export tsv method sql connection error------------',e)
#
# # c = Export_TSV()
# # c.export_tsv()



"""coding is export tsv form export tsv referen in dowload file export tsv.py
QA file
"""
from datetime import datetime
import csv
import datetime
import os
import shutil
import time
import pymysql
import pandas as pd
from numpy.ma import count
from ugam_copple_mx.config import *
# from worlddutyfree_menu.unique_process import

# check directory exists or not and make csv file in the bellow directory
class Export_TSV:
    def __init__(self):
        try:
            self.Tsv_Output_File_Path = "D:\\Daily Scheduler\\0. UGAM\\0. TSV\\" + time.strftime(
                '%Y') + "\\" + time.strftime(
                "%m") + "\\" + time.strftime("%d")
            try:
                if not os.path.exists(self.Tsv_Output_File_Path):
                    os.makedirs(self.Tsv_Output_File_Path)

            except Exception as e:
                logger.error("make dir in constructor method error:{}".format(e))
        except Exception as e:
            logger.error("main constructor in export csv class error:{}".format(e))

    # export csv method
    def export_tsv(self):

        try:
            conn = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_name, use_unicode=True, charset="utf8")
            cursor = conn.cursor()

            today_date = datetime.now().strftime('_%d_%m_%Y')
            # linkdata_table_name = db_data_table + today_date

            # select link data table sequence of headers
            try:
                cursor.execute(f"Select id from {product_data_table} WHERE status='Done' AND product_name<>'' group by Product_URL")
                rows = cursor.fetchall()
                fetch_row_count = int(count(rows))
                # print(fetch_row_count)
                print('select table :',product_data_table)

                cursor.execute(f"UPDATE {product_data_table} SET Product_specifications = REPLACE(Product_specifications,'#||##||#','#||#')")
                conn.commit()
                select_sql_query = dllobj.export_csv_query()

                data_frame = pd.read_sql(select_sql_query, conn)

                csv_file_date = datetime.now().strftime("%Y-%m-%d")

                today_date = datetime.now().strftime("%Y-%m-%d")
                day = today_date.split("-")[2]
                month = today_date.split("-")[1]
                year = today_date.split("-")[0][2:]

                tsv_save_in_dir = self.Tsv_Output_File_Path
                csv_save_in_dir = self.Tsv_Output_File_Path

                tsv_filename = tsv_save_in_dir + f"\\PDP_Coppel.com_LA_output_{month}{day}{year}.tsv"
                csv_filename = csv_save_in_dir + f"\\PDP_Coppel.com_LA_output_{month}{day}{year}.csv"
                if os.path.exists(tsv_filename):
                    os.remove(tsv_filename)
                if os.path.exists(csv_filename):
                    os.remove(csv_filename)

                data_frame.to_csv(tsv_filename, index=False, sep='\t', encoding='utf-8-sig')
                data_frame.to_csv(csv_filename, index=False, encoding='utf-8-sig')

                with open(tsv_filename, 'r+',encoding="utf8") as f:
                    import re
                    text = f.read()
                    text = re.sub('"Availability_preferred_product_""badge"""',
                                  'Availability_preferred_product_"badge"', text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()

                with open(file=tsv_filename, mode='r', encoding='utf8') as f:
                    csv_reader = csv.reader(f, delimiter='\t')
                    data = list(csv_reader)
                    row_count = len(data)
                    # print('row_count:', row_count - 1)
                if fetch_row_count == row_count - 1:
                    print("Both Row Checked !")
                    print("Successfully..... ")
                else:
                    os.remove(tsv_filename)
                    print('File Recreating...')
                    Export_TSV.export_tsv(self)
                if os.path.exists(tsv_filename):
                    src = os.path.realpath(tsv_filename)
                    zip_filename = tsv_save_in_dir + f"\\PDP_Coppel.com_LA_output_{month}{day}{year}"
                    zip_filename_2 = csv_save_in_dir + f"\\PDP_Coppel.com_LA_output_{month}{day}{year}.zip"
                    if os.path.exists(zip_filename_2):
                        os.remove(zip_filename_2)
                    zip_output_path_tsv, tail = os.path.split(src)
                    shutil.make_archive(base_name=zip_filename, format='zip',
                                        root_dir=zip_output_path_tsv, base_dir=tail)
                print("Successfully Done............!")

                #here call QA method and upload exe
                from ugam_copple_mx.QA import QA
                print("Going for QA....")
                QA()

            except Exception as e:
                print(e)
                logger.error('export tsv method link data tabl select error:{}'.format(e))

        except Exception as e:
            logger.error("export tsv method sql connection error:{}".format(e))

# c = Export_TSV()
# c.export_tsv()