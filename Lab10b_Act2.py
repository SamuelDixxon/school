# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Samuel Dixon
# Section:      530
# Assignment:   Lab10b_Act2
# Date:         10 8 2019
import matplotlib.pyplot as plt
Max_templist = [] 
Min_templist = [] 
Average_precipitation = [] 
Humidity_avg = [] 
Average_precip = [] 
Average_dew = []
Average_temp = []
Average_pressure = []
Month_date = []
Dates = []


Months_Avg=[[], [], [], [], [], [], [], [], [], [], [], []]
Months_Low=[[], [], [], [], [], [], [], [], [], [], [], []]
Months_Max=[[], [], [], [], [], [], [], [], [], [], [], []]

with open("WeatherDataWindows.csv",'r') as weatherdata:
    read_data = weatherdata . readline()
    for Eachline in weatherdata:
        LineParts = Eachline.strip('\n').split(',')
        Dates.append(LineParts[0])
        Max_templist.append(float(LineParts[1]))
        Min_templist.append(float(LineParts[3]))
        Average_precipitation.append(float(LineParts[13]))
        Humidity_avg.append(float(LineParts[8]))
        Average_pressure.append(float(LineParts[11]))
        Average_dew.append(float(LineParts[5]))
        Average_temp.append(float(LineParts[2]))
        Date = (LineParts[0].split('/'))
        Month_date.append(Date[0])


for day in range(len(Month_date)):
    Months_Avg[int(Month_date[day])-1].append(Average_temp[day])
    
for day in range(len(Month_date)):
    Months_Low[int(Month_date[day])-1].append(Min_templist[day])
    
for day in range(len(Month_date)):
    Months_Max[int(Month_date[day])-1].append(Max_templist[day])


plt.figure(1)
color = 'tab:red'
plt.xlabel('Date')
plt.ylabel('Average Pressure', color=color)
plt.plot(Dates, Average_pressure, color=color)
plt.tick_params(axis='x', labelcolor=color)

plt.xticks(Dates[0 : len(Dates) : 160], color="g", rotation=70)



plt2 = plt.twinx()

color = 'tab:blue'
plt.ylabel('Average temp', color=color)
plt.plot(Dates, Average_temp, color=color)
plt.tick_params(axis='y', labelcolor=color)
plt.title("Average Temperature and Average Pressure for Bryan College Station 2015-2017")

plt.xticks(Dates[0 : len(Dates) : 160], color='g')


plt.show()

#b
plt.figure(2)
plt.title("Histogram of Average Precipitation in Bryan/College Station")
plt.hist(Average_precipitation, bins = 16)
plt.show()

#c
plt.figure(3)
plt.title("Average Temperature vs. Average Dew in Bryan/College Station")
color = 'tab:red'
plt.xlabel('Average Dew', color='tab:blue')
plt.ylabel('Average Temperature', color=color)
plt.scatter(Average_dew, Average_temp, color=color, alpha=0.5)
plt.show()

#d

plt.figure(4)
Total_avgs = []
Min_for_months = []
Max_for_months = []
Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Oct','Sep','Nov','Dec']
i = 0
num_total = 0 
while i != 12 :
    for num in Months_Avg[i]:
        num_total += num
    avgm = num_total / len(Months_Avg[i])
    num_total = 0
    Total_avgs.append(avgm)
    i+=1

for i in range(0, 12):   
    plt.bar(Months[i], Total_avgs[i],color=(0.1,0.5,0.9,0.2))
    plt.errorbar(Months[i],(Months_Low[i],Months_Max[i]),color='b')
plt.title("Temperature Data in Bryan/College Station")
plt.ylabel("Temperature degrees C")






