# 19.0424 to 19.0412
# 73.0246 to 73.0259

# 0.002/ 0.005

import pandas as pd
# import lxml

data = open("wifi_data.txt", 'r')

wife_data = data.read()


listu = wife_data.split("\n")


for entry in range(len(listu)):
    listu[entry] = listu[entry].split("\t")


df = pd.DataFrame(listu[1:], columns=listu[0][:-1])
df.to_csv("C:/Hamza/Hacking Stuff/College Wifi/wife_data.csv", index=False)