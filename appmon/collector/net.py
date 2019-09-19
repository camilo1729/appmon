import subprocess
import re

class Net:

  DEFAULT_REGEX = r'(?P<type>\S+) \S+ \S+  \S+ (?P<bytes>\S+) \(\S+ \S+\)'

  def __init__(self,
               command='/sbin/ifconfig eth0',
               opts={'field' : 'bytes', 'group_by' : 'type'} ):

    self._command = command
    self._regex = re.compile(self.DEFAULT_REGEX)
    self.opts = opts
    self._data = self.execute()

  def execute(self):

    cmd_array = self._command.split(" ")
    out_cmd = subprocess.check_output(cmd_array)
    out_lines = [line.strip() for line in out_cmd.split('\n')]
    values = []
    for line in out_lines:
      groups = self._regex.match(line)
      if groups:
        values.append(groups.groupdict())

    return values

  def get_delta(self):
      delta={}
      current_data = self.execute() 
      data_delta = current_data+self._data
      self._data = current_data
      group_by = self.opts['group_by']
      field = self.opts['field']
      for register in data_delta:
        if not register[group_by] in delta:
          delta[register[group_by]] = float(register[field])
        else:
          delta[register[group_by]]-= float(register[field])

      return delta
