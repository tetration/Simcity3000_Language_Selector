## Text menu in Python
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Menu Option 1"
    print "2. Menu Option 2"
    print "3. Menu Option 3"
    print "4. Menu Option 4"
    print "5. Exit"
    print 67 * "-"
  
loop=True      

def mainmenu():  
    while loop:          ## While loop which will keep going until loop = False
        print_menu()    ## Displays menu
        choice = input("Enter your choice [1-12]: ")
         
        if choice==1:     
            print "Menu 1 has been selected"
            ## You can add your code or functions here
        elif choice==2:
            print "Menu 2 has been selected"
            ## You can add your code or functions here
        elif choice==3:
            print "Menu 3 has been selected"
            ## You can add your code or functions here
        elif choice==4:
            print "Menu 4 has been selected"
            ## You can add your code or functions here
        elif choice==5:
            print "Menu 5 has been selected"
            ## You can add your code or functions here
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            raw_input("ERROR: Wrong Please choose an option between 1 to 12")
