"""
Execute shell command 'dir' and print the output
"""

print("Execute shell command 'dir' and print the output")
print("-"*20)
# -------------------

import subprocess

cmd_output = subprocess.check_output('dir', shell=True)
print("cmd_output : ", cmd_output)
print("type of cmd_output : ", type(cmd_output))
cmd_output = cmd_output.decode()
print("type of cmd_output after convert to str: ", type(cmd_output))
print(cmd_output)

print("-"*40)
# -------------------
