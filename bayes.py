#-- bayes.py BY:Hinux --#
#Including training function, classifying function 

#Bayes Train
def train(report_path:str):
    #P(A|x1,x2,...)=P(x1,x2,...|A)*P(A)/P(x1)*P(x2)*... However, calculation with small possibilities may cause underflow.
    #so we use ln() here to avoid this bug
    pass