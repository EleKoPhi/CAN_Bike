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

with open('/Users/philippmochti/src/CANBike/LogFiles/enviolo_pressent.csv') as can_log:
    log_reader = csv.reader(can_log, delimiter=',')
    for sample in log_reader:
        if sample[index.can_type] == id_key:
            data_bytes = []
            error_Flag = False
            msg_id = hex(int(sample[index.id],0))
            next_sample = next(log_reader)
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
                
            
            
            if not error_Flag:   
                if msg_id in id_counter.keys():
                    id_counter[msg_id] = id_counter[msg_id] + 1
                else:
                    id_counter[msg_id] = 1
                    
                pressent_ids.add(msg_id)
                
cyclic_ids = []
for id in id_counter.keys():
    if id_counter[id] > 10:
        cyclic_ids.append(id)
print(sorted(cyclic_ids))
#print(sorted(pressent_ids))
