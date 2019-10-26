# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:13:12 2019

@author: user
"""
""" JOSHUA JAISTEIN S URK18CS033 (II YEAR) CSE """
""" KARUNYA UNIVERSITY , INDIA.                 """

#First of all, we import the python library, which is essential to plot graphs.
import matplotlib.pyplot as plt
# 'plt' can be anyting as you wish, we consider 'plt' for easy explanation.
# we use numpy library for numerical calculation(or) value assigning purpose.
import numpy as np
# here also 'np' can be anything as you wish.

#The menu driven function
def Start():
   
  print("Welcome , we're going to look at lines in matplotlib")
  print("Select operation.")
  print("1.SimpleLine")
  print("2.Add Colour to the SimpleLine")
  print("3.Add Effects to the Simpleline")
  print("4.Create custom coordinates for plotting")
  print("5.Plotting the straight line equation y = mx + c")
  print("6.About Me!")
  print("Enter choice")
  choice = input()

#---------- A simple line drawn in the canvas ----------

  if choice == '1':
      SimpleLine()
      
#---------- The same line with different colour ----------
       
  elif choice == '2':
      print("The different colours are :")
      print("blue")
      print("green")
      print("red")
      print("cyan")
      print("magenta")
      print("yellow")
      print("black")
      print("white")
      
      print("Change the code")
      print("Try it for youself and play around !")
      LineColour()
      
#---------- The different styling options that I know :) ----------

  elif choice == '3':
      print("a.Dashed Style")
      print("b.Dotted Style")
      print("c.Dashdotted style")
                
      subChoice = input("Enter the Styling : ")
      if subChoice == 'a':
          LineStyleDashed()
          
      elif subChoice == 'b':
          LineStyleDotted()
          
      elif subChoice == 'c':
          LineStyleDashdotted()
  
  elif choice == '4':
      CustomCoordinate()
      
      
  elif choice == '5':
    yisEquals()
    
  elif choice == '6':
    Me()
    
    
  else:
    print("Invalid input")     
   
#---------- Function Declaration area ----------

def SimpleLine():
   X = range(1, 50)
   Y = [value * 4 for value in X]
   plt.plot(X, Y)
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.title('A simple line.')
   plt.show()
   
def LineColour():
   X = range(1, 50)
   Y = [value * 4 for value in X]
   plt.plot(X, Y, color = 'red')
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.title('A simple line.')
   plt.show()

def LineStyleDashed():
   X = range(1, 50)
   Y = [value * 4 for value in X]
   plt.plot(X, Y, color = 'red',linestyle = 'dashed')
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.title('A simple line.')
   plt.show()
   
def LineStyleDashed():
   X = range(1, 50)
   Y = [value * 4 for value in X]
   plt.plot(X, Y, color = 'red',linestyle = 'dotted')
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.title('A simple line.')
   plt.show()
   
def LineStyleDashdotted():
   X = range(1, 50)
   Y = [value * 4 for value in X]
   plt.plot(X, Y, color = 'red',linestyle = 'dashdot')
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.title('A simple line.')
   plt.show()
   
def CustomCoordinate():
   fig = plt.figure()
   ax = fig.add_subplot(1, 1, 1)
   ax.spines['left'].set_position('center')
   ax.spines['bottom'].set_position('center')
   ax.spines['right'].set_color('none')
   ax.spines['top'].set_color('none')
   ax.xaxis.set_ticks_position('bottom')
   ax.yaxis.set_ticks_position('left')
   plt.plot()
   plt.show()
   
def yisEquals():
   fig = plt.figure()
   ax = fig.add_subplot(1, 1, 1)
   x = np.linspace(-5,5,100)
   #linspace is the in-built function in numpy to create even spacing in the plot
   ax.spines['left'].set_position('center')
   ax.spines['bottom'].set_position('center')
   ax.spines['right'].set_color('none')
   ax.spines['top'].set_color('none')
   ax.xaxis.set_ticks_position('bottom')
   ax.yaxis.set_ticks_position('left')
   #play around by defining your favourite values
   plt.plot(x, 2*x+3,':b', label='y=2x+3',color = 'red')
   #here, m = 2; c = 3
   plt.plot()
   plt.show()

def Me():
   print("I love tech and I like to make things that enrich lives of people around me.\n My juniors were struggling with python programming\nAs I taught them ,it striked me to help other such potential students \nall aroud the globe.")
   
   
Start()
