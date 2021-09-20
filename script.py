import pandas as pd
import subprocess


def record_ping(path):

    df = pd.read_excel(path)

    ips = df["ip"]

    n = 0
    print("pinging ... ")
    new = pd.DataFrame({'ip': [i for i in ips], 'ping': [output(i) for i in ips]})
    new.to_excel('new.xlsx')


    

def output(ip):
    x = subprocess.run(["ping",f"{ip}"], capture_output=True)
    if x.returncode == 0:
        return "live"
    return "decommisioned"



record_ping("./ips.xlsx")