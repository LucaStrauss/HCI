import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

directory_path = '/'
separator_symbol = '\t'

while True:
    file_path = filedialog.askopenfilename(initialdir=directory_path, title='Select a file')
    directory_path = os.path.dirname(file_path)
    txt = open(file_path,'r')
    count_lines = 0
    sum = 0
    for line in txt.readlines():
        values = line.split(separator_symbol)
        if len(values) == 2:
            values[0].lstrip()
            values[1].rstrip()
            try:
                sum = sum + ( (float(values[0]) + float(values[1])) / 2)
                count_lines = count_lines + 1
            except ValueError:
                break
        else:
            break
    print(sum / count_lines)
