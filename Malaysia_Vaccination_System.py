#**************************************************
# Program: Vaccine
# Course = PROGRAMMING WITH PYTHON
# Course Code: AAPP010-4-2-PWP
# Intake Code: UCDF2109ICT(SE)
# Lecture Name: DR.MASRINA AKMAL BINTI SALLEH
# Hand Out Date: 1 SEPTEMBER 2022
# Hand In Date: 30 OCTOBER
# **************************************************
# Group Members
# Member_1: TP065539 | GAN MING HUI 
# Member_2: TP063370 | HO FENG SHENG
# Member_3: TP065406 | DYANIEL CHING CHEE XIONG
# **************************************************
# Task Distribution
# GAN MING HUI              : New Patient Registration & Statistical Information & All Additional Features
# HO FENG SHENG             : Search Patient Record & Vaccination Status 
# DYANIEL CHING CHEE XIONG  : Vaccine Administration

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Let admin edit vaccine

def vaccine_edit():

    while(True):
        vaccine_details()
        print("\n--------------------Edit Vaccination--------------------")
        print("\n1.Add New Vaccines\n2.Delete Existing Vaccines\n3.Back\n")

        opt = input("Please Enter the selection : ")

        if(opt == "1"):
            add_vaccine()

        elif(opt == "2"):
            delete_vaccine()

        elif(opt == "3"):
            break

        else:
            print("\n*Error : Invalid Input")

            
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Let admin add new vaccine

def add_vaccine():
    flag = False
    while(flag == False):

        print("\n--------------------Add New Vaccine--------------------")

        #Ask new vaccine details
        #vaccine code
        print("\n*Enter 'exit' to exit")
        vc_code = input("Please enter the new vaccine code : ").upper()
        if(vc_code == "EXIT"):
            return
        

        #Validation for VC Code - Make sure new vaccine no exist in the text file
        f = open("vaccine.txt", "r")
        lists = []
            
        for line in f:
            line_split = line.split(",")
            lists.append(line_split) 
                
        for i in range(len(lists)):
            if (vc_code) in lists[i][0]:
                print("*vaccine code exists, Please try again")
                add_vaccine()
                return #to stop asking again the dosage required after executing the add_vaccine
        f.close()
        
        #validation for dosage required
        dosage_required = validation_dosage()
        if(dosage_required == "exit"):
            return
                
        #validation for interval
        interval = validation_interval()
        if(interval == "exit"):
            return
                
        #validation for age_group
        age_group = validation_age()
        min_num = (age_group[:2])
        max_num = (age_group[3:])
        if(age_group == "exit"):
            return

        #Append new vaccine code into text file
        f = open("vaccine.txt","a")
        f.writelines([vc_code,",",dosage_required," dose required",",",interval," week interval",",",min_num,",",max_num,"\n"])
        f.close()

        while(True):
            print("\n*Record added")
            opt = input("\nDo you still want to add new vaccine (yes/no) : ").lower()

            if(opt == "yes"):
                break
            
            elif(opt == "no"):
                flag = True
                break
            
            else:
                print("\n*Error : Invalid Input")
                return
        
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for dosage required

def validation_dosage():
    regex_dosage = '([1-3]{1})'

    while(True):
        print("\n*Enter 'exit' to exit")
        dosage_required = input("Please enter the number of dosage required (Only 1-3 are accepted) : ")

        if(dosage_required == "exit"):
            return dosage_required

        if(len(dosage_required) == 1):

            if(re.search(regex_dosage,dosage_required)):
                return dosage_required

            else:
                print("\n*Error : Invalid dosage required")

        else:
            print("\n*Error : Invalid dosage required")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for interval

def validation_interval():
    regex_interval = '([1-4]{1})'

    while(True):
        print("\n*Enter 'exit' to exit")
        interval = input("Please enter the interval between doses in weeks (Only 1-4 or 'no' are accepted) : ")

        if(interval == "exit"):
            return interval


        if(len(interval) == 1):

            if(re.search(regex_interval,interval)):
                return interval

            else:
                print("\n*Error : Invalid interval")

        elif(interval == "no"):
            return interval
        
        else:
            print("\n*Error : Invalid interval")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for age group

def validation_age():
    while(True):
        print("\n*Enter 'exit' to exit")
        age_group = input("\n*Minimum Age-Maximum Age*\n-Minimum of minimum age is 12 and maximum of minimum age is 18\n-Maximum of maximum age is 80 and it can also be the word 'above'\n\nPlease enter the age group in above format : ")

        if(age_group == "exit"):
            return age_group

        #make sure dash is located between min and max age
        if("-" in age_group):

            #Make sure starts with digit and end with digit
            x = age_group[:2].isdigit()
            y = age_group[3:].isdigit()
            y1 = age_group[3:]

            if((x == True) and (y == True)):


                #make sure the minimum and maximum values is logic
                min_num = int(age_group[:2])
                max_num = int(age_group[3:])

                if((min_num <= 20) and (min_num >=12)):
                    if(max_num <= 80):

                    #make sure the minimum value is smaller than maximum value
                        if(min_num < max_num):
                            return age_group

                        else:
                            print("\n*Error : Invalid Input")
                        

                    else:
                        print("\n*Error : Invalid Input")

                else:
                    print("\n*Error : Invalid Input")
                                
                        
            if(y == False):

                #Prevent no maximum age being entered but 'above' being entered exp:18-above
                if(y1 == "above"):

                    #make sure the minimum value is logic
                    min_num = int(age_group[:2])

                    if(min_num <= 20):
                        return age_group

                    else:
                        print("\n*Error : Invalid Input")

                else:
                    print("\n*Error : Invalid Input")

        else:
            print("\n*Error : Invalid Input")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Let admin delete vaccine
                    
def delete_vaccine():
    flag = True
    while(flag == True):
        print("\n--------------------Delete Vaccine--------------------")
        
        #Ask the vaccine code that admin want to delete
        print("\n*Enter '1' to exit")
        vc_code = input("Please enter the vaccine code you want to delete : ").upper()
        if(vc_code == "1"):
            return

        #Make sure vaccine exist in the text file
        f = open("vaccine.txt", "r")
        lists = []
                
        for line in f:
            line_split = line.split(",")
            lists.append(line_split) 
                    
        for i in range(len(lists)):
            if (vc_code) in lists[i][0]:
                ans = "yes"
                break
            
            else:
                ans = "no"
        f.close()
        
        if(ans == "yes"):
            f = open("vaccine.txt","r")
            text = f.readlines()
            del text[i]
            f.close()

            #insert updated record to the text file
            f = open("vaccine.txt","w")

            #loop each record in the list
            for a in text:
                f.write(a)
            f.close()
            
            print("\n*Deleted Successfully")

        else:
            print("*vaccine code not exists, Please try again")
            delete_vaccine()
            return #to stop asking again the below statement

        #want to continue delete or not
        while(True):
                opt = input("\nDo you still want to delete vaccine (yes/no) : ").lower()

                if(opt == "yes"):
                    break
                
                elif(opt == "no"):
                    flag = False
                    break
                
                else:
                    print("Invalid Input")

 

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Let users view Vaccine details

def vaccine_details():
    print("\n--------------------Vaccine Details--------------------\n")
    f = open("vaccine.txt","r")
    n = 0
    a = 1
    lists = []
    for line in f:
        line_strip = line.strip()
        line_split = line_strip.split(",")
        lists.append(line_split)

        #print the available vaccines
        print(f'{a}.{lists[n][0]} -- {lists[n][1]} | {lists[n][2]} | {lists[n][3]} - {lists[n][4]} age group')
        n = n + 1
        a = a + 1
    f.close()

'''
Registration  
'''

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define admin account

def admin_acc():
    while (True):
        print("\n--------------------Admin Account-------------------")
        print("\n1.Login into Existing Account\n2.Back\n")
        opt = input("Please enter the selection : ")
        
        if (opt == "1"):

            #admin username
            print("\n*Enter '1' to exit")
            admin_user = input("Please enter username : ")
            if(admin_user == "1"):
                return

            #admin password
            print("\n*Enter '1' to exit")
            admin_pass = input("Please enter password : ")
            if(admin_pass == "1"):
                return
            
            if (admin_user == "minghui" and admin_pass == "tp065539"):
                print("\n--------------------Login Successfully--------------------")
                print("\n--------------------Welcome Back--------------------")
                #CALL THE ADMIN MENU
                admin_menu()
                break

            elif (admin_user == "fengsheng" and admin_pass == "tp063370"):
                print("\n--------------------Login Successfully--------------------")
                print("\n--------------------Welcome Back--------------------")
                admin_menu()
                break

            elif (admin_user == "dyaniel" and admin_pass == "tp065406"):
                print("\n--------------------Login Successfully--------------------")
                print("\n--------------------Welcome Back--------------------")
                admin_menu()
                break #the 'break' will break the loop

            else:
                print("\n*Error : Invalid Account")

        elif (opt == "2"):
            return

        else:
            print("\n*Error : Invalid Input")
      
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define is new account or existing account

def type_user():
    while(True):
        print("\n--------------------Patient Account--------------------")
        print("\n1.Create New Account\n2.Login into Existing Account\n3.Back\n")
        user_acc = input("Pls enter the selection : ")

        # if users enter 1, will lead them to do new registration and the patient id will be assigned to them
        if (user_acc == "1"):
            new_user()
            break

        # if users enter 2, will lead them to log in                 
        elif (user_acc == "2"):
            exist_user()
            break

        elif (user_acc == "3"):
            return #STOP THE FUNCTION

        else:
            print("\n*Error : Invalid Input")
            
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a menu for user (what they can do after they login)
        
def user_menu(patientic):
    while (True):
        print("\n1.View Profile\n2.Edit Profile Details\n3.View Available Vaccines\n4.View Vaccination Status\n5.Log Out\n")
        opt = input("Pls enter the selection : ")
        print("")
        
        #link to each of the function
        if (opt == "1"):
            user_info_user(patientic)
            
        elif (opt == "2"):
            edit_profile_menu(patientic)
            
        elif (opt == "3"):
            vaccine_details()
            
        elif (opt == "4"):
            vac_status(patientic)
            
        elif (opt == "5"):
            print("*You have been successfully logged out.")
            break
        
        else:
            print("Invalid Input")



#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a menu for admin(what they can do after they login)

def admin_menu():
    while (True):
        print("\n1.Vaccine Administration\n2.Search Patients Record\n3.Edit the Vaccines\n4.View Statistical Information\n5.Log Out\n")
        opt = input("Pls enter the selection : ")

        #link to each of the function
        if (opt == "1"):
            administration() #record all vaccines administered in vaccination.txt file
            
        elif (opt == "2"):
            user_info_admin() #a menu allows admins to choose either searching patients (one / all)
            
        elif (opt == "3"):
            vaccine_edit() #allow admins to add new vaccines or delete vaccines
        
        elif (opt == "4"):
            statistical_report() #reporting - Statistical Information(VC1/VC2)
            
        elif (opt == "5"):
            print("\n*You have been successfully logged out.")
            break
        
        else:
            print("\n*Error : Invalid Input")
    
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define new user registration

def new_user():
        print("\n--------------------Please register your details--------------------")

        #validation for name
        while(True):
            print("\n*Enter '1' to exit")
            name = input("Please enter your name (only letters are accepted) : ")

            #make sure only alphabet entered
            a = name.isalpha()

            if(name == "1"):
                return

            elif(a == True):
                break

            if(a == False):
                if " " in name:
                    break

                else:
                    print("\n*Error : Invalid Input")
            


        #validation for password
        passw = validation_password()

        #exit the registration function
        if (passw == "1"):
            return
                    
        #validation for IC
        f = open("Patients.txt", "r")
        while (True):
            flag = False
            ic = validation_ic()

            #exit the registration
            if(ic == "1"):
                return
            
            lists = []
            
            for line in f:
                line_split = line.split(",")
                lists.append(line_split) 
            f.close()

            f = open("Patients.txt","r")
            for i in range(len(lists)):
                if (ic) in lists[i][1]:
                    flag = True
                    
            if (flag == True):
                print("\n*Error : IC exists, Please try again")
                continue

            else:
                break
                

                    #return #to stop asking again the gender
            f.close()


        #validation for gender
        while(True):
            print("\n*Enter '1' to exit")
            gender = input("Please enter your gender(m/f) : ").lower()
            if((gender == "m") or (gender == "f") or (gender == "male") or (gender == "female")):
                    break

            elif(gender == "1"):
                return

            else:
                print("\n*Error : Invalid Input either male(m) or female(f)")

        #Address
        print("\n*Enter '1' to exit")
        address = input("Please enter your Current Address : ")

        if(address == "1"):
            return

        #validation for postcode
        postcode = validation_postcode()

        #exit registration
        if(postcode == "1"):
            return

        #validation for vc
        while(True):
            print("\n*Enter '1' to exit")
            vc = input("Please enter the Vaccine Centre where you want to select (vc1/vc2)  : ").upper()

            if(vc == "1"):
                return

            if((vc == "VC1") or (vc == "VC2")):
                break
            else:
                print("\n*Error : Invalid VC")

        #validation for age               
        while(True):

            #avoid user enter string, string cannot be converted to integer, avoid show red error message
            try:
                print("\n*Enter '1' to exit")
                age_int = int(input("Please enter your age (minimum age & maximum age to register is 12 & 100) : "))

                if(age_int == 1):
                    return

                if((age_int > 11) and (age_int < 101)):
                    age_str = str(age_int)
                    break
                
                else:
                    print("\n*Error : Invalid age")
            except:
                print("\n*Error : Invalid Input")


        #validation for email
        email = validation_email()

        #exit registration
        if(email == "1"):
            return

        #valdidation for phone number
        phone_num = validation_phone()
        if(phone_num == "1"):
            return

        #validation for illness
        while(True):
            print("\n*Enter '1' to exit")
            illness = input("Do you have any illnesses (yes/no) : ").lower()

            if(illness == "1"):
                return
            
            if((illness == "yes") or (illness == "no")):
                break
            else:
                print("\n*Error : Invalid Input*")
        
        #validation for allergic
        while(True):
            print("\n*Enter '1' to exit")
            is_allergic = input("Do you have allergic (yes/no) : ").lower()

            if(is_allergic == "1"):
                return

            if((is_allergic == "yes") or (is_allergic == "no")):
                break

            else:
                print("\n*Error : Invalid Input")

        vaccine = vaccine_selection(age_int)
        #user want to exit the registration
        if(vaccine == "1"):
            return
        
        pat_id = id(vc)
        f = open("Patients.txt", "a")
        f.writelines([pat_id,",",ic,",",name,",", passw,",",gender,",", vc,",", address,",", postcode,",", age_str,",", email,",", phone_num,",", illness,",", is_allergic,",",vaccine,"\n"])
        f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for password

def validation_password():
        regex_password = "[0-9a-zA-Z]{6,}"
        
        while (True):
            a = False
            b = False
            print("\n*Enter '1' to exit")
            #Wiil only store the correct password in text file
            passw = input("Please enter your password (at least 6 characters / must contain only alpha and numbers) : ")

            if(passw == "1"):
                return passw

            if(re.search(regex_password,passw)):
                
                #make sure contain alpha and numbers
                makesure_digit = any(char.isdigit() for char in passw)
                makesure_alpha = any(char.isalpha() for char in passw)

                if(makesure_digit == True):
                    a = True

                else:
                    print("\n*Error : Must contain digit")

                if(makesure_alpha == True):
                    b = True

                else:
                    print("\n*Error : Must contain alpha")


                if((a == True) and (b == True)):
                    return passw
                
            else:
                print("\n*Error : minimum 6 characters")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for IC
def validation_ic():
        #Year-Month-Day
        regex_ic = '(([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))-([0-9]{2})-([0-9]{4})'
        

        while(True):
            print("\n*Enter '1' to exit")
            ic = input("Please enter your identity card (YYMMDD-99-9999) : ")

            if(ic == "1"):
                return ic
            
            if (len(ic) == 14):
                    if(re.search(regex_ic,ic)):
                            return ic
                    else:
                            print("\n*Error : Invalid IC")
                            
            else:
                    print("\n*Error : Invalid IC")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for postcode

def validation_postcode():
    while(True):
        print("\n*Enter '1' to exit")
        postcode = input("Please enter your postcode (only 5 numbers can be entered) : ")
        check = postcode.isnumeric()

        if(postcode == "1"):
            return postcode

        if(check == True) and (len(postcode) == 5 ):
            return postcode

        else:
            print("\n*Error : Invalid Postcode")
                        
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for email

def validation_email():   #symbol + = 1 or more  (any) characters
    regex_email = re.compile(r'([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+')

    while(True):
        print("\n*Enter '1' to exit")
        email = input("Please enter your Email : ")

        if(email == "1"):
            return email
        
        if(re.search(regex_email,email)):
            return email

        else:
            print("\n*Error : Invalid email")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Validation for phone number

def validation_phone():
    regex_phone = '^(\+?6?01)[02-46-9][-][0-9]{7}$|^(\+?6?01)[1][-][0-9]{8}$'

    while(True):
        print("\n*Enter '1' to exit")
        phone_num = input("Format : 01Z-XXXXXXX or 011-XXXXXXXX,where Z is 0, 2, 3, 4, 6, 7, 8, 9\nPlease enter your phone number in above format : ")

        if(phone_num == "1"):
            return phone_num
        
        if(re.search(regex_phone,phone_num)):
            return phone_num

        else:
            print("\n*Error : Invalid Phone Number, Please refer to the format")

        
#**************************************************************************************************************************************************************************************        
#DONE BY GAN MING HUI
#Functions for user to edit profile
        
def edit_profile_menu(patientic):
    while (True):
        print("\n--------------------Edit Profile--------------------")
        print("\n1.Password\n2.Address & Postcode\n3.Email\n4.Phone Number\n5.Vaccine\n6.Back\n")

        opt = input("Please Enter the selection : ")
        
        if (opt == "1"):
            edit_password(patientic)
            
        elif (opt == "2"):
            edit_address_postcode(patientic)
            
        elif (opt == "3"):
            edit_email(patientic)
            
        elif (opt == "4"):
            edit_phone_number(patientic)
            
        elif (opt == "5"):
            edit_vaccine(patientic)
            
        elif (opt == "6"):
            break
        
        else:
            print("Invalid Input")   

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Edit phone number

def edit_phone_number(patientic):

    line_number = 0
    access = False

    f = open("Patients.txt","r") 
    lists = []
    for line in f:
        line_split = line.split(",")
        lists.append(line_split)

    #To know the users info in which line
    while (access == False):
        if(lists[line_number][1] == patientic):
            patientid, ic, name, password, gender, vc, address, postcode, age, email, old_phone_number, illness, allergic, vaccine = lists[line_number]#get the old record
            access = True
        else:
            line_number += 1
    f.close()

    print("\n--------------------Edit Phone Number--------------------\n")
    new_phone_number = input("Please enter new phone number : ")
    makesure = input("Do you really want to edit (yes/no) ?\n> ").lower()
    while (True):
        if (makesure == "yes"):
            print("\n--------------------Edited Successfully--------------------")
            print("\n* Phone Number has been edited from", old_phone_number,"to",new_phone_number,"*")

            #To update the ONE new record to the file
            f = open("Patients.txt","a")
            #insert new record but haven deleted old record
            f.writelines([patientid,",",ic,",",name,",", password,",",gender,",", vc,",", address,",", postcode,",", age,",", email,",", new_phone_number,",", illness,",", allergic,",", vaccine])
            f.close()

            #delete old record and write new record into text file
            f = open("Patients.txt","r")  
            lines = f.readlines()
            del lines[line_number]  #the lines contains the latest records(including the record which has been edited)
            f.close()

            f = open("Patients.txt","w") 
            for line in lines:  #write all the latest record into text file
                f.write(line) 
            f.close()
            break
        
        elif (makesure == "no"):
            print("*Nothing has changed*")
            break
        
        else:
            print("Invalid Input")


    
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Edit email
def edit_email(patientic):
    line_number = 0
    access = False

    f = open("Patients.txt","r") 
    lists = []
    for line in f:
        line_split = line.split(",")
        lists.append(line_split)
        
    while (access == False):
        if(lists[line_number][1] == patientic):
            patientid, ic, name, password, gender, vc, address, postcode, age, old_email, phone_number, illness, allergic, vaccine = lists[line_number]#get the old record
            access = True
        else:
            line_number += 1
    f.close()

    print("\n--------------------Edit Email--------------------")
    new_email = input("\nPlease enter new email : ")
    makesure = input("Do you really want to edit (yes/no) ?\n> ").lower()
    while (True):
        if (makesure == "yes"):
            print("\n--------------------Edited Successfully--------------------")
            print("\n* Email has been edited from", old_email,"to",new_email,"*")
            f = open("Patients.txt","a")
            f.writelines([patientid,",",ic,",",name,",", password,",",gender,",", vc,",", address,",", postcode,",", age,",", new_email,",", phone_number,",", illness,",", allergic,",", vaccine])
            f.close()

            f = open("Patients.txt","r")  
            lines = f.readlines()
            del lines[line_number]
            f.close()

            f = open("Patients.txt","w") 
            for line in lines:  
                f.write(line) 
            f.close()
            break
        
        elif (makesure == "no"):
            print("*Nothing has changed*")
            break
        
        else:
            print("Invalid Input")


             
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Edit address_postcode            
def edit_address_postcode(patientic):
    line_number = 0
    access = False

    f = open("Patients.txt","r") 
    lists = []
    for line in f:
        line_split = line.split(",")
        lists.append(line_split)
        
    while (access == False):
        if(lists[line_number][1] == patientic):
            patientid, ic, name, password, gender, vc, old_address, old_postcode, age, email, phone_number, illness, allergic, vaccine = lists[line_number]#get the old record
            access = True
        else:
            line_number += 1
    f.close()

    print("\n--------------------Edit Address & Postcode--------------------")
    new_address = input("\nPlease enter new address : ")
    new_postcode = input("Please enter new postcode : ")
    makesure = input("Do you really want to edit (yes/no) ?\n> ").lower()
    while (True):
        if (makesure == "yes"):
            print("\n--------------------Edited Successfully--------------------")
            print("\n* Address and Postcode has been edited from", old_address,"&",old_postcode,"to",new_address,"&",new_postcode,"*")
            f = open("Patients.txt","a")
            f.writelines([patientid,",",ic,",",name,",", password,",",gender,",", vc,",", new_address,",", new_postcode,",", age,",", email,",", phone_number,",", illness,",", allergic,",", vaccine])
            f.close()

            f = open("Patients.txt","r")  
            lines = f.readlines()
            del lines[line_number]
            f.close()

            f = open("Patients.txt","w") 
            for line in lines:  
                f.write(line) 
            f.close()   
            break
        
        elif (makesure == "no"):
            print("*Nothing has changed*")
            break
        
        else:
            print("Invalid Input")

       
            


#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Edit password
def edit_password(patientic):

    line_number = 0
    access = False

    f = open("Patients.txt","r") 
    lists = []
    for line in f:
        line_split = line.split(",")
        lists.append(line_split)

    #To know the users info in which line
    while (access == False):
        if(lists[line_number][1] == patientic):
            patientid, ic, name, old_password, gender, vc, address, postcode, age, email, phone_number, illness, allergic, vaccine = lists[line_number]#get the old record
            access = True
        else:
            line_number += 1
    f.close()

    print("\n--------------------Edit Password--------------------\n")
    while (True):
        comfirm = input("Please enter old password before edit your password : ")
        if (lists[line_number][3] == comfirm):
            new_password = input("Please enter new password : ")
            makesure = input("Do you really want to edit (yes/no) ?\n> ").lower()
            break
        else:
            print("\n* The password you entered is incorrect. *")
            confirm2 = input("Do you really want to edit your password (yes/no) ? \n>").lower()
            if (confirm2 == "yes"):
                continue
            elif(confirm2 == "no"):
                makesure = "no"
                break
            else:
                print("\n*Error : Invalid Input")
            
    while (True):
        if (makesure == "yes"):
            print("\n--------------------Edited Successfully--------------------")
            print("\n* Password has been edited from", old_password,"to",new_password,"*")
                #To update the new record to the file
            f = open("Patients.txt","a")
            #insert new record but haven deleted old record
            f.writelines([patientid,",",ic,",",name,",", new_password,",",gender,",", vc,",", address,",", postcode,",", age,",", email,",", phone_number,",", illness,",", allergic,",", vaccine])
            f.close()

            #delete old record and write new record into text file
            f = open("Patients.txt","r")  
            lines = f.readlines()
            del lines[line_number]  #the lines contains the latest records(including the record which has been edited)
            f.close()

            f = open("Patients.txt","w") 
            for line in lines:  #write all the latest record into text file
                f.write(line) 
            f.close()
            break
        elif (makesure == "no"):
            print("\n*Nothing has changed*")
            break
        else:
            print("Invalid Input")

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Edit vaccine selection
def edit_vaccine(patientic):

    line_number = 0
    access = False

    f = open("Patients.txt","r") 
    lists = []
    for line in f:
        line_strip = line.strip()
        line_split = line_strip.split(",")
        lists.append(line_split)

    #To know the users info in which line
    while (access == False):
        if(lists[line_number][1] == patientic):
            patientid, ic, name, password, gender, vc, address, postcode, age, email, phone_number, illness, allergic, old_vaccine = lists[line_number]#get the old record
            access = True
        else:
            line_number += 1
    f.close()
    age_int = int(age)
    if(age_int >= 12):
        print("\n--------------------Edit Vaccine Selection--------------------")
        vaccine_details()
        print("")
        new_vaccine = input("Please enter the vaccine you want to change to : ").upper()
    else:
        print("\n* The minimum age to receive the vaccine is 12 *")
        access = False
    while (access == True):
        makesure = input("Do you really want to edit (yes/no) ?\n> ").lower()
        if (makesure == "yes"):
            print("\n--------------------Edited Successfully--------------------\n")
            print("* Vaccine Selection has been edited from", old_vaccine,"to",new_vaccine,"*")
            f = open("Patients.txt","a")
            f.writelines([patientid,",",ic,",",name,",", password,",",gender,",", vc,",", address,",", postcode,",", age,",", email,",", phone_number,",", illness,",", allergic,",", new_vaccine,"\n"])
            f.close()

            f = open("Patients.txt","r")  
            lines = f.readlines()
            del lines[line_number]
            f.close()

            f = open("Patients.txt","w") 
            for line in lines:  
                f.write(line)
            f.close()   
            break
        
        elif (makesure == "no"):
            print("*Nothing has changed*")
            break
        
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function to let the user view the options of vaccines and choose the vaccine they want to receive

def vaccine_selection(age_int):
    access = False

    while (access == False):
        print("\n--------------------Depending on the age of you, the following vaccines are available to you--------------------\n")
        
        #retrieve minimum and maximum age from vaccine.txt text file
        f = open("vaccine.txt","r")
        lists = []
        lists1 = []
        above = True
        n = 0
        a = 1
        for line in f:
            line_strip = line.strip()
            line_split = line_strip.split(",")
            lists.append(line_split)

            #Check which vc meets the age
            #prevent the max age in age group is the word "above"
            try:
                min_age_str = lists[n][3]
                min_age_int = int(min_age_str)
                max_age_str = lists[n][4]
                max_age_int = int(max_age_str)

            except:
                max_age_int = 0

            #Not allow the too young & old people to receive vaccine (12 & 80)
            if(age_int < 18):
                print(f"\n*Notice : Your age is {age_int} and haven reach the minimum age ")
                return("ineligible") 
                
            elif(age_int > 80):
                print(f"\n*Notice : Your age is {age_int} and already reach the maximum age ")
                return("ineligible")      

            #if the patient age greather than minimum age and smaller than maximum age of the vaccine, then print the vaccine details
            if((age_int >= min_age_int) and (age_int <= max_age_int)):
                print(f'{a}.{lists[n][0]} -- {lists[n][1]} | {lists[n][2]} | {lists[n][3]} - {lists[n][4]} age group')
                access = True
                
                #store all the vaccine which available to patient into a list (validation for the selection--make sure selection is within the available vaccine)
                lists1.append(lists[n][0])

                #numbering
                a = a + 1
                
            else:
                above = False


            #print the vaccine available for the word "above"
            if(above == False):
                if((age_int >= min_age_int) and (max_age_int == 0)):
                    print(f'{a}.{lists[n][0]} -- {lists[n][1]} | {lists[n][2]} | {lists[n][3]} - {lists[n][4]} age group')
                    access = True
                    lists1.append(lists[n][0])
                    a = a + 1
                    n = n + 1

                else:
                    n = n + 1
            else:
                n = n + 1
                
        #for age not meet the age group requirement
        if(access == False):
            print(f"\n*Notice : You are not eligible to receive vaccines because your age is only {age_int} ")
            return ("ineligible")

        while(True):
            print("\n*Enter '1' to exit")
            selection = input("Please enter the vaccine code you want to receive (only the VC code is accepted) : ").upper()

            if(selection == "1"):
                return selection

            #import current date time
            import datetime
            vac_date = datetime.date.today()

            #recommendate the patient receive first dose after 10 days registration
            vac_date = vac_date + datetime.timedelta(days= 10)

            #make sure user only select the vaccine which available to him
            if(selection in lists1):
                print(f"\n--------------------Registration Completed You can receive your {selection} vaccination on {vac_date}--------------------")
                return selection
            else:
                print("\n*Error : Invalid Input")
                              
        f.close()
        
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define Giving Patient ID

def id(vc):
    if (vc == "VC1"):
        #CALL THE LINE FUNCTION AND ASSIGN THE VALUE OF LINE TO VARIABLE NUM1
        num1 = line(vc)
        print(f"\nPatient ID of the patient is : VC1-{num1}")
        print("*You Can Start To Login Into Your Account")
        pat_id = (f"VC1-{num1}")
        #RETURN THE PATIENT ID TO THE id()FUNCTION
        return pat_id

    elif (vc == "VC2"):
        #CALL THE LINE FUNCTION AND ASSIGN THE VALUE OF LINE TO VARIABLE NUM2
        num2 = line(vc)
        print(f"\nPatient ID of the patient is : VC2-{num2}")
        print("*You Can Start To Login Into Your Account")
        pat_id = (f"VC2-{num2}")
        #RETURN THE PATIENT ID TO THE id()FUNCTION
        return pat_id
    
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define login access(all registered patietns)

def exist_user():
    access1 = False
    access2 = False
    a = False
    b = False
    
    while (access1 == False):
        print("\n--------------------Please login to your personal account--------------------")


        #login ic
        print("\n*Enter '1' to exit")
        ic = input("Please enter your IC : ")
        
        #exit login
        if(ic == "1"):
            return

        #login password
        print("\n*Enter '1' to exit")
        passw = input("Please enter your password : ")

        #exit login
        if(passw == "1"):
            return
        
        i = 0
        f = open("Patients.txt", "r")
        list1 = []
        for line in f:
            line_strip = line.strip()
            line_split = line_strip.split(",")
            list1.append(line_split)

            #matching the user input with the text file
            if((list1[i][1] == ic) and (list1[i][3] == passw)):
                print("\n--------------------Login Successfully--------------------")
                print("\n--------------------Welcome Back--------------------")
                user_menu(ic) #successfully enter into the acc
                access1 = True #avoid enter the first WHILE LOOP again / avoid enter the second WHILE Loop
                break #break the for loop
                
                            
            elif((list1[i][1] != ic) or (list1[i][3] != passw)):
                i+=1

            else:
                #PREVENT INVALID INPUT
                access1 = False
                access2 = False
                        
        #ask whether want to continue login if the login is failed
        if(access1 == False):
            print("\n*Error : Invalid Account")

            while (access2 == False):
                again = input("Do you still want to login (yes/no) : ").lower()  #MAKE SURE THE INPUT IS ALL LOWER CASE
                if (again == "yes"):
                    break

                elif (again == "no"):
                    access1 = True
                    break

                else:
                    print("\n*Error : Invalid Input")
                    
        f.close()
        

                
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define counting number of lines in the text file where vc1/vc2 exists
#This is used when giving the patient id, Whenever we start the program,
#the program will add 1 to give the next patient id according to how many patients there are in each vc in the text file                

def line(vc):
    f = open("Patients.txt","r")
    count1 = 101
    for line in f:
        if line.startswith(vc):
            count1 = count1 + 1
    f.close()
    return count1

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function for admin to know each person before they search for particular patient

def name_list():
    f = open("Patients.txt","r")
    print("\n--------------------Patient list--------------------")
    a = 1
    for line in f:
        patientid, ic, name, password, gender, vc, address, postcode, age, email, phonenumber, illness, allergic, vaccine = line.split(",")
        print(f"\n{a}. Name:",name, "\nID :",patientid)
        a = a + 1
    f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function for admin to look user information either search desired patient or show all patients
#COMBINE one_user_info_admin() & all_user_info_admin()

def user_info_admin():
    while (True):
        print("\n--------------------Patient Record--------------------")
        print("\n1.Search a patient\n2.All patients\n3.Back\n")

        opt = input("Pls enter the selection : ")
        if (opt == "1"):
            name_list()
            #-- a function to let admin view all the patient and name
            patient_id = one_user_info_admin()
            if(patient_id == "1"):
                return

        elif (opt == "2"):
            all_user_info_admin()

        elif (opt == "3"):
            break

        else:
            print("Invalid Input")



#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function for admin to view particular user information by key in the patient id

def one_user_info_admin():
    f = open("Patients.txt","r")
    print("\n*Enter '1' to exit")
    patient_id = input("Please Enter the Patient ID : ").upper()

    if(patient_id == "1"):
        return patient_id

    #link to user_info for user
    flag = True
    for line in f:

        #SHOW THE USER INFO IF AND ONLY IF THE PATIENT ID EXIST IN TEXT FILE
        if patient_id in line:

            #Giving a variable to the data in text file in order
            patientid, ic, name, password, gender, vc, address, postcode, age, email, phonenumber, illness, allergic, vaccine = line.split(",")
            print("\n--------------------This is the Personal Details of Patient", patient_id,"--------------------\n")
            print(": Patient ID\t: ", patientid)
            print(": IC\t\t: ", ic)
            print(": Name\t\t: ", name)
            print(": Gender(m/f)\t: ", gender)
            print(": VC(vc1/vc2)\t: ", vc)
            print(": Address\t: ", address)
            print(": Postcode\t: ", postcode)
            print(": Age\t\t: ", age)
            print(": Email\t\t: ", email)
            print(": Phone Number\t: ", phonenumber)
            print(": Illness\t: ", illness)
            print(": Allergic\t: ", allergic)
            print(": Vaccine\t: ", vaccine)
            flag = False

            vac_status_admin(patient_id)


    if (flag == True):
            print("\n*Error : The patient id cannot be found")

    f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function for admin to view all users information

def all_user_info_admin():
    count = 0 
    f = open("Patients.txt","r")
    for line in f:
        count = count + 1 #INCREMENT -- Will show all the patients info one by one
        print("\n--------------------This is the Personal Details of Patient", count,"--------------------\n")
        #Givin a variable to the data in text file in order
        patient_id, ic, name, password, gender, vc, address, postcode, age, email, phonenumber, illness, allergic, vaccine = line.split(",")
        print(": Patient ID\t: ", patient_id)
        print(": IC\t\t: ", ic)
        print(": Name\t\t: ", name)
        print(": Gender(m/f)\t: ", gender)
        print(": VC(vc1/vc2)\t: ", vc)
        print(": Address\t: ", address)
        print(": Postcode\t: ", postcode)
        print(": Age\t\t: ", age)
        print(": Email\t\t: ", email)
        print(": Phone Number\t: ", phonenumber)
        print(": Illness\t: ", illness)
        print(": Allergic\t: ", allergic)
        print(" ")
        #add on what vc the patient take + vc date....

        vac_status_admin(patient_id)
    f.close()            
    

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a function for users to view their personal information after they login

def user_info_user(patient_id): #get the patient id from other function
    f = open("Patients.txt","r")
    
    #loop every line in text file, will get the patient details when patient id exist in any of the line
    for line in f:
        if patient_id in line:
            #Divide the data of a record in the text file into their respective variables
            patientid, ic, name, password, gender, vc, address, postcode, age, email, phonenumber, illness, allergic, vaccine = line.split(",")
            print("\n--------------------Personal Details--------------------\n")
            print(": Patient ID\t: ", patientid)
            print(": IC\t\t: ", ic)
            print(": Name\t\t: ", name)
            print(": Gender(m/f)\t: ", gender)
            print(": VC(vc1/vc2)\t: ", vc)
            print(": Address\t: ", address)
            print(": Postcode\t: ", postcode)
            print(": Age\t\t: ", age)
            print(": Email\t\t: ", email)
            print(": Phone Number\t: ", phonenumber)
            print(": Illness\t: ", illness)
            print(": Allergic\t: ", allergic)
            print(": Vaccine\t: ", vaccine)
    f.close()
            
    
    


#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Define a main menu for the system
                        
def menu():
    print("\n--------------------Malaysia Vaccination System--------------------")
    print("\nWelcome Back :D\n")
    print("Do you want to enter as ? : \n")
    print("1.Patient\n2.Admin\n3.Close")
    selection = input("\nPls enter the selection (1-3) : ")

    if(selection == "1"):
        type_user() #USER LOGIN / REGISTER
    elif(selection == "2"):
        admin_acc() #ADMIN LOGIN
    elif(selection == "3"):
        exit() #STOP ENTIRE PROGRAM
    else:
        print("\nError : Invalid Input")

#4.Statistical Information on Patients Vaccinated
#a.(reporting part- print the total number of the patients according to their center)
#b.The program should have option to print the total number of patients vaccinated by each VC. （从总数分出来已经打了疫苗的）
#c.These numbers should be broken down into people who are waiting for dose 2 and people who have completed vaccination. (再从已经打了疫苗的病人里，分出谁是打完dose2的,和谁是等dose2的）

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#a.print the total number of the patients according to their center
def statistical_report():
    flag = True
    while(flag == True):
        #Show a menu
        print("\n--------------------Statistical Information-------------------")
        print("\n1.View Statistical Report\n2.Back\n")
        opt = input("Please enter the selection : ")

        #Choose the VC
        while(True):
            if(opt == "1"):
                print("\n--------------------View Statistical Report-------------------")
                print("\n1.Ststistics VC1\n2.Statistics VC2\n3.Back\n")
                selection = input("Please enter the selection : ")

                #VC1
                if(selection == "1"):
                    vc = "VC1"
                    vc_menu(vc)                   

                #VC2
                elif(selection == "2"):
                    vc = "VC2"
                    vc_menu(vc)
                    
                #Back to choose vc menu
                elif(selection == "3"):
                    break

                else:
                    print("\n*Error : Invalid Input")

            #Back to admin main menu
            elif(opt == "2"):
                flag = False
                break

            else:
                print("\n*Error : Invalid Input")
                break


#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#define a menu for vc statistics report

def vc_menu(vc):
    if(vc == "VC1"):
        print("\n--------------------VC1 Statistics Report-------------------")
        total_patients(vc)
        vaccinated(vc)
        wait_dose2(vc)
        completed(vc)
        

    elif(vc == "VC2"):
        print("\n--------------------VC2 Statistics Report-------------------")
        total_patients(vc)
        vaccinated(vc)
        wait_dose2(vc)
        completed(vc)
        


#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#a.define a menu to print total number of patients in vc  

def total_patients(vc):
    #Total Patients
    count = 0
    f = open("Patients.txt","r")
    for line in f:
        if line.startswith(vc):
            count = count + 1
    print("\nTotal Number of Patients\t\t\t: ", count)
    f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#b.print the total number of patients vaccinated.

def vaccinated(vc):
    #Patients Vaccinated
    count = 0
    f = open("vaccination.txt","r")
    for line in f:
        if ((line.startswith(vc)) and ("dose" in line)):
            count = count + 1
    print("\nTotal Number of Vaccinated Patients\t\t: ", count)
    f.close()
        
#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#c.print the total number of who are waiting for dose 2

def wait_dose2(vc):
    #Patients Waiting Dose 2
    count = 0
    f = open("vaccination.txt","r")
    for line in f:
        if ((line.startswith(vc)) and ("dose1" in line)):
            count = count + 1
    print("\nTotal Number of Patients who Waiting for Dose 2 : ", count)
    f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#d.print the total number of who have completed vaccine

def completed(vc):
    #Patients Complete Vaccine
    count = 0
    f = open("vaccination.txt","r")
    for line in f:
        if ((line.startswith(vc)) and ("dose2" in line)):
            count = count + 1
    print("\nTotal Number of Patients who have finished receiving all doses  : ", count)
    f.close()



#**************************************************************************************************************************************************************************************
#DYANIEL PART

'''
Vaccine Admistration
done by: dyaniel
'''
'''MAKE SURE KEY IN VALID PATIENT ID'''
def checking_id():
    print("\n*Enter '1' to exit")
    id =  input('Pls enter patient id: ').upper()
    if(id == "1"):
        return id
    
    f = open('Patients.txt', 'r')
    flag = False

    # check patient id
    for check in f:
        if (check.startswith(id)):
            flag = True
            break

    #Invalid patient id
    if (flag == False):
        print('Invalid patient id, pls re-submit.\n')
        id = checking_id()
    return id
    f.close()

'''DETERMINE PATIENT AGE'''
def checking_age(id):
    f = open('Patients.txt','r')
    #get patient's age
    for check in f:
        if (check.startswith(id)):
            ID,ic,nm,password,gender,VC,add,pc,age,email,no_ph,date_dose1,date_dose2,vaccine_code = check.split(',')

    return age
    f.close()


'''VACCINE APPROVEMENT ACCORDING AGE'''
def approve(type, age):
    age = int(age)
    #display AF or DM vaccine error
    if (type == 'AF'or type == 'DM'):
        if (age < 12) :
            print('\nThis patient is not suitable for having this dosage')
            flag = False
        else:
            flag = True

    #display BV or EC vaccine error
    elif (type == 'BV' or type == 'EC'):
        if (age <18) :
            print('\nThis patient is not suitable for having this dosage.')
            flag = False
        else:
            flag = True

    # display CZ vaccine error
    elif (type == 'CZ'):
        if (age <12 or age >45):
            print('\nThis patient is not suitable for having this dosage.')
            flag = False
        else:
            flag = True

     # error display + back to start
    else:
        flag = False
        print('\nInvalid vaccine code, pls re-submit.\n')
        administration()

    return flag


'''MAKE SURE DOSE1 SAME WITH DOSE CHOSEN BY PATIENT'''
def check_dose1(vac_code,id):
    vac_code = vac_code+'\n'
    f = open('Patients.txt', 'r')

    # get vaccine code chosen by patient
    for check in f:
        if (check.startswith(id)):
            ID,ic,nm,password,gender,VC,add,pc,age,email,no_ph,date_dose1,date_dose2,vaccine_code = check.split(',')

    # vaccine code key in same with vaccine code chosen by patient
    if (vac_code == vaccine_code) :
        check_dose1_approve = True

    # vaccine code key in different with vaccine code chosen by patient
    else:
        print(f'The vaccine code key in is different with the vaccine code chosen by patient. Patient choose {vaccine_code} vaccine.\nPls re-submit\n')
        check_dose1_approve = False

    return check_dose1_approve
    f.close()


'''CONFIRM PATIENT REACH SECOND DOSE DATE '''
def check_2nd_dose_date(id):
    f = open('vaccination.txt', 'r')

    # set date of on day
    import datetime
    vac_date = datetime.datetime.today()
    #for testing second dose date arrive
    vac_date = vac_date + datetime.timedelta(days= 35)

    #find second dose date from vaccination.txt
    for check in f:
        if (id in check):
            id,dose,code,date,date1,date2 = check.split(',')
            date =datetime.datetime.strptime(date,'%Y-%m-%d')

            #date reach
            if (vac_date > date):
                flag = True
                break

            #date haven't reach
            else:
                print(f"\nThe second dose date of patient haven't reach, patient cannot have second dose today.\nSecond dose date is {date}")
                flag = False
                break

    return flag
    f.close()


'''MAKE SURE DOSE1 SAME WITH DOSE2'''
def check_dose2(dose2_code,id):
    f = open('vaccination.txt','r')

    # find first dose code from vaccination.txt
    for check in f:
        if (id in check):
            id,dose,code,date,date1,date2 = check.split(',')

            #dose1 = dose2
            if (dose2_code == code):
                check_dose2_approve = True
                break

            # dose1 = EC
            elif(code == 'EC'):
                print('\nThis patient is having EC vaccine, no need have second dose.')
                check_dose2_approve = None
                break

            #dose1 not= dose2
            else:
                check_dose2_approve = False
                print(f"\nPatient's dose 2 type vaccine is different with dose 1. Patient's dose1 vaccine code is {code}\nPls re-submit\n")
                break

    return check_dose2_approve
    f.close()


'''DOSE1 STEP'''
def dose1_step(id,code):
    f = open('vaccination.txt','a+')

    #set date of on day
    import datetime
    vac_date = datetime.date.today()

    #write patient data into text file + calculate date of next dose
    #AF vaccine set
    if (code == 'AF'):
        next_dose = vac_date + datetime.timedelta(days = 14)
        f.write(f'{id},dose1,{code},{next_dose},{vac_date},NONE\n')
        print('\nSubmit Successfully')
        print(f'Second dose date: {next_dose}')

    #BV or CZ vaccine set
    elif (code == 'BV' or code == 'CZ'):
        next_dose = vac_date + datetime.timedelta(days=21)
        f.write(f'{id},dose1,{code},{next_dose},{vac_date},NONE\n')
        print('\nSubmit Successfully')
        print(f'Second dose date: {next_dose}')

    #DM vaccine set
    elif (code == 'DM'):
        next_dose = vac_date + datetime.timedelta(days=28)
        f.write(f'{id},dose1,{code},{next_dose},{vac_date},NONE\n')
        print('\nSubmit Successfully')
        print(f'Second dose date: {next_dose}')

    #EC vaccine set
    elif (code == 'EC'):
        f.write(f'{id},dose1,{code},NONE,{vac_date},NONE\n')
        print('\nSubmit Successfully')
        print('patient get EC vaccine no need has second dose.')

    f.close()



'''DOSE2 STEP'''
def dose2_step(id,code):
    #set current date
    import datetime
    vac_date = datetime.date.today()
    vac_date = vac_date + datetime.timedelta(days= 35)
    vac_date = vac_date.strftime('%Y-%m-%d')

   #take 1st dose date from vaccination.txt
    f = open('vaccination.txt','r')
    for check in f:
        if (id in check):
            id,dose,code,date,date1,date2 = check.split(',')
    f.close()

    # count the line of patient id
    f = open('vaccination.txt', 'r')
    count = 0
    for line in f :
        count += 1
        if id in line :
            break
    f.close()

    #change the dose status of patient in list
    f = open('vaccination.txt','r')
    lines = f.readlines()
    lines[count-1] = id + ',dose2,'+ code+',NONE,'+date1+','+vac_date+'\n'
    f.close()

    #write back the list that change into text file
    f = open('vaccination.txt', 'w')
    for rewrite in lines:
        f.write(rewrite)

    print('\nSubmit Successfully')
    print('#All the doses are completed!')



#administration(main)
def administration():
    #user input
    patient_id = checking_id()
    if(patient_id == "1"):
        return

    while(True):
        print("\n*Enter '1' to exit")
        dosage_done = input('Pls enter the dosage that patient get today (dose1 / dose2) : ')
        if(dosage_done == "1"):
            return
        
        if((dosage_done == "dose1") or (dosage_done == "dose2")):
            break
        else:
            print("\n*Error : Invalid dosage number*")
            
    print("\n*Enter '1' to exit")       
    
    vaccine_details()
    
    vac_code = input('\nPls enter the vaccine code of patient : ').upper()
    if(vac_code == "1"):
        return
    vac_code = vac_code.upper()

    #manual key in patient's age
    #age = int(input('age :'))

    #read patient's age from registration.txt
    age = checking_age(patient_id)
    approve_status = approve(vac_code, age)

    #determine dosage_done
    if (approve_status == True):

        #INPUT DOSE2
        if (dosage_done == 'dose2'):
            flag = True
            f = open('vaccination.txt','r')

            #find patient column from vaccination.txt
            for check in f:
                if (check.startswith(patient_id)):
                    if ('dose1' in check):

                        #dose1 = EC
                        if(vac_code == 'EC'):
                            print('\nEC vaccine, no need have second dose.')
                            flag = False
                            break

                        #DOSE2 FLOW
                        else:
                            flag = False
                            check_dose2_approve = check_dose2(vac_code, patient_id)

                            #confirm dose1 = dose2
                            if (check_dose2_approve == True):
                                date_approve = check_2nd_dose_date(patient_id)

                                #confirm 2nd dose date reach
                                if (date_approve == True):
                                    dose2_step(patient_id,vac_code)
                                    break

                            #confirm dose1 not= dose2 + back to start
                            elif (check_dose2_approve == False):
                                administration()

                            #for dose1 = EC
                            else:
                                break

                    #patient done second dose
                    else:
                        print('\nThis patient has done second dose!')
                        flag = False
                        break

            #Switch to DOSE1 FLOW
            if flag == True:
                print('\nThis patient no having the first dose yet.\nSystem will set patient in dose 1 status.')
                check_dose1_approve = check_dose1(vac_code, patient_id)

                # confirm dose1 = dose chosen by patient
                if (check_dose1_approve == True):
                    dose1_step(patient_id,vac_code)

                # dose1 key in different with dose chosen by patient
                else:
                    administration()
            f.close()

        #INPUT DOSE1
        elif (dosage_done == 'dose1'):
            flag = True
            f = open('vaccination.txt', 'r')

            # find patient column from vaccination.txt
            for check in f:
                if (check.startswith(patient_id)):
                    if ('dose1' in check):

                        # dose1 = EC
                        if (vac_code == 'EC'):
                            print('\nThis patient is having EC vaccine, no need have second dose.')
                            flag = False
                            break

                        # Switch to DOSE2 FLOW
                        print('\nThis patient has done first dose.\nSystem will set patient in dose2 status')
                        flag = False
                        check_dose_approve = check_dose2(vac_code, patient_id)

                        # confirm dose1 = dose2
                        if check_dose_approve == True:
                            date_approve = check_2nd_dose_date(patient_id)

                            # confirm 2nd dose date reach
                            if (date_approve == True):
                                dose2_step(patient_id, vac_code)
                                break

                        # confirm dose1 not= dose2 + back to start
                        elif (check_dose_approve == False):
                            administration()

                        # for dose1 = EC
                        else:
                            break

                    # patient done second dose
                    else:
                        print('\nThis patient has done second dose!')
                        flag = False
                        break

            #DOSE1 FLOW
            if flag == True:
                check_dose1_approve = check_dose1(vac_code, patient_id)

                # confirm dose1 key in = dose chosen by patient
                if (check_dose1_approve == True):
                    dose1_step(patient_id, vac_code)

                #dose1 key in different with dose chosen by patient
                else:
                    administration()
            f.close()

#**************************************************************************************************************************************************************************************
#DONE BY HO FENG SHENG

def vac_status(patientic):
    flag = False
    f = open("Patients.txt","r")
    for line in f:
        if (patientic) in line:
            patientid, ic, name, password, gender, vc, address, postcode, age, email, phonenumber, illness, allergic, vaccine = line.split(",")
            patient_id = patientid
    f.close()    
    
    f = open("vaccination.txt", "r")
    for i in f:
        if i.startswith(patient_id):
            i = i.replace("\n","").split(",")
            flag = True
            if i[2] == 'AF'or i[2] == 'BV'or i[2] =='CZ'or i[2] =='DM':
                print("Vaccination Code :" + i[2])
                if i[1] == 'dose1':
                    print("Dose 1 status             :Completed")
                    print("Dose 1 completed date     :"+i[4])
                elif i[1] == 'dose2':
                    print("Dose 1 status             :Completed")
                    print("Dose 1 completed date     :"+i[4])
                if i[3]=='NONE':
                    print("Dose 2 status             :Completed")
                    print("Dose 2 completed date     :"+i[5])
                else:
                    print("Dose 2 status             :Incompleted")
                    print("Suggested for Dose 2 date :"+i[3])
            elif i[2] == 'EC':
                print("Vaccination Code :" + i[2])
                print("Dose 1 status             :Completed")
                print("Dose 1 completed date     :"+i[4])
                print("Dose 2 status             :Only for one dose")
    f.close()
    if flag == False:
        #print("Invalid Patient ID")
        f = open("Patients.txt","r")
        flag2 = False
        for i in f :
            if i.startswith(patient_id):
                flag2 = True
                ID,ic,nm,password,gender,VC,add,pc,age,email,no_ph,date_dose1,date_dose2,vaccine_code = i.replace("\n","").split(',')
                print("Vaccination Code :" + vaccine_code)
                print("Dose 1 status             :Incompleted")
                print("Dose 2 status             :Incompleted")
                
        if flag2 == False:
            print("Invalid patient id")

        f.close()

#**************************************************************************************************************************************************************************************
#DONE BY HO FENG SHENG
def vac_status_admin(patient_id):

    flag = False
    f = open("vaccination.txt", "r")
    for i in f:
        if i.startswith(patient_id):
            i = i.replace("\n","").split(",")
            flag = True
            if i[2] == 'AF'or i[2] == 'BV'or i[2] =='CZ'or i[2] =='DM':
                print("Vaccination Code :" + i[2])
                if i[1] == 'dose1':
                    print("Dose 1 status             :Completed")
                    print("Dose 1 completed date     :"+i[4])
                elif i[1] == 'dose2':
                    print("Dose 1 status             :Completed")
                    print("Dose 1 completed date     :"+i[4])
                if i[3]=='NONE':
                    print("Dose 2 status             :Completed")
                    print("Dose 2 completed date     :"+i[5])
                else:
                    print("Dose 2 status             :Incompleted")
                    print("Suggested for Dose 2 date :"+i[3])
            elif i[2] == 'EC':
                print("Vaccination Code :" + i[2])
                print("Dose 1 status             :Completed")
                print("Dose 1 completed date     :"+i[4])
                print("Dose 2 status             :Only for one dose")
    f.close()
    if flag == False:
        #print("Invalid Patient ID")
        f = open("Patients.txt","r")
        flag2 = False
        for i in f :
            if i.startswith(patient_id):
                flag2 = True
                ID,ic,nm,password,gender,VC,add,pc,age,email,no_ph,date_dose1,date_dose2,vaccine_code = i.replace("\n","").split(',')
                print("Vaccination Code :" + vaccine_code)
                print("Dose 1 status             :Incompleted")
                print("Dose 2 status             :Incompleted")
                
        if flag2 == False:
            print("Invalid patient id")

        f.close()

#**************************************************************************************************************************************************************************************
#DONE BY GAN MING HUI
#Main Program
import re #import regular expression              

flag = True
while (flag):
    menu()

