import subprocess
import re

class Net:

  DEFAULT_REGEX = r'(?P<type>\S+) \S+ \S+  \S+ (?P<bytes>\S+) \(\S+ \S+\)'

  def __init__(self, command='/sbin/ifconfig eth0'):

    self._command = command
    self._regex = re.compile(self.DEFAULT_REGEX)

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
