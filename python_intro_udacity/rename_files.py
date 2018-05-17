import os
def rename_file():
    file_list = os.listdir(r"C:\Users\Alex\Projetos\Introdução ao Python - Udacity\files_secrete_message\prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Alex\Projetos\Introdução ao Python - Udacity\files_secrete_message\prank")
    for file_name in file_list:
        print("old file name: " + file_name)
        print("new file name: " + file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)                  
        
rename_file()    
    
