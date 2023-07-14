import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import ChatGPT
import DocQA
import os
from docx2python import docx2python
from pdfminer.high_level import extract_text


def send_message():
    user_message = user_input.get()
    response = ChatGPT.sendResponse(user_message)
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    chat_display.insert(tk.END, "Chatbot: " + response + "\n")
    user_input.delete(0, tk.END)

def question_answering():
    question = user_input_Document.get()
    chat_display_other.insert(tk.END, "You: " + question + "\n")
    context  = document_display.get(1.0, tk.END)
    response  = DocQA.sendResponse(question,context)
    chat_display_other.insert(tk.END, "Chatbot: " + response + "\n")
    user_input_Document.delete(0, tk.END)
    
def on_tab_change(event):
    selected_tab = event.widget.select()
    tab_index = event.widget.index(selected_tab)
    if tab_index == 0:
        message_label.config(text="Chatbot tab selected.")
    elif tab_index == 1:
        message_label.config(text="Document tab selected.")


def browse_file():
    file = filedialog.askopenfilename()
    fname,fext = os.path.splitext(file)
    if fext == ".pdf":
        context = extract_text(file)
    elif fext == ".docx":
        doc_result = docx2python(file)
        context = doc_result.text
    elif fext == ".txt":
        with open(file, 'r') as f:
            context = f.read()
    document_display.insert(tk.END,context)


window = tk.Tk()
window.title("Chatbot with Tabs")

tab_control = ttk.Notebook(window)

# Chatbot tab
chat_tab = ttk.Frame(tab_control)
tab_control.add(chat_tab, text='Chatbot')

chat_display = scrolledtext.ScrolledText(chat_tab, width=50, height=20)
chat_display.grid(column=0, row=0, padx=10, pady=10)

user_input = tk.Entry(chat_tab, width=40)
user_input.grid(column=0, row=1, padx=10, pady=10)

send_button = tk.Button(chat_tab, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Document tab
Document_tab = ttk.Frame(tab_control)
tab_control.add(Document_tab, text='Document')

document_label = tk.Label(Document_tab, text="Upload a Document:")
document_label.pack(padx=10, pady=10)

document_button = tk.Button(Document_tab, text="Browse", command=browse_file)
document_button.pack(padx=10, pady=10)

document_display = scrolledtext.ScrolledText(Document_tab, width=50, height=15)
document_display.pack(padx=10, pady=10)

chat_display_other = scrolledtext.ScrolledText(Document_tab, width=50, height=5)
chat_display_other.pack(padx=10, pady=10)

user_input_Document = tk.Entry(Document_tab, width=40)
user_input_Document.pack(padx=10, pady=10)

send_button_Document = tk.Button(Document_tab, text="Send", command=question_answering)
send_button_Document.pack(padx=10, pady=10)

tab_control.pack(expand=1, fill="both")

# Message label
message_label = tk.Label(window, text="Select a tab!")
message_label.pack(pady=10)

# Event handling
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

window.mainloop()