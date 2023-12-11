from tkinter import StringVar, Tk

root = Tk()
last_directory = StringVar()
csv_file = StringVar()
json_file = StringVar()
google_sheet_name = StringVar()

accept_button = StringVar()
verify_button = StringVar()
compare_button = StringVar()
export_button = StringVar()
close_button = StringVar()
load_output = StringVar()

###

last_directory.set('sensitive/')
csv_file.set('')
json_file.set('')
google_sheet_name.set('VIII Гордеевский фестиваль')

accept_button.set('')
verify_button.set('')
compare_button.set('')
export_button.set('')
close_button.set('')
load_output.set('none')