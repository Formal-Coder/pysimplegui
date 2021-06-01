# displaying message to the user

import PySimpleGUI as sg

# giving layout to the window with width of given text and height with ok button

layout = [[sg.Text("Hello from /real-python/pysimplegui")], [sg.Button("OK")]]

# creating a window
window = sg.Window("Demo",layout)
sg.Window(title="2.psg.py").read()  # won't run without read()

# create a loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN.CLOSED:
        break

window.close()