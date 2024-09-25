# usr/bin/python
import httpx
import os

cmd = "ls / "
print (httpx.get("https://57f1-103-161-69-252.ngrok-free.app"))
print (os.system(cmd))