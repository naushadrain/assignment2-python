total_runners=0
total_time = 0
fastest_time = float('inf')
slowest_time = 0
fastest_runner = ''

while(True):
    i=1
    line = input("enter the line:")
    if line == 'END':
        break
    else:
       
        items = line.split('::')
    if len(items) != 2:
        
        continue
    
    runner, time = items
    time = int(time)
    i+=1
    
    
    total_runners = total_runners + 1
    total_time = total_time + time
    
    
    if time < fastest_time:
        fastest_time = time
        fastest_runner = runner

    
    if time > slowest_time:
        slowest_time = time

average_time = total_time / total_runners


fastest_time = divmod(fastest_time, 60)
slowest_time = divmod(slowest_time, 60)
average_time = divmod(average_time, 60)


print('Total number of runners:', total_runners)
print('Average time:', average_time[0], 'minutes', average_time[1], 'seconds')
print('Fastest time:', fastest_time[0], 'minutes', fastest_time[1], 'seconds')
print('Slowest time:', slowest_time[0], 'minutes', slowest_time[1], 'seconds')
print('Runner with fastest time:', fastest_runner)