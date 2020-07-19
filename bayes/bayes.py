#-- bayes.py BY:Hinux --#
#This .py would get data from a specified file named data_set.txt in which sentences are divided by line-break symbols.
#Then it would generate a vocabulary vector table after shattering a whole article into sentences then fragmented words
import sys
import os
import pathlib
import re
sys.path.append(str(pathlib.Path(__file__).parent.absolute()).replace('/bayes',''))
from err_log import log
import json

def debug(string:str):
    print(string)
    exit()


class data_set_generator:

    def read_from_file(self,file_path:str):

        try:
            article=""
            with open(file_path,"r") as f:
                with open("./result1.txt","w+") as ds:
                    content=f.read()
                    content=content.rsplit('\n')
                    for i in content:
                        article+=i
                    article=str.lower(article)
                    article=re.split('\.+|\?|!',article)            #\.+ here is to split with omission symbol(...) but we don't know how many "." would be written.
                    for i in range(len(article)):
                        article[i]+='\n'
                    ds.writelines(article)
                    ds.close()
                f.close()

        except FileNotFoundError as e:      #Show traceback information if file was not found
            err_msg=e.with_traceback(e.__traceback__)
            log(err_msg)




#This class realizes preconditioning 
class read_from_data_set:
    
    #**ATTENTION: THIS IS THE RESULT. ITS TYPE IS DICT.
    result={}
    
    #words is reserved for word count
    words=[]
    vector={}
    vocabulary=[]

   #non-informative words
    words_rm=['but','however','with','on','also','and','an','a','the','among', 'over', 'past', 'through', 'at', 'in', 'before', 'from', 'for', 'till', 'since', 'beside', 'to', 'behind', 'above', 'between', 'into', 'around', 'after', 'upon', 'during', 'with', 'by', 'on', 'of', 'until', 'below', 'without']

    #Read the result1.txt and then generate the vocabulary vector.
    #Here result1 is the result brought by first-time process(i.e result1.txt, the excrement of data_set_generator.py :-p)
    def report_gen(self,result1_path:str):          
        try:
            flag:bool=True
            with open(result1_path,"r") as f:
                line=f.readline()

                while line:
                    line=line.replace("\n",'').replace(',','').rsplit(" ")                  #Fuck the '\n'(line-break symbol) and ' '(space) off for better work(i.e. shattering the string into a list)
                    for i in range(len(line)):
                        for j in range(len(self.words_rm)):      
                            if line[i]==self.words_rm[j] or line[i]==' ' or line[i]=='':       
                                flag=False                                     #If the word equals to a word of non-informative-word array then tell the outside loop not to append
                                break
                        if flag:                                                        #Inner loop:"Hey! Everything is ok! Just write the word into account!"
                            self.words.append(line[i])         #Outside loop:"OK! Copy that~~ :-)"
                        flag=True                                                   #Reset the flag                             
                    line=f.readline()

                self.vocabulary=list(set(self.words))                #remove repeated elements and convert back to list

                #vector:count of each word
                #initialize the dict vector{}
                for i in range(len(self.vocabulary)):
                    self.vector[self.vocabulary[i]]=0
                
                #counting
                for i in range(len(self.vocabulary)):
                    for j in range(len(self.words)):
                        if self.words[j]==self.vocabulary[i]:
                            self.vector[self.vocabulary[i]]+=1

                #Gather the results together
                self.result['vocabulary']=list(self.vocabulary)
                self.result['words']=list(self.words)
                self.result['class']=1

                #Count the words
                #total:total count
                self.result['total']=len(self.words)
                #vector:count of each word
                self.result['vector']=self.vector

                #generate the report.txt
                with open("report.txt","w+") as report:
                    report.write(json.dumps(self.result))
                report.close()

                #debug(self.result)
                f.close()
            

        except FileNotFoundError as e:
            print(e.with_traceback(e.__traceback__))

'''if __name__ == "__main__":
    #read_from_data_set.read_result1(read_from_data_set,os.getcwd()+"/result1.txt")
    read_from_data_set.report_gen(read_from_data_set,"/home/hinwai/projects/noob/bayes/result1.txt")
    with open("report.txt") as r:
        print(json.load(r))
    r.close()'''