"""
Execute shell command 'dir' and print the output
"""

print("Execute shell command 'dir' and print the output")
print("-"*20)
# -------------------

import subprocess

cmd_output = subprocess.check_output('ls', shell=True)
print("cmd_output : \n\n", cmd_output)
print("type of cmd_output :\n\n ", type(cmd_output))
cmd_output = cmd_output.decode()
print("type of cmd_output after convert to str: \n\n", type(cmd_output))
print(cmd_output)
print("-"*40)
# -------------------