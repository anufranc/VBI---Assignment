import os
import subprocess
import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser()
parser.add_argument("folder",  help="specify the absolute path to the folder containing the python scripts")
parser.add_argument("-n", "--name" , help="specify the name of file to be excecuted (optional)")
parser.add_argument("-o", "--outfile" , help="specify the output log file (optional)")
parser.add_argument("-r", "--reverse", action="store_true", help="enable reverse order for executing files (optional)")

args = parser.parse_args()
folder_path = args.folder

# if reverse keyword is specified set the variable "reverse" to True else set it to False 
reverse = True if args.reverse else False

# if name keyword is specified save the value to variable "filename" else set it to None 
if args.name is not None:
     file_name = args.name 
else:
     file_name = None

# if outfile keyword is specified save the value to variable "out_log" else set it to None 
if args.outfile is not None:
     out_log = args.outfile
else:
     out_log = None



output = PrettyTable()
output.field_names = ["Folder", "File", "Output"]

# list out all the files in the specified fodler path in order (ascending or decscending) [ ascending ==> reverse = False,    desceneding ==> reverse = True]
#loop through all the files in the folder
for file in sorted(os.listdir(folder_path), reverse= reverse):
    # check if the file is a python file by verifying the file extension
    if file.endswith(".py"):
        # if the user mentions a particluar file name to execute , execute only that python file 
        if file_name: 
            # for each file in folder check if the file name matches the file user specified. 
            if file==file_name:
                # If so execute the python file as a subprocess and break the loop
                proc = subprocess.Popen(['python', folder_path+'/'+file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                # store the output of the executed script to a variable
                response = proc.communicate()[0]
                # Add the output to pretty table
                output.add_row([folder_path, file, response.decode("utf-8") ])
                break
            else:
                # else continue the loop with the next file in the folder
                continue
        else:
            # if user has not mentioned any specific file to execute, execute all the python files in the folder one by one
            proc = subprocess.Popen(['python', folder_path+'/'+file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # store the output of the executed script to a variable
            response = proc.communicate()[0]
            # Add the output to pretty table
            output.add_row([folder_path, file, response.decode("utf-8") ])


# if user has mentioned any specified output log file, write the pretty table content to that file.
if out_log:
    # open the output log file 
    f = open(out_log, "w")
    # write the output 
    f.write(str(output))
    #close the output file
    f.close()
else:
    # else print the output in console itself
    print(output)