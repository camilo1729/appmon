import collector.net as net
import time



netcollect = net.Net()

previous = None
time_freq = 10


def delta(data=None,field='', group_by=''):
  group={}
  for register in data:
    if not register[group_by] in group:
      group[register[group_by]]=[]

    group[register[group_by]].append(float(register[field]))

  for field,value in group.iteritems():
    print('{} : {}'.format(field,value[1]-value[0]))


previous = netcollect.execute()
while True:
  time.sleep(time_freq)
  current=netcollect.execute()
  delta(previous+current,'bytes','type')
  previoius=current
