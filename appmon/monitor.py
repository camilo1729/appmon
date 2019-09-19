import collector.net as net
import time

previous = None
time_freq = 5

#   for field,value in group.iteritems():
#     print('{} : {} Mbytes/sec'.format(field,(value[1]-value[0]))))

netcollect = net.Net(command='/sbin/ifconfig wlp3s0')
while True:
  time.sleep(time_freq)
  print(netcollect.get_delta())
