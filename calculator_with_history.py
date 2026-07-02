#making a calculator
HISTORY_FILE="history.txt"

def show_history():
    file =open(HISTORY_FILE,'r')
    lines=file.redlines()
    if len(lines)==0:
        print("no history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file =open(HISTORY_FILE,'w')
    file.close()
    print('History cleared')

def save_to_history(equation,result):
    file = open(HISTORY_FILE,'a')
    file.write(equation +"=" +str(result) +"\n")
    file.close()

def calculate(user_input):
    parts =user_input.split()
    if len(parts)!=3:
        print('invlid input.Use format : number operator number (e.g 8+8)')
        return
    num1= float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    if op=="+":
        result =num1+num2
    elif op =="-":
        result=num1 -num2
    elif op=="*":
        result = num1*num2   
    elif op=="/":
        if num2==0:
            print('cannot divide by zero ')
            return
        result =num1/num2
    else:
        print('Invalid opertor. USE ONLY + - * / .')
        return    
    if int(result)==result:
        result = int(result)
    print("result :",result)
    save_to_history(user_input,result)
def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input=input("enter calculation(+ - * /) or command (history, clear or exit)")      
        if user_input=='exit':
         print('good bye')
         break
        elif user_input=='history':
            show_history()
        else:
            calculate(user_input)    
