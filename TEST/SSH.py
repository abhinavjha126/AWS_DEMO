import paramiko
from paramiko import SSHClient

client = SSHClient()
#client.load_system_host_keys()
#client.load_host_keys('~/.ssh/known_hosts')
#client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('10.14.20.135', username='sdp', password='redHAT733#@+')
client.close()
