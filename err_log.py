#-- log.py BY:Hinux --#
#This .py is used to log the error
import time

def log(err_message:str):
    try:
        err_msg="**["+str(time.ctime())+"]  "+err_message+'\n'          #Error Message: It may looks like "**[Fri Jul 17 17:40:10 2020] something error"
        with open('./log.txt','a+') as f:
            f.write(err_msg)
            f.close()
            return True
    except Exception as e:
        print(e.with_traceback(e.__traceback__))
        return False

'''if __name__ == "__main__":
    log("error!")'''