# usr/bin/python
import httpx
import subprocess

print (httpx.get("https://57f1-103-161-69-252.ngrok-free.app").text)
print (subprocess.call("ls"))