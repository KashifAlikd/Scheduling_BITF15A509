
print("Enter the number of processess: ")
n=int(input())
processes=[]
for i in range(0,n):
     processes.insert(i,i+1)
print("Enter the burst time of the processes:")

burst_time=list(map(int, raw_input().split()))

print("Enter the priority of the processes: \n")
priority=list(map(int, raw_input().split()))
turn_around_time=[]
waiting_time=[]
 
for i in range(0,len(priority)-1):
    for j in range(0,len(priority)-i-1):
        if(priority[j]>priority[j+1]):
            temp=priority[j]
            priority[j]=priority[j+1]
            priority[j+1]=temp
            temp=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j+1]=temp
   	    temp=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=temp
 
waiting_time.insert(0,0)
turn_around_time.insert(0,burst_time[0])
for i in range(1,len(processes)):
     waiting_time.insert(i,waiting_time[i-1]+burst_time[i-1])
     turn_around_time.insert(i,waiting_time[i]+burst_time[i])
 

avg_turn_around_time=0
avg_waiting_time=0
for i in range(0,len(processes)):
     avg_waiting_time=avg_waiting_time+waiting_time[i]
     avg_turn_around_time=avg_turn_around_time+turn_around_time[i]
     avg_waiting_time=float(avg_waiting_time)/n
     avg_waiting_time=float(avg_turn_around_time)/n
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
     print(str(processes[i])+"\t\t"+str(burst_time[i])+"\t\t"+str(waiting_time[i])+"\t\t"+str(turn_around_time[i]))
     print("\n")
print("Average Waiting time is: "+str(avg_waiting_time))
print("Average Turn Around Time is: "+str(avg_turn_around_time))
