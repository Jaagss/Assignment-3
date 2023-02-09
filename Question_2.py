with open("sorted_data_1.txt") as f:
    a = f.read().splitlines()

l = []
for i in range(1,len(a)):
    m = []
    j = a[i].split(', ')
    m += j
    l.append(m)
l.sort( key = lambda x : x[-1] )

Campus_Entry = {}
for i in l:
    temp_dict = {}
    temp_dict[i[0]] = {}
    Campus_Entry.update(temp_dict)


for i in l:
    for k,v in Campus_Entry.items():
        if i[0]==k:
            temp_list=[]
            temp_dict={
                'Crossing' : i[1],
                'Gate' : i[2],
                'Time' : i[3]
            }
            
            temp_list.extend(v)
            temp_list.append(temp_dict)
            Campus_Entry[i[0]]=(temp_list)


def name_find(Entry):
    name = input("Enter Student Name: ")
    time_input = input("Enter Current Time: ")
    temp_list = []
    with open("output.txt","w") as f:
        f.write(name+'\n')
        for i,j in Entry.items():
            if i == name:
                for k in j:
                    write_list=[('Crossing',k['Crossing']),('Gate',k['Gate']),('Time',k['Time'])]
                    f.write(str(write_list))
                    f.write('\n')
                    if k['Time'] <= time_input:
                        temp_list.append(k['Crossing'])

    if temp_list[-1] == 'ENTER':
        return print('\n' + name + " is in the campus" + '\n')
    else:
        return print('\n' + name + ' is out of the campus' + '\n')
    

def time_find(Entry):
    time = list(map(str,input("Enter start and End time: ").split()))
    temp_list=[]
    for i,j in Entry.items():
        for k in j:
            temp=[]
            if k['Time'] >= time[0] and k['Time'] <= time[1]:
                temp.append(i)
                temp.append(k['Crossing'])
                temp.append(k['Gate'])
                temp.append(k['Time'])
                temp_list.append(temp)
    temp_list.sort(key = lambda x: x[-1])
    with open("output_query_2.txt","w") as f:
        for i in temp_list:
            ans = ''
            for j in i:
                ans += j +', '
            f.write(ans[:-2]+'\n')


def gate_find(Entry):
    gate = input("Enter gate number: ")
    count_entry = 0
    count_exit = 0
    for i,j in Entry.items():
        for k in j:
            if k['Gate'] == gate:
                if k['Crossing'] == 'ENTER':
                    count_entry += 1
                else:
                    count_exit += 1

    return count_entry,count_exit

while True:
    print("1: Give Student Name\n2: Give Start and End Time\n3: Gate number\n")
    l = input("Enter choice: ")
    if l == '1':
        name_find(Campus_Entry)
    elif l == '2':
        time_find(Campus_Entry)
    elif l == '3':
        entry,exit_student = gate_find(Campus_Entry)
        print(entry)
        print(exit_student)
    else:
        break