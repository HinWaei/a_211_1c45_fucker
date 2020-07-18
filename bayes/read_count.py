#-- read_count.py BY:Hinux --#
#This .py would get data from a specified file named data_set.txt in which sentences are divided by line-break symbols.
#Then it would generate a vocabulary vector table after separating each word of sentences and 

import re
import os

def debug(string:str):
    print(string)
    exit()

class read_from_data_set:
    #Here result1 is the result brought by first-time process(i.e result1.txt, the excrement of data_set_generator.py :-p)
    
    vocabulary=set([])
   #words that should be removed
    words_rm=['an','a','the','among', 'over', 'past', 'through', 'at', 'in', 'before', 'from', 'for', 'till', 'since', 'beside', 'to', 'behind', 'above', 'between', 'into', 'around', 'after', 'upon', 'during', 'with', 'by', 'on', 'of', 'until', 'below', 'without']

    def read_result1(self,result1_path:str):
        try:
            with open(result1_path,"r") as f:
                line=f.readline()
                while line:
                    for word in self.words_rm:
                        line=line.replace(word,'')
                    self.vocabulary.add(line)
                    line=f.readline()
                debug(self.vocabulary)
                f.close()

        except FileNotFoundError as e:
            print(e.with_traceback(e.__traceback__))

if __name__ == "__main__":
    read_from_data_set.read_result1(read_from_data_set,os.getcwd()+"/result1.txt")