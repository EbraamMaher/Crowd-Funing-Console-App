import fund_parser as fp

import os
############################################################################ 
#                        #####main program######            
############################################################################ 
####1 - Authentication System:
### sign up or login
while True:
    
    print("\t\t"*2,"="*10,"create account","="*10)
    print('''
          press 1 for sign up
          press 2 for login
          press 3 to exit
          ''')
    action= input()
    if action == '1' :
        user=fp.get_user_data()
        fp.write_data("users_login_data",user,'a')
    
    elif action=='2':        
        ##• Login
        '''• The user should be able to login after 
        activation using his email and password'''
        m= fp.login()
        break
    elif action=='3':  os._exit(0)
    
    else :
        print("invalid input")
        
    
while True :
    file_name='projects_data'
    if m : 
        print("\t\t"*2,"="*10,"Welcome back ","="*10)
    print('''
          press 0 to create new project
          press 1 to view all projects
          press 2 to edite your projects
          press 3 to delete a projects
          press 4 to search for a project using date
          press 5 to exit
          ''')
          
    selection= input()
    if selection=='0':
        p_data=fp.get_projects_data(m)
        fp.write_data(file_name, p_data,mode='a')
        
        
    elif selection=='1':
        fp.display_data(file_name)
        
    elif selection=='2':
        proj_id=input("Enter project id ")
        fp.apply_changes(file_name, '2', proj_id, m)
        
    elif selection=='3':
        proj_id=input("Enter project id ")
        fp.apply_changes(file_name, '1', proj_id, m)
        
    elif selection=='4':
           fp. search(file_name)
    elif selection=='5': os._exit(0)  
    else:
        print("invalid input")
        
        