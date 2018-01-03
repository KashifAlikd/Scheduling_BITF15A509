burst_time=[]
print("Enter the number of process: ")
n=int(input())
print("Enter the burst time of the processes: \n")

#for i in range(0,n):
   #burst_time.insert(i,i+1)
burst_time=list(map(int, raw_input().split()))
waiting_time=[]
avg_wait_time=0
turn_a_time=[]
avg_turn_a_time=0
waiting_time.insert(0,0)
turn_a_time.insert(0,burst_time[0])
for i in range(1,len(burst_time)):
    waiting_time.insert(i,waiting_time[i-1]+burst_time[i-1])
    turn_a_time.insert(i,waiting_time[i]+burst_time[i])
    avg_wait_time+=waiting_time[i]
    avg_turn_a_time+=turn_a_time[i]
avg_wait_time=float(avg_wait_time)/n
avg_turn_a_time=float(avg_turn_a_time)/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
    print(str(i)+"\t\t"+str(burst_time[i])+"\t\t"+str(waiting_time[i])+"\t\t"+str(turn_a_time[i]))
    print("\n")
print("Average Waiting time is: "+str(avg_wait_time))
print("Average Turn Arount Time is: "+str(avg_turn_a_time))
