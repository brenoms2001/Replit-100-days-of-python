import tkinter as tk
from time import sleep

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")

number = "0"
total = 0.0
previousOp = ""

numberShowed = tk.Label(text = number)
numberShowed.grid(row=0, column=2)

def buttonChoice(n):
  global number
  global total
  global previousOp

  if previousOp == "=":
    total = 0.0
    previousOp = ""
    
  number = n if number == "0" else number + n
  numberShowed["text"] = number
  
def operatorChoice(op):
  global total
  global number
  global previousOp
  
  if op == "+":
    total += float(number)
  elif op == "-":
    total -= float(number)
  elif op == "*":
    if total == 0.0:
      total = float(number)
    else:
      if number != "0" and previousOp == "=":
        total *= float(number)
  elif op == "/":
    if number != "0":
      if total == 0.0:
        total = float(number)
      else:
        total /= float(number)
    elif number == "0" and previousOp != "=":
      numberShowed["text"] = "ERRO: DIVISÃO POR ZERO. FECHANDO..."
      sleep(3)
      exit()

  if op != "=":
    previousOp = op
    
  if op == "=" and previousOp != "=":
    if previousOp == "+":
      total += float(number)
    elif previousOp == "-":
      total -= float(number)
    elif previousOp == "*":
      total *= float(number)
    elif previousOp == "/":
      if number != "0":
        if total == 0:
          total = number
        else:
          total /= float(number)
      else:
        numberShowed["text"] = "ERRO: DIVISÃO POR ZERO. FECHANDO..."
        exit()
    previousOp = "="
    numberShowed["text"] = str(total)

  number = "0"

#First line
button1 = tk.Button(text = "1", command=lambda:buttonChoice("1"))
button1.grid(row=1, column=0)

button2 = tk.Button(text = "2", command=lambda:buttonChoice("2"))
button2.grid(row=1, column=1)

button3 = tk.Button(text = "3", command=lambda:buttonChoice("3"))
button3.grid(row=1, column=2)

buttonPlus = tk.Button(text = "+", command=lambda:operatorChoice("+"))
buttonPlus.grid(row=1, column=3)

buttonMinus = tk.Button(text = "-", command=lambda:operatorChoice("-"))
buttonMinus.grid(row=1, column=4)

#Second line
button4 = tk.Button(text = "4", command=lambda:buttonChoice("4"))
button4.grid(row=2, column=0)

button5 = tk.Button(text = "5", command=lambda:buttonChoice("5"))
button5.grid(row=2, column=1)

button6 = tk.Button(text = "6", command=lambda:buttonChoice("6"))
button6.grid(row=2, column=2)

buttonTimes = tk.Button(text = "*", command=lambda:operatorChoice("*"))
buttonTimes.grid(row=2, column=3)

buttonDivide = tk.Button(text = "/", command=lambda:operatorChoice("/"))
buttonDivide.grid(row=2, column=4)

#Third line
button7 = tk.Button(text = "7", command=lambda:buttonChoice("7"))
button7.grid(row=3, column=0)

button8 = tk.Button(text = "8", command=lambda:buttonChoice("8"))
button8.grid(row=3, column=1)

button9 = tk.Button(text = "9", command=lambda:buttonChoice("9"))
button9.grid(row=3, column=2)

#Forth line
button0 = tk.Button(text = "0", command=lambda:buttonChoice("0"))
button0.grid(row=4, column=1)

button5 = tk.Button(text = "=", command=lambda:operatorChoice("="))
button5.grid(row=4, column=3)

tk.mainloop()

