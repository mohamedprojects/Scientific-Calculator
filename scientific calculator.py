from math import *
import tkinter as tk
expression = "" # EXPRESSION
π = 3.141592654 # Pi number
################################### functions ######################################
# Function to add in the entry of text display
def btn_click(item, equation):
 
    global expression
    expression = expression + str(item)
    equation.set(expression)
# Function to calculate the percentage of a number
def percentage( equation):
 
    global expression
    expression = expression + "/100"
    equation.set(expression)
# Function to delete one by one from the last in the entry of text display
def delete(equation):
    global expression
    text = expression[:-1]
    expression = text
    equation.set(text)
# Function to calculate the factorial of a number    
def btn_fact( equation):
 
    global expression
    expression = expression + "factorial("
    equation.set(expression)
# Function to calculate ln    
def btn_ln( equation):
 
    global expression
    expression = expression + "log1p("
    equation.set(expression)
# Function to calculate the power
def btn_power(equation):
 
    global expression
    expression = expression + "**"
    equation.set(expression)
# Function to calculate log
def btn_log( equation):
 
    global expression
    expression = expression + "log10("
    equation.set(expression)
# Function to find the square root of a number
def btn_sqrt( equation):
 
    global expression
    expression = expression + "sqrt("
    equation.set(expression)   
def btn_pi( equation):
 
    global expression
    expression = expression + str("π")
    equation.set(expression)
# Function to clear the whole entry of text display
def btn_clear(equation):
 
    global expression
    expression = ""
    equation.set("")
# uses whatever is stored in memory_recall
def answer(equation):
    global expression
    global result
    answer= str(result)
    expression = expression + answer
    equation.set(expression)
# Funtion to find the result of an operation       
def btn_equal(equation):
 
    global expression
    global result
    result = str(eval(expression))  # 'eval' function evalutes the string expression directly
    equation.set(result)
    expression = ""
expression = ""
def main():
    # creating basic window
    f = tk.Tk()
    f.title("Scientific Calculator")
    # 'StringVar()' is used to get the instance of input field
    equation = tk.StringVar()
    # creating a frame for the input field
    input_field = tk.Entry(f, textvariable=equation).grid(row=0, ipadx=150, ipady=10, columnspan=9)
    equation.set("0")
    # first row
    exp = tk.Button(f, text=' e ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("exp(", equation), height=2, width=7).grid(row=1, column=0)
    pi = tk.Button(f, text=' π ', fg='black', bg='#87927e', 
                     command=lambda: btn_pi( equation), height=2, width=7).grid(row=1, column=1)
    fac = tk.Button(f, text=' x! ', fg='black', bg='#87927e', 
                     command=lambda: btn_fact( equation), height=2, width=7).grid(row=1, column=2)
    left_brack = tk.Button(f, text=' ( ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("(", equation), height=2, width=7).grid(row=1, column=3)
    right_brack = tk.Button(f, text=' ) ', fg='black', bg='#87927e', 
                     command=lambda: btn_click(")", equation), height=2, width=7).grid(row=1, column=4)
    pour = tk.Button(f, text=' % ', fg='black', bg='#87927e', 
                     command=lambda: percentage( equation), height=2, width=7).grid(row=1, column=5)
    AC = tk.Button(f, text=' AC ', fg='black', bg='#87927e', 
                     command=lambda: btn_clear(equation), height=2, width=7).grid(row=1, column=6)
    # second row
    arcsin = tk.Button(f, text=' arcsin ', fg='black', bg='#87927e', 
                     command=lambda: btn_click('asin(', equation), height=2, width=7).grid(row=2, column=0)
    
    sin = tk.Button(f, text=' sin ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("sin(", equation), height=2, width=7).grid(row=2, column=1)
    ln = tk.Button(f, text=' ln ', fg='black', bg='#87927e', 
                     command=lambda: btn_ln( equation), height=2, width=7).grid(row=2, column=2)
    seven = tk.Button(f, text=' 7 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(7, equation), height=2, width=7).grid(row=2, column=3) 
  
    eight = tk.Button(f, text=' 8 ', fg='black', bg='#e6f6df', 
                     command=lambda:btn_click(8, equation), height=2, width=7).grid(row=2, column=4) 
  
    nine = tk.Button(f, text=' 9 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(9, equation), height=2, width=7).grid(row=2, column=5)
    divide = tk.Button(f, text=' / ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("/", equation), height=2, width=7).grid(row=2, column=6)
    
    # third row
    arccos = tk.Button(f, text=' arccos ',fg='black', bg='#87927e', 
                     command=lambda: btn_click('acos(', equation),height=2, width=7).grid(row=3, column=0)
    cos = tk.Button(f, text=' cos ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("cos(", equation), height=2, width=7).grid(row=3, column=1)
    log = tk.Button(f, text=' log ', fg='black', bg='#87927e', 
                     command=lambda: btn_log( equation), height=2, width=7).grid(row=3, column=2)
    four = tk.Button(f, text=' 4 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(4, equation), height=2, width=7).grid(row=3, column=3)
    five = tk.Button(f, text=' 5 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(5, equation), height=2, width=7).grid(row=3, column=4) 
  
    six = tk.Button(f, text=' 6 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(6, equation), height=2, width=7).grid(row=3, column=5)
    multiply = tk.Button(f, text=' * ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("*", equation), height=2, width=7).grid(row=3, column=6)
    # fourth row
    arctan = tk.Button(f, text=' arctan ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("atan(", equation), height=2, width=7).grid(row=4, column=0)
    tang = tk.Button(f, text=' tan ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("tan(", equation), height=2, width=7).grid(row=4, column=1)
    rac = tk.Button(f, text=' √ ', fg='black', bg='#87927e', 
                     command=lambda: btn_sqrt( equation), height=2, width=7).grid(row=4, column=2)
    one = tk.Button(f, text=' 1 ', fg='black', bg='#e6f6df', cursor ="hand2",
                     command=lambda: btn_click(1, equation), height=2, width=7).grid(row=4, column=3) 
    two = tk.Button(f, text=' 2 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(2, equation), height=2, width=7).grid(row=4, column=4) 
  
    three = tk.Button(f, text=' 3 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(3, equation), height=2, width=7).grid(row=4, column=5) 
    minus = tk.Button(f, text=' - ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("-", equation), height=2, width=7).grid(row=4, column=6)
    
   # fourth row 
    Ans = tk.Button(f, text=' Ans ', fg='black', bg='#87927e', 
                     command=lambda: answer(equation), height=2, width=7).grid(row=5, column=0)
    Del = tk.Button(f, text=' Del ', fg='black', bg='#87927e', 
                     command=lambda: delete(equation), height=2, width=7).grid(row=5, column=2)
    power = tk.Button(f, text=' power ', fg='black', bg='#87927e', 
                     command=lambda: btn_power(equation), height=2, width=7).grid(row=5, column=1)
    zero = tk.Button(f, text=' 0 ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(0, equation), height=2, width=7).grid(row=5, column=3)
    point = tk.Button(f, text=' . ', fg='black', bg='#e6f6df', 
                     command=lambda: btn_click(".", equation), height=2, width=7).grid(row=5, column=4)
    equals = tk.Button(f, text=' = ', fg='black', bg='#00c0ff', 
                     command=lambda: btn_equal(equation), height=2, width=7).grid(row=5, column=5)
    plus = tk.Button(f, text=' + ', fg='black', bg='#87927e', 
                     command=lambda: btn_click("+", equation), height=2, width=7).grid(row=5, column=6)
    f.mainloop()
if __name__ == '__main__':
    main()
