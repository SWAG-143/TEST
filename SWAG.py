import os, sys
os.system("git pull")
try:
    __import__("SWAG").___swag___()
except Exception as e:
    exit(str(e))
