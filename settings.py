from tkinter import StringVar, Tk, Variable

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
list_var = Variable()
selected_columns = Variable()

###

last_directory.set('sensitive')
csv_file.set('')
json_file.set('')
google_sheet_name.set('VIII Гордеевский фестиваль')

accept_button.set('')
verify_button.set('')
compare_button.set('')
export_button.set('')
close_button.set('')
load_output.set('none')
list_var.set(['Entry ID', 'Что для Вас есть авторская песня', 'Страна, город', 'Возраст', 'Место учёбы или работы', 'Адрес электронной почты', 'Согласие на обработку персональных данных', 'Custom HTML', 'Custom HTML.1', 'Название номера', 'Название коллектива и исполнители', 'Ссылка на запись Вашего выступления (YouTube, Google Drive, OneDrive и другие)', 'Автор слов в Вашем выступлении', 'Custom HTML.2', 'Ссылка на запись Вашего выступления (YouTube, Google Drive, OneDrive и другие).1', 'Автор музыки в Вашем выступлении', 'Как Вы узнали о Гордеевском фестивале?', 'IP Address', 'Date'])
selected_columns.set([])