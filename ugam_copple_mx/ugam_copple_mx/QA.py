import subprocess
def QA():

    try:
        subprocess.call(["D:\\Ugam_File_Upload_App\\UGAM_Upload_File_APP.exe",
                         r"D:\Dhruv\Ugam\ugam_copple_mx\ugam_copple_mx\config.txt"])
    except Exception as k:
        print("error",k)

# QA()