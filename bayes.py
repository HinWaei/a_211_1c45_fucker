#-- bayes.py BY:Hinux --#
#Including training function, classifying function 

import json

#Bayes Train
def train(report_path:str):
    #P(A|x1,x2,...)=P(x1,x2,...|A)*P(A)/P(x1)*P(x2)*... However, calculation with small possibilities may cause underflow.
    #so we use ln() here to avoid this bug: ln(P)=lnP(x1|A)+lnP(x2|A)+...+lnP(xn|A)+lnP(A)-( lnP(x1)+lnP(x2)+...+lnP(xn) )
    
    try:
        with open(report_path,"r+") as f:
            line=f.readline()
            while line:
                line=json.loads(line)


    except Exception as e:
        print(e.with_traceback(e.__traceback__))