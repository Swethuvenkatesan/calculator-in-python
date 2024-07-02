from tkinter import Label,Button, Tk
calc_app=Tk()
calc_app.title("calculator")
calc_app.geometry('570x600+100+200')
calc_app.resizable(False,False)
calc_app.configure(background='sky blue')

equation = " "

def show(value):
    global equation
    equation+=value
    Label_result.config(text=equation)
    
def clear():
    global equation
    equation =""
    Label_result.config(text=equation)
    
    
def calculate():
    global equation
    result = " "
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation = " "
    Label_result.config(text=result)
    
    
    
Label_result=Label(calc_app,width=25,height=2,text="",font=("arial",30))
Label_result.pack()   

Button(calc_app,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="blue" , command=lambda:clear()).place(x=10,y=100) 
  
Button(calc_app,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda: show("/")).place(x=150,y=100) 
  
Button(calc_app,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("%")).place(x=290,y=100)

Button(calc_app,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("*")).place(x=430,y=100)       


Button(calc_app,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("7")).place(x=10,y=200) 
  
Button(calc_app,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("8")).place(x=150,y=200) 
  
Button(calc_app,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("9")).place(x=290,y=200)

Button(calc_app,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("-")).place(x=430,y=200) 


Button(calc_app,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("4")).place(x=10,y=300) 
  
Button(calc_app,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("5")).place(x=150,y=300) 
  
Button(calc_app,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black",command=lambda:show("6")).place(x=290,y=300)

Button(calc_app,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black",command=lambda:show("+")).place(x=430,y=300)    



Button(calc_app,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black" , command=lambda:show("1")).place(x=10,y=400) 
  
Button(calc_app,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda: show("2")).place(x=150,y=400) 
  
Button(calc_app,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("3")).place(x=290,y=400)

Button(calc_app,text="0", width=11, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black", command=lambda:show("0")).place(x=10,y=500)       
     
      


Button(calc_app,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="black",command=lambda: show(".")).place(x=290,y=500)

Button(calc_app,text="=", width=5, height=1, font=("arial",30,"bold"), bd=1,
fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=400)       
      


calc_app.mainloop()





'''This imports the necessary classes (Label, Button, and Tk) from the tkinter module.
This sets the size and position of the main window. The format is widthxheight+x_offset+y_offset. 
 570 pixels wide and 600 pixels high, and it will be positioned 
 100 pixels from the left edge of the screen and 200 pixels from the top edge of the screen.
 This makes the window resizable. The first True allows horizontal resizing, 
 and the second True allows vertical resizing.
 
 equation = " "
This initializes the global variable equation to store the current input string for the calculator.

def show(value):
    global equation
    equation += value
    Label_result.config(text=equation)
This function show appends the input value to the equation and updates the label (Label_result) to display the current equation.

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)
This function clear resets the equation to an empty string and updates the label to reflect the cleared equation.



def calculate():
    
    global equation
    result = " "
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = " "
    Label_result.config(text=result)
This function calculate evaluates the current equation using the eval function and displays the result. If there's an error in evaluation, it sets the result to "error" and clears the equation.

This creates a button labeled "C" to clear the equation. It sets the button's size, font, border width, 
foreground and background colors, and places it at the specified coordinates (x=10, y=100). 
The button calls the clear function when clicked.

These create buttons for the division (/), percentage (%), and multiplication (*) operators.
 Each button calls the show function with the respective operator when clicked.

These create buttons for the digits 7, 8, and 9, and the subtraction (-) operator.
 Each button calls the show function with the respective digit or operator when clicked.


These create buttons for the digits 4, 5, and 6, and the addition (+) operator. 
Each button calls the show function with the respective digit or operator when clicked.

These create buttons for the digits 1, 2, 3, and 0. 
The button for 0 spans two columns in width. Each button calls the show function with the respective digit when clicked.

This creates a button for the decimal point (.). It calls the show function with the decimal point when clicked.

python
Copy code
Button(calc_app, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1,
       fg="#fff", bg="#fe9037", command=calculate).place(x=430, y=400)
This creates a button for the equals (=) operator.
 It calls the calculate function to evaluate the current equation when clicked.

python
Copy code
calc_app.mainloop()
This starts the main event loop of the Tkinter application, waiting for user interactions.

In summary, this code sets up a basic calculator using Tkinter with buttons for digits, operators, 
and a label to display the input and result. The show, clear, and calculate functions handle the input, 
clearing, and evaluation of the equation, respectively.

The lambda keyword in Python is used to create small anonymous functions (functions without a name). 
In your Tkinter calculator code, lambda is used to define simple inline functions 
that are executed when the buttons are clicked.
In this line, a Button widget is created with the following properties:

text: The text displayed on the button, which is / in this case.
width: The width of the button.
height: The height of the button.
font: The font of the text on the button.
bd: The border width of the button.
fg: The foreground color (text color) of the button.
bg: The background color of the button.
command: The function to be executed when the button is clicked. Here, lambda: show("/") is used.
The command parameter is set to a lambda function: lambda: show("/"). This lambda function is a shorthand way to define a function that calls show("/") when the button is clicked.

Explanation of Lambda
A lambda function is defined as:

python
Copy code
lambda arguments: expression










'''


''' password generator'''

7



'''import random
This imports the random module, which provides functions to generate random numbers and select random items.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
This defines a list called letters that contains all lowercase letters of the alphabet.

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
This defines a list called numbers that contains all digits from 0 to 9.

symbols = ['!', '#', '@', '$', '*', '+', '&', '(', ')']
This defines a list called symbols that contains various special characters.

print("welcome to password generator!")
This prints a welcome message to the user.

n_letters = int(input("how many letters you want in your password?\n"))
This prompts the user to enter the number of letters they want in their password. The input is converted to an integer and stored in n_letters.

n_symbols = int(input("how many symbols you want in your password?\n"))
This prompts the user to enter the number of symbols they want in their password. The input is converted to an integer and stored in n_symbols.

n_numbers = int(input("how many numbers you want in your password?\n"))
This prompts the user to enter the number of numbers they want in their password. The input is converted to an integer and stored in n_numbers.

password_list = []
This initializes an empty list called password_list which will hold the characters of the password.

for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list += char
This loop runs n_letters times. In each iteration, it randomly selects a letter from the letters list and appends it to password_list.

for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_list += char
This loop runs n_symbols times. In each iteration, it randomly selects a symbol from the symbols list and appends it to password_list.

for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    password_list += char
This loop runs n_numbers times. In each iteration, it randomly selects a number from the numbers list and appends it to password_list.

print(password_list)
This prints the password_list before shuffling, showing the characters in the order they were added.

random.shuffle(password_list)
This shuffles the elements of password_list in place, creating a random order.


print(password_list)
This prints the shuffled password_list.


password = ""
This initializes an empty string called password which will hold the final password.


for char in password_list:
    password += char
This loop concatenates each character in password_list to the password string.


print(password)
This prints the final password.

The overall flow of the program is as follows:

Import necessary modules.
Define character pools (letters, numbers, symbols).
Gather user input for the number of each character type.
Create a list of random characters based on user input.
Shuffle the list to randomize the order.
Concatenate the list into a single password string.
Print the generated password.'''