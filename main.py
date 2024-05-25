import csv

id_key = 'identifier_field'
control_key = 'control_field'
data_key = 'data_field'

class index():
    com_type = 0
    can_type = 1
    timee_stamp = 2
    duration = 3
    id = 4
    data_length = 5
    data = 6
    d2 = 5
    d3 = 6
    d4 = 7
    d5 = 8
    d6 = 9
    d7 = 10
    d8 = 11 
    
data_bytes = []
error_Flag = False

pressent_ids = set({})

id_counter = {}


signals:dict[str, list] = {}

startTimeSamp = None


from canDBC import bosch_dbc
import datetime

import matplotlib

import numpy as nm
import pandas as pd

with open('/Users/philippmochti/src/CANBike/LogFiles/enviolo_pressent.csv') as can_log:
    log_reader = csv.reader(can_log, delimiter=',')
    next(log_reader)
    for sample in log_reader:
        if startTimeSamp == None:
            s = sample[index.timee_stamp].split("+")[0][:-3]
            startTimeSamp = datetime.datetime.fromisoformat(s)
        if sample[index.can_type] == id_key:
            msg_id = hex(int(sample[index.id],0))
            sampleTime = sample[index.timee_stamp]
            next_sample = next(log_reader)
            data_bytes = []
            error_Flag = False
            if next_sample[index.can_type] == control_key:
                dlc = int(next_sample[index.data_length],0)
                if dlc == 0 or dlc == None:
                    error_Flag = True
                for element in range(dlc):
                    next_sample = next(log_reader)
                    if next_sample[index.can_type] != data_key:
                        error_Flag = True
                        break
                    else:
                        data_bytes.append(next_sample[index.data])
            else:
                error_Flag = True
                
            if error_Flag: continue
            
            if msg_id in bosch_dbc.dbc_pdus.keys():
                #print("Decoding PDU: " + str(bosch_dbc.dbc_pdus[msg_id]))
                for i, signal in enumerate(bosch_dbc.dbc_pdus[msg_id].signals):
                    #print(f"{i+1}. Signal: {signal.name}")
                    startbyte = signal.startPosition
                    endbyte = signal.endPosition
                    signal_byte = data_bytes[startbyte:endbyte+1]
                    
                    if signal.converionTable is not None:
                        #Only use first byte - We ensure enums are only 0 to 255

                        value = signal.converionTable[signal_byte[0]]
                        
                    else: 
                        value = 0 # Todo numerical values
                        
                    if signal.name not in signals.keys():
                        signals[signal.name] = list()
                        
                    s = sampleTime.split("+")[0][:-3]  
                    convertedSampleTime = datetime.datetime.fromisoformat(s)
                    time_since_start = (convertedSampleTime-startTimeSamp).total_seconds()
                    signals[signal.name].append([time_since_start, value])


import matplotlib.pyplot as plt
import numpy as np


print(signals.keys())
# Data for plotting
s = []
t = []
for sample in signals["Status light button"]:
    t.append(sample[0])
    s.append(sample[1])


fig, ax = plt.subplots()
ax.plot(t, s)
plt.show()


#print(signals)       
            #if msg_id in id_counter.keys():
            #    id_counter[msg_id] = id_counter[msg_id] + 1
            #else:
            #    id_counter[msg_id] = 1
            #        
            #    pressent_ids.add(msg_id)
            #    
            #if msg_id == '0x3b':
            #    print(data_bytes)
                
#cyclic_ids = []
#for id in id_counter.keys():
#    if id_counter[id] > 10:
#       cyclic_ids.append(id)
#print(sorted(cyclic_ids))
#print(sorted(pressent_ids))
