import time

# processes = [2,20, 3, 54,40, 7]
# vorud=[0,7,5,10,11,2]
processes =[]
vorud=[]
print("Teda process ha ra vared konid :")
for i in range(int(input())):
    processes.append(int(input("service time process: ")))
    vorud.append(int(input("zamane vorud process: ")))
processes = [x for _, x in sorted(zip(vorud, processes))]
vorud = sorted(vorud)

def RR(processes, vorud):
    RQ1 = []
    for i in processes:
        time.sleep(2)
        if i - 2 > 0:
            RQ1.append(i - 2)
        else:
            vorud.remove(vorud[processes.index(i)])
    print("RR")
    print("RQ1: ", RQ1)
    return RQ1


#print(RR(processes))

def FCFS(processes, vorud):
    RQ1 = RR(processes, vorud)
    RQ2 = []
    for i in RQ1:
        time.sleep(4)
        if i - 4 > 0:
            RQ2.append(i - 4)
        else:
            vorud.remove(vorud[RQ1.index(i)])
            #RQ1.remove(i)
            #RQ1=filter(i, RQ1.remove)
            #i + 1 =
    print("FCFS")
    print("RQ2: ",RQ2)
    return RQ2


#print(FCFS(processes))

def SPN(processes,vorud):
    RQ2 = FCFS(processes,vorud)
    #RQ2 = SRN(processes,vorud)
    RQ3 = []
    new_vorud=[]
    for i in RQ2:
        if RQ2.index(i) != 0 and vorud[RQ2.index(i)-1] + 8 <= vorud[RQ2.index(i)]:
          time.sleep(8)
          if i - 8 > 0:
            RQ3.append(i - 8)
            new_vorud.append(vorud[RQ2.index(i)])
        else:
            if RQ2.index(i) != 0:
               time.sleep(vorud[RQ2.index(i)-1] + 8 - vorud[RQ2.index(i)])
            if i - 8 > 0:
                RQ3.append(i - 8)
                new_vorud.append(vorud[RQ2.index(i)])
    print("SPN1")
    print("RQ3: ", RQ3)
    return RQ3, new_vorud

def SPN2(RQ3, vorud):
    RQ4 = []
    new_vorud = []
    for i in RQ3:
        if RQ3.index(i) != 0 and vorud[RQ3.index(i) - 1] + 16 <= vorud[RQ3.index(i)]:
            time.sleep(16)
            if i - 16 > 0:
                RQ4.append(i - 16)
                new_vorud.append(vorud[RQ3.index(i)])
        else:
            if RQ3.index(i) != 0:
                time.sleep(vorud[RQ3.index(i) - 1] + 16 - vorud[RQ3.index(i)])
            if i - 16 > 0:
                RQ4.append(i - 16)
                new_vorud.append(vorud[RQ3.index(i)])
    print("SPN")
    print("RQ4: ", RQ4)
    if RQ4 != []:
        SPN2(RQ4, new_vorud)
    return RQ4, new_vorud
processes, vorud = SPN(processes,vorud)
SPN2(processes, vorud)
