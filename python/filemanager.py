from tkinter import END, Entry, Label, OptionMenu, Tk, Button, Toplevel, mainloop, W, E, Text, N, S
import os
from calculator import Calculator
# from airquality import AirQuality
from weather import Weather

root = Tk()
root.title("Desktop Friend!")
root.geometry('1500x700')

def make_folder():
    new_folder = os.getcwd() + '\\' + make_folder_entry.get()
    make_folder_entry.delete(0, END)
    try:
        os.mkdir(new_folder)
        display()
    except (Exception):
        return

def delete_folder():
    delete_folder = os.getcwd() + '\\' + delete_folder_entry.get()
    delete_folder_entry.delete(0, END)
    try:
        os.rmdir(delete_folder)
        display()
    except (Exception):
        return

def delete_file():
    delete_file = delete_file_entry.get()
    delete_file_entry.delete(0, END)
    try:
        os.remove( os.getcwd() + '\\' + delete_file )
        display()
    except (Exception):
        return

def start_file():
    start_file = start_file_entry.get()
    start_file_entry.delete(0, END)
    try:
        os.startfile(start_file)
    except (Exception):
        return

def display():
    files_and_folders = os.listdir( os.getcwd() )
    files_list = []
    folders_list = []
    # divide up list into files and folders
    for x in files_and_folders:
        if '.' in x and x[0] != '.':
            files_list.append(x)
        else:
            folders_list.append(x)

    list_files_lbl = Label(root, text='Files:')
    list_files_lbl.grid(row=3, column=0, pady=10, sticky=W+E)
    files_text_box = Text(root, width=50, height=10)
    files_text_box.insert(END, files_list)
    files_text_box.grid(row=4, column=0, pady=10, sticky=W+E)
    list_folders_lbl = Label(root, text='Folders:')
    list_folders_lbl.grid(row=3, column=1, pady=10)
    folders_text_box = Text(root, width=50, height=10)
    folders_text_box.insert(END, folders_list)
    folders_text_box.grid(row=4, column=1, pady=10, sticky=W+E)

def change_dir():
    new_dir = change_dir_entry.get()
    change_dir_entry.delete(0, END)
    # check if new_dir is not a subfolder
    if 'C' == new_dir[0]:
        os.chdir(new_dir)
        current_directory = Label(root, text=os.getcwd())
        current_directory.grid(row=1, column=0, columnspan=2, pady=10, sticky=W+E)
        display()
        return

    # check if request is desktop
    if new_dir.lower == 'desktop':
        os.chdir('C:/Users/giodi/OneDrive/Desktop/')
        current_directory = Label(root, text=os.getcwd())
        current_directory.grid(row=1, column=0, columnspan=2, pady=10, sticky=W+E)
        display()
        return

    # go into a higher-level folder
    if new_dir in os.getcwd():
        temp = ''
        curr_dir = os.getcwd()
        for i in range( len(curr_dir) ):
            for j in range(i + 1, len(curr_dir) ):
                if new_dir == curr_dir[i:j]:
                    temp = curr_dir[:j+1]
        new_dir = temp
        try:
            os.chdir(new_dir)
            current_directory = Label(root, text=os.getcwd())
            current_directory.grid(row=1, column=0, columnspan=2, pady=10, sticky=W+E)
            display()
            return
        except (Exception):
            return

    # if subfolder, do this
    new_dir = os.getcwd() + "\\" + new_dir
    try:
        os.chdir(new_dir)
        current_directory = Label(root, text=os.getcwd())
        current_directory.grid(row=1, column=0, columnspan=2, pady=10, sticky=W+E)
        display()
        return
    except (Exception):
        return

def calculator_win():
    calc_win = Calculator()
    calc_win.run()

def weather_win():
    weather_win = Weather()
    weather_win.run()

# current directory
if True:
    os.chdir('C:/Users/giodi/OneDrive/Desktop/')
    current_directory_lbl = Label(root, text='Current Directory:', font='bold')
    current_directory_lbl.grid(row=0, column=0, columnspan=2, pady=10, sticky=W+E)
    current_directory = Label(root, text=os.getcwd())
    current_directory.grid(row=1, column=0, columnspan=2, pady=10)

# display files
files_and_folders = os.listdir( os.getcwd() )
files_list = []
folders_list = []
# divide up list into files and folders
for x in files_and_folders:
    if '.' in x:
        files_list.append(x)
    else:
        folders_list.append(x)

# files and folders
if True:
    list_files_lbl = Label(root, text='Files:')
    list_files_lbl.grid(row=3, column=0, pady=10, sticky=W+E)
    files_text_box = Text(root, width=50)
    files_text_box.insert(END, files_list)
    files_text_box.grid(row=4, column=0, pady=10, sticky=W+E+N+S)
    list_folders_lbl = Label(root, text='Folders:')
    list_folders_lbl.grid(row=3, column=1, pady=10)
    folders_text_box = Text(root, width=50)
    folders_text_box.insert(END, folders_list)
    folders_text_box.grid(row=4, column=1, pady=10, sticky=W+E+N+S)

# calculator pop-up page
if True:
    calculator_btn = Button(root, text='Calculator', command=calculator_win)
    calculator_btn.grid(row=0, column=2)

# air quality pop-up page
if True:
    weather_btn = Button(root, text='Weather', command=weather_win)
    weather_btn.grid(row=0, column=3)

# change directory
if True:
    change_dir_btn = Button(root, text='Change Folder:', command=change_dir)
    change_dir_btn.grid(row=5, column=0, pady=10)
    change_dir_entry = Entry(root)
    change_dir_entry.grid(row=5, column=1)

# start file
if True:
    start_file_btn = Button(root, text='Start File', command=start_file)
    start_file_btn.grid(row=5, column=2, pady=10)
    start_file_entry = Entry(root)
    start_file_entry.grid(row=5, column=3, pady=10)

# delete a file
if True:
    delete_file_btn = Button(root, text='Delete File', command=delete_file)
    delete_file_btn.grid(row=2, column=2, padx=5, pady=10)
    delete_file_entry = Entry(root)
    delete_file_entry.grid(row=2, column=3, padx=5, pady=10)

# delete a folder
if True:
    delete_folder_btn = Button(root, text='Delete Folder', command=delete_folder)
    delete_folder_btn.grid(row=3, column=2, padx=5, pady=10)
    delete_folder_entry = Entry(root)
    delete_folder_entry.grid(row=3, column=3, padx=5, pady=10)

# make a folder
if True:
    make_folder_btn = Button(root, text='Make Folder', command=make_folder)
    make_folder_btn.grid(row=4, column=2, padx=5, pady=10)
    make_folder_entry = Entry(root)
    make_folder_entry.grid(row=4, column=3, padx=5, pady=10)

if __name__ == '__main__':
    mainloop()