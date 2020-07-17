#-- data_set_generator.py BY:Hinux --#
#This .py is used to get sentences from an article and output them to a file with line-break symbols at the end of each sentence.
#The output file could be used to provide data set for other purposes (e.g. The Bayes Learning here).
import err_log
class data_set_generator:

    def read_from_file(self,file_path:str):
        
        try:
            with open(file_path,"r") as f:
            #Here I don't wanna use f.read() directly because loading the whole passage into memory would take great size of space
                while True:
                    line=f.readline()
                    sentences=line.split(".")
                    if line[-1]!=".":
                        sentences[-1]

        except EOFError as eof:
            return
        except FileExistsError as e:
            err_msg=e.with_traceback(e.__traceback__)
            err_log(err_msg)