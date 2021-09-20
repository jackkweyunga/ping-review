import pandas as pd
import subprocess
import sys

def record_ping(path):

    df = pd.read_excel(path)

    ips = df["IP Address"]

    print("pinging ... ")
    new = pd.DataFrame({'IP Address': [i for i in ips], 'Live': [output(i) for i in ips]})
    new.to_excel('new.xlsx')


    

def output(ip):
    x = subprocess.run(["ping",f"{ip}"], capture_output=True)
    if x.returncode == 0:
        return "Yes"
    return "Decommisioned"

# listen for args
if sys.argv[1] != None:

    path = sys.argv[1]

    record_ping(path)