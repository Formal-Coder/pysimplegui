# This python file demonstrates the usage of pythonsimplegui
# I got reference from realpython.com and i'm really thankful to them

# creating an empty gui window
import PySimpleGUI as sg

sg.Window(title="Hello world", layout=[[]], margins=(100,100)).read()


import PySimpleGUI as sg

layout = [[sg.Text("Hello from /real-python/pysimplegui")], [sg.Button("OK")]]

# creating a window
window = sg.Window("Demo",layout)

# create a loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN.CLOSED:
        break

window.close()