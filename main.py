#-- main.py BY:Hinux --
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.absolute())+'/bayes')
from bayes.preconditioning import *

def debug(string:str):
    print(string)
    exit()



if __name__ == "__main__":
    read_from_file(os.getcwd()+'/bayes/article.txt')
    report_gen(os.getcwd()+'/result1.txt',0)