""" This is a IDE I made for my daily puthon practices"""
import re
#importing libraries
from tkinter import * #tkinter for the GUI
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import colorchooser #colorchooser to pick color
import subprocess # subprocess for compiling code
import jedi #to autocompelete text
import pygments
from  pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters import HtmlFormatter


#function to set the file path
def set_file_path(path):
    global file_path
    file_path = path

#function to run the code from ide
def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Save your code Nigger!", padx=5, pady=19)
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    code_output.insert(1.0, output)
    code_output.insert(1.0, error)

#function to save and save_as files in ide
def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('python files', '*.py')], defaultextension='.py')
    else:
        path = file_path
    path = asksaveasfilename(filetypes=[("Python Files", "*.py")], defaultextension='.py')
    with open(path, "w") as file:
        code = text_edit.get(1.0, END)
        file.write(code)
        set_file_path(path)

#function to open files in ide
def open_file():
    path = askopenfilename(filetypes=[("Python Files", "*.py")], defaultextension='.py')
    with open(path, "r") as file:
        code = file.read()
        text_edit.delete(1.0, END)
        text_edit.insert(1.0, code)
        set_file_path(path)

#function to change background color
def background_color():
    color = colorchooser.askcolor()[1]
    text_edit.config(bg=color)

#function to change font color
def font_color():
    color = colorchooser.askcolor()[1]
    text_edit.config(fg=color)

#function to copy from ide
def copy_text():
    window.clipboard_clear()
    window.clipboard_append(text_edit.get(1.0, END))

#function to cut from ide
def cut_text():
    window.clipboard_clear()
    window.clipboard_append(text_edit.get('sel.first', 'sel.last'))

#function to paste in ide
def paste_text():
    window.clipboard_get()

#adding line numbers to the editor
def add_line_numbers(event = None):
    editor = text_edit.get(1.0, "end-1c")
    line_numbers = "\n".join(str(i+1) for i in range(editor.count("\n")))
    line_number_bar.config(state=NORMAL)
    line_number_bar.delete(1.0, END)
    line_number_bar.insert(END, line_numbers)
    line_number_bar.config(state=DISABLED)


"""#syntax highlighting using pygments
def apply_syntax_highlight(event = None):
    code = text_edit.get(1.0, END)
    highlighted_code = pygments.highlight(code, PythonLexer(), HtmlFormatter(nowrap = True))
    highlighted_code = re.sub(r'<.*?>', '', highlighted_code)
    text_edit.delete(1.0, END)
    text_edit.insert(1.0, highlighted_code)"""

#smarter autocomplete using jedi


#showing in line documentation using jedi


#function to handle autocompeletion using tab key


#function to search within the editor


window = Tk() #main window
window.title('IDE by @duttaturja')
file_path = ''
window.rowconfigure(0,minsize=500)
window.columnconfigure(1,minsize=500)

#line numbers at the left
line_number_bar = Text(window, width=2, padx=6, pady=3, takefocus=0, border=0, font="Consolas 12" ,background='lightgrey', fg='black')
line_number_bar.pack(side=LEFT, fill= Y)

#coding section in the ide
text_edit = Text(window, font="Consolas 12", padx=5, pady=3, undo=True)
text_edit.pack( expand = True, fill = BOTH)

#menu bar
menu = Menu(window)

#file menu and its items
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="New", accelerator='Ctrl+Shift+N')
file_menu.add_command(label='Open',accelerator='Ctrl+O', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save',accelerator='Ctrl+S', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)
menu.add_cascade(label='File', menu=file_menu)

#edit menu and its items
edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', command=text_edit.edit_undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Shift+Z', command=text_edit.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cut_text)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copy_text)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=paste_text)
menu.add_cascade(label='Edit', menu=edit_menu)

#run menu and its item
run_menu = Menu(menu, tearoff=0)
run_menu.add_command(label='Run', accelerator='F9', command=run)
menu.add_cascade(label='Run', menu=run_menu)

#personalization menu
personalization_menu = Menu(menu, tearoff=0)
personalization_menu.add_command(label='Background Color', command=background_color)
personalization_menu.add_command(label='Text Color', command=font_color)
menu.add_cascade(label='Personalization', menu=personalization_menu)

#setting the menu at window
window.config(menu=menu)

#menubar shortcuts and keybindings
text_edit.bind("<Control-s>",save_as)
text_edit.bind("<Control-o>", open_file)
text_edit.bind("<Control-Shift-s>", save_as)
text_edit.bind("<F9>", run)
text_edit.bind("<KeyRelease>", add_line_numbers)
#text_edit.bind("<KeyRelease>", apply_syntax_highlight)

#making a list box for suggestions


#output section in the ide
code_output = Text(height=10, width=90, bg='#282828', fg='#33FF00', bd=0, padx=5, pady=5, undo=True)
code_output.pack(expand = True, fill = BOTH)

#function to stop the code after selecting the red x
window.mainloop()

#https://onecompiler.com/python/42u4ub8t9
#https://onecompiler.com/python/42vkbra32
#developed by duttaturja