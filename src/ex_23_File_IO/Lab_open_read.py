
### open
# t = open('testdata.txt', 'r')
# t = open('testdata.txt', 'w')
# t = open('testdata.txt', 'r+')
# t = open('testdata.txt', 'w+')
# t = open('testdata.txt', 'b')
# t.close()

# # Automatically close
# with open('testdata.txt', 'r') as f:
#     data = f.read()
# #
# print(data)


### Open Read
# try:
#     with open('testdata.txt', 'r') as file:
#         content = file.read()
#     # content = file.readlines() # list manner
#         print(content)
# except FileNotFoundError as fnfe:
#     print(fnfe)



### Open append
with open('TestData.txt','a') as file:
    file.write("Hello How are you")


### CSV(comma sepreted file/date)
# import csv
#
# with open('TD.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for col in reader:
#         print(col[0],col[1],sep="|")

### Pandas
# import pandas as pd
#
# df = pd.read_csv("TD.csv")
# print(df)


