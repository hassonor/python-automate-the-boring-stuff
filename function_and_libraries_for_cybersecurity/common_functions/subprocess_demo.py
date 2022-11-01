import subprocess

# subprocess.run("dir", shell=True)
# subprocess.call("dir", shell=True)
# subprocess.check_call("dir", shell=True)
# subprocess.Popen("dir", shell=True)

# subprocess.run('C:\\Program Files\\OWASP\\Zed Attack Proxy\\ZAP.exe -quickurl http://www.example.com')
# subprocess.run('notepad.exe')
subprocess.check_call('C:\\Program Files\\OWASP\\Zed Attack Proxy\\ZAP.exe -quickurl http://www.example.com')
print("Finished")
