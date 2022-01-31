import pymysql
import hashlib


def signin(fname,lname,pwd,branch,email,username):
    con=pymysql.connect(host='localhost',user='root',password='muku123@',db='college')
    handle=con.cursor()

    #hashing
    salt = "5gz"
    pwd_sec = pwd + salt
    pwd = hashlib.md5(pwd_sec.encode())

    pwd = pwd.hexdigest()
    print(pwd)
    sql="insert into `teacher` values('{0}','{1}','{2}','{3}','{4}','{5}');".format(fname,lname,pwd,branch,email,username)
    handle.execute(sql)
    con.commit()
    con.close()

def logindash(username,pwd):
    
   
   
    '''try:
        
        pass
        #con=pymysql.connect(host='localhost',user='root',password='muku123@',db='college')
        
    except Exception:
        print("Error")
        var=False
    else:
        #handle=con.cursor()
        var=True
    
            
    if var==True:
       
        
        #sql="select username,pwd from `teacher`;"
        #handle.execute(sql)
        #full_data  =  handle.fetchall()      #full set of username and passwords
        for single_data in full_data:        #iterating over tuple
            uname     =  single_data[0]      #username
            password  =  single_data[1]      #password

            salt = "5gz"
            pwd_sec = pwd + salt
            pwd = hashlib.md5(pwd_sec.encode())
            pwd = pwd.hexdigest()
            print(pwd)
            if uname == username and password == pwd:
                query="select fname,lname,branch from `teacher` where username = '{0}' ;".format(uname)
                handle.execute(query)
                info=handle.fetchall()
                for item in info:
                    f_name=item[0]
                    l_name=item[1]
                    branch=item[2]
                
                result = True
                return result,f_name,l_name,branch                  #9646647402
        else:
            res=False
            return False, False, False, False
            con.close()
            
    else:
        print("Cant reach server at the moment")'''
    return True,'Ishan','Gambhir','cse'
        
    
    
    
if __name__ == "__main__":
    a,b,c,d=login('dasdas','sadassdas')
    print(a,b,c,d)
