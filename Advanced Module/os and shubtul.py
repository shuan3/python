import os
os.getcwd()
print(os.listdir('c:\\Users'))


import shutil
shutil.move('practice.txt','C:\\Users\\Marcial')



#delete file
import send2trash

send2trash.send2trash('practice.txt')







for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    