#-- data_set_generator.py BY:Hinux --#
#This .py is used to get sentences from an article and output them to a file with line-break symbols at the end of each sentence.
#The output file could be used to provide data set for other purposes (e.g. The Bayes Learning here).
import sys
import os
import pathlib
import re
sys.path.append(str(pathlib.Path(__file__).parent.absolute()).replace('/bayes/dataset',''))
from err_log import log

def debug(msg:str):
    print(msg)
    exit()

class data_set_generator:

    def read_from_file(self,file_path:str):

        #try:
        article=""
        with open(file_path,"r") as f:
            with open("./vector.txt","w+") as ds:
                content=f.read()
                content=content.rsplit('\n')
                for i in content:
                    article+=i
                article=str.lower(article)
                article=re.split('\..|\?|!',article)
                for i in range(len(article)):
                    article[i]+='\n'
                ds.writelines(article)
                ds.close()
            f.close()

            '''except FileNotFoundError as e:      #Show traceback information if file was not found
                err_msg=e.with_traceback(e.__traceback__)
                log(err_msg)'''

if __name__ == "__main__":
    data_set_generator.read_from_file(data_set_generator,str(os.getcwd()+"/article.txt"))