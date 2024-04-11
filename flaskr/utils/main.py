import pandas as pd 
import matplotlib.pyplot as plt
import os


## Points block - goes inside a loop
point_a = 0 # iteration for each in CSV  
point_b = 0 # point_a[i+1] 
delta = point_b - point_a

## const block
const_mc = 0
const_mic = 0
const_mcc = const_mc + const_mic # In this case 0 < mcc > 110

## events block
event = 0 
event_time = 0
event_peak = 0

# DB query block
coincidence = 0
item_average = 0 # For each item [i]

## Read CSV block
file = open('../flaskr/static/consumo_casa.csv')
fileLines = file.readlines()


def values_items():
    item_values = []

    for i in range(3,11):
        item_values.append([]) #Items name
        for j in range(1,len(fileLines)): # Each Value
            clearLine = fileLines[j].strip()
            data = clearLine.split(",")
            
            if (j < 194124):
                if(float(data[i]) > 30):
                    item_values[i-3].append(float(data[i]))
    return item_values

def average_items(item_values):
    item_values_average = []
    for i in range(8):
        if (len(item_values[i]) != 0):
            item_values_average.append(round(sum(item_values[i])/len(item_values[i])))
    print(item_values_average)
    return item_values_average

def find_coincidence(delta_total, items_values_average):
    shortest_values = []
    for i in items_values_average:
         value = round(delta_total-i)
         shortest_values.append(value)
    return shortest_values


i=1
const_mcc = 110
event_time = 0
event_device = 0
event_time_sec = 0
event_device_sec = 0
values_usage = {}
time = 194214

## Print CSV data 
items_values =  values_items()
items_values_average = average_items(items_values)


while(i<len(fileLines)):
    clearLine = fileLines[i].strip()
    data = clearLine.split(",")
    #if (i < 10):
        #print(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    
    if( i + 1 < len(fileLines)):
        clearLineB = fileLines[i+1].strip()
        dataB = clearLineB.split(",")
        point_a = float(data[2])
        #point_b = float(dataB[2])  ###
        #delta = point_b - point_a ###
        #point_average = (point_a + point_b)/2 ###
        #delta_total = point_average - const_mcc # esta medianamente malo
        delta_total = point_a - const_mcc
    if (i > 0 and i < time):
        print("----------------------")
        print(items_values_average)
        print("Contador= ", i)
        print("A= ", point_a)
        #print("B= ", point_b)
        #print("Delta= ", delta)
        print("Delta Total= ", delta_total)
        ##Variable de tiempo
        
        ## coincidence
        if (delta_total > 39):
            shortest_values = find_coincidence(delta_total,items_values_average )
            print("Shortest:",shortest_values)
            if any(x > 0 for x in shortest_values):
                coincidence = min([x for x in shortest_values if x > 0])
                indice = shortest_values.index(coincidence)
                #print("Indice:",indice)
                print("Coincidence:",coincidence)
                device = fileLines[0].strip().split(',')[indice+3]
                print("Device:",device)
                if (event_device != 0 and event_device == device):
                    event_time = event_time + 1
                else:
                    print("The previous event lasts:", event_time, " minutes")
                    event_device =  device
                    event_time = 0 
                while (coincidence > 40):
                    event_time_sec = 0
                    print("Coincidence:",coincidence)
                    shortest_values = find_coincidence(coincidence,items_values_average )
                    coincidence = min([x for x in shortest_values if x > 0])
                    indice = shortest_values.index(coincidence)
                    device_sec = fileLines[0].strip().split(',')[indice+3]
                    print("Aditional Device:", device_sec)
                    event_time_sec = event_time_sec + 1
                    if (device_sec in values_usage):
                        values_usage[device_sec].append(event_time_sec)
                        print("An aditional event has been added")
                    else:
                        values_usage[device_sec] = [event_time_sec]
                        print("An aditional event has been added") 
            else:
                print("Hola")
                print("The previous event lasts:", event_time, " minutes")
                print("There is not event")
        ##variable de tiempo ++

    if (i > 0 and i < time and delta_total > 30):
        print("This event lasts:", event_time, " minutes")
        print("There's event")
    elif(i > 0 and i < time and delta_total < 30):
        if(event_time > 0):
            if (device in values_usage):
                values_usage[device].append(event_time)
            else:
                values_usage[device] = [event_time]
            print("This event lasts:", event_time, " minutes")
            event_time = 0
        print("There is not event")  

    i=i+1


print("----------------------")


values_usage_sum = {}
values_usage_kw = {}
values_usage_cost = {}

for i in values_usage:
    values_usage_sum[i] = sum(values_usage[i])
print("Dictionary:", values_usage)

for i in values_usage:
    device = fileLines[0].strip().split(',').index(i)
    device_value = items_values_average[device-3]
    values_usage_kw[i] = (values_usage_sum[i]*device_value)/1000
print("Dictionary:", values_usage)

cost_average = (787.76 / 60)

for i in values_usage:
    #values_usage_cost[i] = f"${round(values_usage[i] * (cost_average))} COP"
    values_usage_cost[i] = round(values_usage_kw[i] * (cost_average))
print("Dictionary:", values_usage)

devices = fileLines[0].strip().split(',')
devices = devices[3:]
print("Devices=", devices)

time = round(time / 1440)

def graphics():
    

    Data = pd.read_csv("../flaskr/static/consumo_casa.csv", usecols=['Fecha', 'Refrigerator', 'Clothes washer',
                                                    'Clothes Iron', 'Computer', 'Oven', 'Play', 'TV', 'Sound system'])

    Data['G. Electrodomésticos'] = Data['Refrigerator'] + Data['Oven'].sum()
    Data['P. Electrodomésticos'] = Data['Clothes washer'] + Data['Clothes Iron'].sum()
    Data['Equipos de Informatica'] = Data['Play'] + Data['TV'] + Data['Sound system'].sum()

    total_consumo = Data[['G. Electrodomésticos', 'P. Electrodomésticos', 'Equipos de Informatica']].sum().sum()

    consumo_por_dispositivo = Data[['G. Electrodomésticos', 'P. Electrodomésticos', 'Equipos de Informatica']].sum()


    etiquetas = consumo_por_dispositivo.index

    valores = consumo_por_dispositivo.values
    colores = ['#D5752D', '#FFF549', '#54585A', '#0E3BAF', '#2BBF8E', '#D30042', '#279FE5', '#C19FE5']
                #REFRI     #CLOS W    #CL IRON   #COMPU     #OVEN      #PLAY      #TV        #SOND SYSTEM
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140,colors=colores)

    plt.title('Proporción del consumo total de energía Agrupados')

    filename = '../flaskr/static/img/graph'
    plt.savefig(filename)
    plt.close()
    filename = filename+".png"
    print(filename)
    return filename