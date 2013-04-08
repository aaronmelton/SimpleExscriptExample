#!/usr/bin/python
import Exscript

from Exscript.util.interact	import read_login
from Exscript.protocols		import SSH2

account = read_login()				# Prompt the user for his name and password
socket = SSH2()						# Set conenction type to SSH2
socket.connect('192.168.1.1')		# Open connection to router
socket.login(account)				# Authenticate on the remote host

socket.execute('terminal length 0')	# Disable page breaks in router output
									# socket.autoinit() doesn't seem to disable
									# page breaks; Using standard command instead
socket.execute('show run')			# Send command to router
print socket.response				# Print results of command to screen

socket.send('exit\r')				# Send command to exit gracefully
									# socket.execute('exit') produces EOF error
socket.close()						# Close connection

