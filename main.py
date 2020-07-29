#-- main.py BY:Hinux --
import sys
import pathlib
import os
sys.path.append(str(pathlib.Path(__file__).parent.absolute())+'/bayes')
from preconditioning.preconditioning import *

#debug
def debug(string:str):
    print(string)
    exit()

if __name__ == "__main__":
    articles=os.listdir(os.getcwd()+'/articles')             #List of files of the directory.
    for article in articles:
        read_from_file(os.getcwd()+'/articles/'+article)
        report_gen(os.getcwd()+'/result1.txt')