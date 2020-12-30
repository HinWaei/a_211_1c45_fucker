"""
ICAS fUcK3r

@Copyright Copyright (c) 2020
@Author Hinux Lam Yiu Hang

The ICAS Login System is widely used in authentication of numbers of services in a southern university of 211 project. 
Modifying this script correctly after analysing specific framework can realize operating on 1c45-required services 
like https://jwx_.___.edu.cn automatically.

Just Enjoy it!!

Time now is 11:37 AM, Dec 26th, 2020
"""

import execjs
import datetime
import requests
import re

#Get UTC Timestamp
def get_gmt_timestamp():
    dt=datetime.datetime.now()
    return int(dt.timestamp()*1000)

#def get timestamp like "Sun, 27 Dec 2020 01:21:23 GMT"
def get_timestamp(time:str):
    dt=datetime.datetime.strptime(time,"%a, %d %b %Y %H:%M:%S GMT")
    return int(dt.timestamp())

#Return the fake rsa(fake DES actually)
#Here I directly call the des.js fetched from target with execjs
#just for the purpose of being lazy :-P
def icas_strEnc(user:str,pwd:str,lt:str):
    ctx=execjs.compile(open('./des.js','r+').read())
    return ctx.call("strEnc",user+pwd+lt,'1','2','3')

#Get pre_login info like lt,rsa
def icas_pre_login(target:str):

    '''
    @param
    target: https://jwx_.___.edu.cn/amp-auth-adapter/login?service=https%3A%2F%2Fjwx_.___.edu.cn%3A443%2F
    @return
    lt,
    '''

    #headers
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    #Login
    ssn=requests.Session()
    req=ssn.get(url=target,headers=headers)
    content=req.content.decode('utf-8')

    #Info returned.
    Cookie_1=ssn.cookies.get_dict()

    JSESSIONID=Cookie_1['JSESSIONID']
    lt=re.search(
        "<input type=\"hidden\" id=\"lt\" name=\"lt\" value=\"[^\"]*\" \/>", \
        content
    )[0].split("\"")[-2]
    execution=re.search(
        "<input type=\"hidden\" name=\"execution\" value=\"[^\"]*\" />", \
        content
    )[0].split("\"")[-2]

    #Update headers:Store JSESSIONID needed to the headers
    headers['Cookie']=f"JSESSIONID={JSESSIONID}"

    return JSESSIONID,lt,execution,headers,ssn


#Login
def icas_login(
    headers:dict,
    target:str,
    ssn:requests.sessions.Session,
    user:str,pwd:str,lt:str,execution:str
):

    """
    @param
    target: https://jwx_.___.edu.cn/amp-auth-adapter/login?service=https%3A%2F%2Fjwx_.___.edu.cn%3A443%2F
    """

    #Data
    icasLogin={
        'ul':len(user),
        'pl':len(pwd),
        'rsa':icas_strEnc(user=user,pwd=pwd,lt=lt),
        'lt':lt,
        'execution':execution,
        '_eventId':'submit'
    }

    #login
    r=ssn.request(
        method='POST',
        url=target,
        data=icasLogin,
        headers=headers
    )

    #get info
    Cookie_2=ssn.cookies.get_dict()
    #Get keys required by following steps here. For example:
    #CASTGC=Cookie_2['CASTGC']
    
    #return CASTGC


if __name__ == "__main__":

    #Initial data
    target="https://jwx_.___.edu.cn/amp-auth-adapter/login?service=https%3A%2F%2Fjwxk.jnu.edu.cn%3A443%2F" #URL like https://jwx_.___.edu.cn/amp-auth-adapter/login?service=https%3A%2F%2Fjwx_.___.edu.cn%3A443%2F

    #Get pre_login data like JSESSIONID,lt,execution
    #"headers" here is used to check whether it has other useful info
    JSESSIONID,lt,execution,headers,ssn=icas_pre_login(target=target)
    
    #Fill certain keys needed with certain values
    #headers['token']=token

    print(f"""
    JSESSIONID: {JSESSIONID}
    lt: {lt}
    execution: {execution}
    headers: {headers}
    """)

    #Enter your student number and password while 50 attempts are allowed
    user=input('User:')
    pwd=input('Password:')

    #ICAS Login
    #CASTGC=icas_login(headers=headers,target=target,ssn=ssn,user=user,pwd=pwd,execution=execution,lt=lt)
