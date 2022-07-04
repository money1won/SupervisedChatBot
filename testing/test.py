
import torch
import subprocess
import sys

files = ["chat.py", "discord_main.py"]

for f in files:
    subprocess.Popen([sys.executable, f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
