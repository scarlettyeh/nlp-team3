from flask import Flask

# create Flask app
app = Flask(__name__)

# create route for /
@app.route('/')

#### sg.theme('DarkBlue')	 
# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Please input the sentence you want corrected or Attach a word file')],
            [sg.Text('Input Sentence'), sg.InputText()],
            [sg.Text('Attach File'), sg.InputText('Default Folder', size=(45,22)), sg.FolderBrowse(), sg.Stretch()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
UploadFlag = 0

# Create the Window
window = sg.Window('SMU English Correction Tool').Layout([[sg.Input(key='FILES'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]])

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or UploadFlag > 0:	# if user closes window or clicks cancel
        break
    UploadFlag + 1
    List_of_Files = (values['FILES'].split(';'))
    print(values['FILES'].split(';'))
    #Input = values[0]
    #print('You entered ', values[0])
window.close()
