import os
import datetime

# count = 0
location = r'D:\test\Reporting\CFCPM_errors'
searchfile = open("D:\\test\\Reporting\\CFCPM_errors\\5951785.txt", "r")
# for line in searchfile:
#     if 'ERROR - Error occurred while uploading core file out package' in line:
#         count +=1 
#         print("------------------------")
#         print(f"Reported error: {line}")
#         print("------------------------")
#         print(f"Occurances: {count}.")
#         print("------------------------")
#         print()
#         print("End.")
# searchfile.close()

today = datetime.date()

count = 0
for file in os.listdir(location):
    if file.endswith('.txt') and file.startswith(today):
        print("here")







    #     searchfile = open(f"D:\\test\\Reporting\\CFCPM_errors\\{file}", "r")
    #     for line in searchfile:
    #         count += 1
    #         if 'ERROR - Error occurred while uploading core file out package' in searchfile:
    #             count +=1
    #             print(count)
    #             print("------------------------")
    #             print(f"Reported error: {line}")
    #             print(searchfile)
    #             #print(count)
    #     #         # print("------------------------")
    #             print(f"Occurances: {count}.")
    #             # print("------------------------")
    #             # print()
    #             # print("End.")
    #         # searchfile.close()