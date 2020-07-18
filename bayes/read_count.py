#-- read_count.py BY:Hinux --#
#This .py would get data from a specified file named data_set.txt in which sentences are divided by line-break symbols.
#Then it would generate a vocabulary vector table after shattering a whole article into sentences then fragmented words
import os
import json

def debug(string:str):
    print(string)
    exit()

class read_from_data_set:
    
    #**ATTENTION: THIS IS THE RESULT. ITS TYPE IS DICT.
    result={}
    
    #vocabulary is reserved for word count
    vocabulary=[]
    vector=[]
   #words that should be removed
    words_rm=['but','however','with','on','also','and','an','a','the','among', 'over', 'past', 'through', 'at', 'in', 'before', 'from', 'for', 'till', 'since', 'beside', 'to', 'behind', 'above', 'between', 'into', 'around', 'after', 'upon', 'during', 'with', 'by', 'on', 'of', 'until', 'below', 'without']

    #Read the result1.txt and then generate the vocabulary vector.
    #Here result1 is the result brought by first-time process(i.e result1.txt, the excrement of data_set_generator.py :-p)
    def vector_gen(self,result1_path:str):          
        try:
            flag:bool=True
            with open(result1_path,"r") as f:
                line=f.readline()

                while line:
                    line=line.replace("\n",'').replace(',','').rsplit(" ")                  #Fuck the '\n'(line-break symbol) and ' '(space) off for better work(i.e. shattering the string into a list)
                    for i in range(len(line)):
                        for j in range(len(self.words_rm)):      
                            if line[i]==self.words_rm[j] or line[i]==' ' or line[i]=='':       #replace the words that fit in with words_rm
                                flag=False
                                break
                        if flag:    
                            self.vocabulary.append(line[i])
                        flag=True
                                
                    line=f.readline()

                self.vector=set(self.vocabulary)                #remove repeated elements
                
                self.result['vector']=list(self.vector)
                self.result['vocabulary']=list(self.vocabulary)
                self.result['class']=True

                f.close()

        except FileNotFoundError as e:
            print(e.with_traceback(e.__traceback__))

if __name__ == "__main__":
    #read_from_data_set.read_result1(read_from_data_set,os.getcwd()+"/result1.txt")
    read_from_data_set.vector_gen(read_from_data_set,"/home/hinwai/projects/noob/bayes/result1.txt")
    print(read_from_data_set.result)