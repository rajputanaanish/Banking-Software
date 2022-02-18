#Created by: Python Viewer
#file handaling Project
#Banking
def print_menu():
    print("1. Create Account")
    print("2. print All Account Details")
    print("3. Remove Account")
    print("4. Detils of Account Holder")
    print("5. Edit Account")
    print("6. save Account in File")
    print("7. Load Account From File")
    print("8. Quit")
def add_account(arr):
    nm=input("Enter Name:")
    ph=input("Enter Phone:")
    account=input("Enter Account number:")
    balance=int(input("Enter Balance:"))
    L1=[nm,ph,account,balance]
    if(account in arr):
        print("account already exist")
    else:
        arr[account]=L1
    print("inserted sucessfully")
def all_account(arr):
    for x in arr:
        print(x,":",arr[x])
def remove_account(arr):
    account=input("Enter Account number:")
    arr.pop(account)
    print("deleted sucessfully")
def details_account(arr):
    account=input("Enter Account number:")
    if(account not in arr):
        print("account does not exist")
    else:
        print(arr[account])
        print("fetch sucessfully")
def edit_account(arr):
    account=input("Enter Account number:")
    print("Press")
    print("1. name change")
    print("2. phone number change")
    print("3. balance change")
    n1=int(input())
    if(n1==1):
        nm=input("Enter Name:")
        arr[account][0]=nm
    elif(n1==2):
        ph=input("Enter Phone:")
        arr[account][1]=ph
    elif(n1==3):
        print("1->creadit,2->debit:")
        n2=int(input())
    if(n2==1):
        balance=int(input("Enter Balance:"))
        arr[account][3]=arr[account][3]+balance
    if(n2==2):
        balance=int(input("Enter Balance:"))
        arr[account][3]=arr[account][3]-balance
        print("updated sucessfully")
def save_account(arr):
    p=open("abc.txt","a")
    for x in arr.keys():
        p.write("id:"+str(x)+" Details:"+str(arr[x])+"\n")
        #print ("id:",x,"\tDetails:",arr[x])
        p.close()
        arr.clear()
def load_account(arr):
    p=open("abc.txt","r")
    s1=p.read()
    print(s1)
    p.close()
#main function here
account_list={}
print_menu()#once execute
while(True):
    #repeate
    x=int(input("type a number in b/w (1-7)"))
    if (x==1):
        add_account(account_list)
    elif (x==2):
        all_account(account_list)
    elif (x==3):
        remove_account(account_list)
    elif (x==4):
        details_account(account_list)
    elif (x==5):
        edit_account(account_list)
    elif (x==6):
        save_account(account_list)
    elif (x==7):
        load_account(account_list)
    elif (x==8):
        break
    else:
        print("wrong choice")
