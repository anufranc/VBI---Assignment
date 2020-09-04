
import os
from prettytable import PrettyTable
********

folder_path = input("Please input the folder path to the scripts : ")
if folder_path is None:
    print("Folder path can't be empty. Script terminated")
    exit()

file_name = input("Specify a filename to execute: (Leave blank to execute all files)")

out_log = input("Specify an output log file: (Leave blank to print output in console)")

run_reverse = input("Execute scripts in reverse order (y|n) : ")
if run_reverse=='y':
    reverse_flag = True
elif run_reverse=='n':
    reverse_flag = False
else:
    print("Invalid input. Continuing with defaults")
    reverse_flag=False

output = PrettyTable()
# specify the column headers for output (output as table format)
output.field_names = ["Folder", "File", "Output"]


# list out all the files in the specified fodler path in order (ascending or decscending) [ ascending ==> reverse = False,    desceneding ==> reverse = True]
#loop through all the files in the folder
for file in sorted(os.listdir(folder_path), reverse=reverse_flag):
    # check if the file is a python file by verifying the file extension
    if file.endswith(".py"):
        # if the user mentions a particluar file name to execute , execute only that python file 
        if file_name: 
            # for each file in folder check if the file name matches the file user specified. 
            if file==file_name:
                # If so execute the python file as a subprocess and break the loop and then store the output to a variable otherwise continoue the loop with the next file in the folder
             break
