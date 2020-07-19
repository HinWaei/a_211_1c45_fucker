import json
import os
if __name__ == "__main__":
    with open(os.getcwd()+"/report.txt","r+") as f:
        line=f.readline()
        while line:
            line=json.loads(line)
            print(line)
            line=f.readline()