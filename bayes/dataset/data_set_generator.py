#-- data_set_generator.py BY:Hinux --#
#This .py is used to get sentences from an article and output them to a file with line-break symbols at the end of each sentence.
#The output file could be used to provide data set for other purposes (e.g. The Bayes Learning here).
import sys
import os
sys.path.append(str(os.getcwd()).replace('/bayes/dataset',''))
from err_log import log
class data_set_generator:

    def read_from_file(self,file_path:str):
        frag=""

        try:
            with open(file_path,"r") as f:
            #Here I don't wanna use f.read() directly because loading the whole passage into memory would take great size of space
                while True:
                    s=[]
                    sentences=[]                       #s:Each line with separated sentences.         sentences:Made up of elements except the one with fragment sentence of s
                    line=f.readline()                   #"line" is reserved in order to get fragment sentence(i.e. a sentence that not ended by period symbol(.) )
                    s=line.split(".")                       #Split each line with '.' to get single sentences 
                    sentences+=s[:-1]               
                    frag=s[-1] if line[-1]!='.' else ""             #If the line is not ended by period(.) then the last element would be the fragment sentence


        except EOFError as eof:                 #Quit if EOF was met
            f.close()
            with open("data_set2.txt","w+") as ds:
                for i in sentences:
                    f.write(sentences+'\n')
                f.close()
            return
        '''except FileNotFoundError as e:      #Show traceback information if file was not found
            err_msg=e.with_traceback(e.__traceback__)
            log(err_msg)'''

if __name__ == "__main__":
    data_set_generator.read_from_file(data_set_generator,os.path.join(os.getcwd(),"article.txt"))