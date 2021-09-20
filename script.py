import pandas as pd
import subprocess


def record_ping(path):

    df = pd.read_excel(path)

    ips = df["IP Address"]

    n = 0
    print("pinging ... ")
    new = pd.DataFrame({'IP Address': [i for i in ips], 'Live': [output(i) for i in ips]})
    new.to_excel('new.xlsx')


    

def output(ip):
    x = subprocess.run(["ping",f"{ip}"], capture_output=True)
    if x.returncode == 0:
        return "Yes"
    return "Decommisioned"



record_ping("./ips.xlsx")