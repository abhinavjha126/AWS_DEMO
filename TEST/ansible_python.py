import paramiko
from subprocess import *
command = "df"

# Update the next three lines with your
# server's information

host = "10.14.20.135"
username = "sdp"
password = "redHAT733#@+"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
stdin, _stdout,_stderr = client.exec_command("df")
print(stdout.read().decode())
client.close()
