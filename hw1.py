# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108060034.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

target_data = list(filter(lambda item: item['PRES'] == '-99.000', data))
for i in range(len(target_data)):
    target_data[i]['station_id'] = 'None'

target_data = list(filter(lambda item: item['PRES'] == '-999.000', data))
for i in range(len(target_data)):
    target_data[i]['station_id'] = 'None'

target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
sumCOA880 = 0.000
for i in range(len(target_data)):
    #print(i, " ", target_data[i]['PRES'], "\n")
    sumCOA880 = sumCOA880 + float(target_data[i]['PRES'])
meanCOA880 = sumCOA880 / len(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
sumC0F9A0 = 0.000
for i in range(len(target_data)):
    #print(i, " ", target_data[i]['PRES'], "\n")
    sumC0F9A0 = sumC0F9A0 + float(target_data[i]['PRES'])
meanC0F9A0 = sumC0F9A0 / len(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
sumC0G640 = 0.000
for i in range(len(target_data)):
    #print(i, " ", target_data[i]['PRES'], "\n")
    sumC0G640 = sumC0G640 + float(target_data[i]['PRES'])
meanC0G640 = sumC0G640 / len(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
sumC0R190 = 0.000
for i in range(len(target_data)):
    #print(i, " ", target_data[i]['PRES'], "\n")
    sumC0R190 = sumC0R190 + float(target_data[i]['PRES'])
meanC0R190 = sumC0R190 / len(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
sumC0X260 = 0.000
for i in range(len(target_data)):
    #print(i, " ", target_data[i]['PRES'], "\n")
    sumC0X260 = sumC0X260 + float(target_data[i]['PRES'])
meanC0X260 = sumC0X260 / len(target_data)

print("[['C0A880', ", '%.1f'%meanCOA880, "], ['C0F9A0', ", '%.1f'%meanC0F9A0, "], ['C0G640', ", '%.1f'%meanC0G640, "], ['C0R190', ", '%.1f'%meanC0R190, "], ['C0X260', ", '%.1f'%meanC0X260, "]]")

# Retrive ten data points from the beginning.
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
#print(target_data[0]['PRES'])
#========================================
