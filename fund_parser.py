import re
import time
from datetime import datetime
################################################################
def name(message):
    regex=r'[A-Za-z]{2,25}( [A-Za-z]{2,25})?'
    
    user_name= input(message).strip()
    if not user_name :
        print("This field is required")
        return name(message)
    elif not re.fullmatch(regex, user_name) :     
        print("only Alphabet is allowed")
        return name(message)
    else :
        return user_name
#################################################################
def email(message):
    regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    user_mail= input(message).strip()
    if not user_mail :
        print("This field is required")
        return email(message)
    elif not re.fullmatch(regex, user_mail) :     
        print("invalid Email")
        return email(message)
    else :
        return user_mail
############################################################
def passwd(message):
    #regex=r'[A-Za-z0-9@#$%^&+=]{8}'
    reg=r'\b^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$\b'
    #regex=r'[A-Za-z0-9]{8,}'
    password=input(message)
    if not password:
        print("This field is required")
        return passwd(message)
    elif not re.fullmatch(reg, password): #re.fullmatch(regex,password):
        print('''very weak password ,password shuold :
              1-at least 8 characters
              2-pecial character 
              3-upper and lower case characters
              4-numbers
              ''')
        return passwd(message)
    else :
        return password 
###########################################################        
def confirm_passwd(message,value1):
    # if c==5: 
    #     print("you exceed the allowed number of trials")
    #     exit()
    value2=input(message)
    if value1==value2:
        return True
    else:
        #c+=1
        print("not matched password") 
        return  confirm_passwd(message,value1)

######################################################
def mobile(message):
    regex=r'\b^01[0125][0-9]{8}$\b'
    
    mob_num= input(message).strip()
    if not mob_num :
        print("This field is required")
        return mobile(message)
    elif not re.fullmatch(regex, mob_num) :     
       print("invalid Mobile number")
       return mobile(message)
    else :
        return mob_num
#################################################
def mail_existence(path,value):
    try:
        fh=open(path)
            
            
    except: 
        print("unexpected error occured")
        return False

    else:
       #print("mail_existence process done successfully")
       users=fh.readlines()
       for user in users:
            user = user.split(",")
            #print(user[3])
            
            if user[3]==value:
                return True,user[2]
            
       else: return False,0
            
       fh.close()

       
 #################################################   
    
def get_user_data():    
    fname=name("First name :\t")#alphabet only
    lname=name("last name  :\t")#alphabet only
    mail=email("Email      :\t")#acc. to pattern
    check=mail_existence("users_login_data",mail)
    
    if check[0]: 
        print("Sorry E-Mail already exists")
        return get_user_data()
    password=passwd("Password     :\t")#must match reptyped one   #  #bounes : chacters / upper /lower /num/special ...... 
    
    pass_confirm=confirm_passwd("retype password :\t",password) #confirm password
    
    mNumber=mobile("Mobile number :\t+2") # +20 " number must be egyptian 01[0-->9 except 3] "
    
#    active_status=active("active your account")
    if pass_confirm : 
        return [fname,lname,password,mail,mNumber]
    else:
        print("account creation failed")
        get_user_data()


###################################################
def get_projects_data(email):
    '''function that prompot all projects data from the user
     arguments: user email "since it is the unique identity"
     return : a list of all data 
     
     hint: if email == -1 this means we just get data to update a specific row
     
     '''   
    
    ##note : each campaign must have unique id which must used to get a specific campign
    print("please,Enter project")
    title=input("Title        :\t")#alphanumeric only
    details=input("Detials      :\t")#text only
    tot_target=input("Total target :\t")#intger nums(or float)
    
    start_time=check_date("start time :\t",datetime.now())
    end_time=check_date("end time :\t",datetime.strptime(start_time,"%d-%m-%Y"))
    
    if email == -1 : return  [title,details,tot_target,start_time,end_time]
    
    return [str(round(time.time())),title,details,tot_target,start_time,end_time,email]

##############################################################
def write_data(file_name,data,mode):
    '''
    function to write project data in a txt file with file name passed as arguemnt
    
    arguments : 1- file name "str" 2- data "list of all project data"
    return : None "only print a message or switch to get_projects_data function 
    if it encountered any error"
    
    '''
    data=",".join(data)
    try:
        with open(file_name, mode) as fh:
            fh.write(f"{data}\n")
    except: 
       print("unexpected error occured")
       #get_projects_data()
   
    else:
       print("process done successfully")
       
#############################################################

def apply_changes(file_name,action,proj_id,email):
   print("enter done")
   mode='r'
   fh_r=open(file_name,mode) 
   projects=fh_r.readlines()
   fh_r.close()
   #print(projects)

   mode="w"
   fh_w=open(file_name,mode)
   #print("write start")
   
   for proj in projects:
        proj = proj.split(",")
        proj[-1]=proj[-1].strip("\n")
        
        if email==proj[-1] : ###only owner can update or delete
            
            ##delete
            print("email correct")
            print(proj_id == proj[0])
            if proj_id == proj[0] and action =='1' :
                print("deleted successfully")
                continue

            ###update
            print("update")
            if proj_id==proj[0] and action == '2'  :
                d=get_projects_data(-1)
                print("updated successfully")
                
                d.insert(0, proj_id)                        
                d.append(email)
                proj=d
            print(f"{proj}")
            
            proj=",".join(proj)
            fh_w.write(f"{proj}\n")
        else: pass
   fh_w.close()
   
##############################################################
def display_data(file_name):
    '''

    Parameters
    ----------
    file_name : str
    a path for file to be displayed     

    Returns
    -------
    None.

    '''
    try:
         fh=open(file_name) 
            
    except: 
        print("unexpected error occured")
        get_projects_data()
   
    else:
        projects=fh.readlines()
        for proj in projects:
            proj = proj.split(",")
            proj[-1]=proj[-1].strip("\n")
    
           # proj=proj.replace(',', '|\t|')
           # proj=proj.strip("\n")
            print(proj)
            print("process done successfully")
    fh.close()
##############################################################
def check_date(message,b):
    
    format="%d-%m-%Y"
    date= input(message)
    try:
       
      a=datetime.strptime(date,format)
      delta= a-b
      
      if delta.days < 0:
          print("not logical date")
          return check_date(message, b)
      else: return date
    except:
      print("invalid format")
      return check_date(message,b)
##############################################################
def search(file_name):
    c=0
    date= check_date("please Enter a date :   ",datetime.strptime('01-01-1000',"%d-%m-%Y"))
    try:
        fh=open(file_name) 
            
    except: 
        print("unexpected error occured")
        
    else:
        projects=fh.readlines()
        for proj in projects:
            proj = proj.split(",")
            proj[-1]=proj[-1].strip("\n")
            if proj[4]== date :
                
                print (proj)
                c+=1
        if c==0: print("nothing to show at this date")
##############################################################

def login():
    
    #check level 1 :mail validation
    m=email("Email \t:")
    #check level2 : email existence
    auth,retrved_pass=mail_existence('users_login_data',m)
    if auth : 
        if confirm_passwd("password :",retrved_pass) :
            print("successfully login")
            return m
        
    else : 
        print("The Email you enetered does not exist")
        return login()
    