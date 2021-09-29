#import module
import os
import datetime as dt

# Defining the function to iterate through a directory to search for a specific string
def find_stuff(absolute_path, search_for_error):
    today = dt.datetime.today().date()
    for file_name in os.listdir(absolute_path):
        filetime = dt.datetime.fromtimestamp(os.path.getctime(absolute_path + file_name))
        # File type filtered to text file extension
        if file_name.endswith('.txt') and filetime.date() == today:
            # Open file for reading
            open_file = open(absolute_path + file_name)
            # Read the first line from the file
            line = open_file.readline()
            # Initialize counter for line number
            line_no = 1
            # Loop until EOF
            while line != '' :
                    # Search for string in line
                    index = line.find(search_for_error)
                    if ( index != -1) :
                        print("File name: " + file_name, "\nError found on line: ", line_no, ",", index, "\n", line, sep="")
                    # Read next line
                    line = open_file.readline()  
                    # Increment line counter
                    line_no += 1
            # Close the files
            open_file.close()

print(find_stuff(absolute_path=r'D:\\test\\Reporting\\CFCPM_errors\\', search_for_error='ERROR - Error occurred in CFC: 3 (Directory or file does not exist)'))