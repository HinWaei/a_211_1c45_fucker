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
        frag=""

        #try:
        with open(file_path,"r") as f:
            with open("./vector.txt","w+") as ds:
            #Here I don't wanna use f.read() directly because loading the whole passage into memory would take great size of space
                line=f.readline() 
                while line:
                    s=[]
                    sentences=[]                       #s:Each line with separated sentences.         sentences:Made up of elements except the one with fragment sentence of s
                    #"line" is reserved in order to get fragment sentence(i.e. a sentence that not ended by period symbol(.) )
                    s=re.split("\.|!|\?|\.\.\.",line)                       #Split each line with '.' to get single sentences
                    s[0]=frag+s[0]
                    sentences+=s[:-1]               
                    frag=s[-1] if s[-1]!='.' else ""             #If the line is not ended by period(.) then the last element would be the fragment sentence
                    if(len(s))>1:
                        for i in range(len(sentences)):
                            if sentences[i][-1]!='\n':
                                debug(sentences[i][-1])
                                sentences[i]+='\n'
                        ds.writelines(sentences)
                    line=f.readline()

                ds.close()
            f.close()

            '''except FileNotFoundError as e:      #Show traceback information if file was not found
                err_msg=e.with_traceback(e.__traceback__)
                log(err_msg)'''

if __name__ == "__main__":
    data_set_generator.read_from_file(data_set_generator,str(os.getcwd()+"/article.txt"))