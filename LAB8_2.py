import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_permuted_alphabet(keyword):
    seen = set()
    keyword_upper = ''.join([ch for ch in keyword.upper() if not (ch in seen or seen.add(ch))])
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remaining_alphabet = ''.join([ch for ch in alphabet if ch not in keyword_upper])
    permuted_alphabet = keyword_upper + remaining_alphabet
    return permuted_alphabet

def caesar_cipher_with_keyword(text, key, keyword, mode='encrypt'):
    permuted_alphabet = generate_permuted_alphabet(keyword)
    result = ""
    text = text.upper().replace(" ", "")
    for char in text:
        if char in permuted_alphabet:
            original_index = permuted_alphabet.index(char)
            if mode == 'encrypt':
                new_index = (original_index + key) % 26
            else:  # Modul 'decrypt'
                new_index = (original_index - key) % 26
            result_char = permuted_alphabet[new_index]
            result += result_char
        else:
            result += char
    return result

def execute():
    mode = operation_var.get().lower()
    text = text_entry.get()
    key1 = key1_entry.get()

    if not key1.isdigit() or not 1 <= int(key1) <= 25:
        messagebox.showerror("Eroare", "Cheia trebuie să fie un număr între 1 și 25.")
        return

    if use_keyword_var.get():
        keyword = keyword_entry.get()
        if not keyword.isalpha() or len(keyword) < 7:
            messagebox.showerror("Eroare", "Cuvântul-cheie trebuie să conțină doar litere și să aibă o lungime de cel puțin 7 caractere.")
            return
        result = caesar_cipher_with_keyword(text, int(key1), keyword, mode)
    else:
        result = caesar_cipher_with_keyword(text, int(key1), "", mode)

    result_entry.config(state=tk.NORMAL)
    result_entry.delete(1.0, tk.END)
    result_entry.insert(tk.END, result)
    result_entry.config(state=tk.DISABLED)

def reset():
    text_entry.delete(0, tk.END)
    key1_entry.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    result_entry.config(state=tk.NORMAL)
    result_entry.delete(1.0, tk.END)
    result_entry.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Cifrul Cezar cu două chei")
root.configure(bg='#ffc0cb')
root.geometry("600x400")

style = ttk.Style(root)
style.theme_use('clam')
style.configure('TButton', foreground='#ffffff', background='#ff69b4', borderwidth=2)
style.map('TButton', background=[('active', '#ff1493')])
style.configure('TLabel', foreground='#333333', background='#ffc0cb')
style.configure('TEntry', fieldbackground='#ffffff')
style.configure('TCheckbutton', background='#ffc0cb', foreground='#333333')

tk.Label(root, text="Introduceți cuvântul:", background='#ffc0cb').grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.grid(column=1, row=0, sticky=tk.W, padx=10, pady=5)

tk.Label(root, text="Indicați cheia (1-25):", background='#ffc0cb').grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)
key1_entry = tk.Entry(root, width=50)
key1_entry.grid(column=1, row=1, sticky=tk.W, padx=10, pady=5)

use_keyword_var = tk.BooleanVar(value=False)
use_keyword_checkbox = tk.Checkbutton(root, text="Utilizați cuvânt-cheie", variable=use_keyword_var, onvalue=True, offvalue=False, background='#ffc0cb')
use_keyword_checkbox.grid(column=1, row=2, columnspan=2, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Introduceți cuvântul-cheie (minim 7 litere):", background='#ffc0cb').grid(column=0, row=3, sticky=tk.W, padx=10, pady=5)
keyword_entry = tk.Entry(root, width=50, state=tk.DISABLED)
keyword_entry.grid(column=1, row=3, sticky=tk.W, padx=10, pady=5)

def toggle_keyword_entry():
    if use_keyword_var.get():
        keyword_entry.config(state=tk.NORMAL)
    else:
        keyword_entry.config(state=tk.DISABLED)

use_keyword_checkbox.config(command=toggle_keyword_entry)

execute_button = ttk.Button(root, text="Execută", command=execute)
execute_button.grid(column=1, row=4, padx=(10, 5), pady=5, sticky=tk.W)

reset_button = ttk.Button(root, text="Resetează", command=reset)
reset_button.grid(column=1, row=4, padx=(5, 10), pady=5, sticky=tk.E)

tk.Label(root, text="Rezultatul:", background='#ffc0cb').grid(column=0, row=5, sticky=tk.W, padx=10, pady=5)
result_entry = tk.Text(root, height=5, width=70)
result_entry.grid(column=0, row=6, columnspan=2, sticky=tk.W, padx=10, pady=5)

tk.Label(root, text="Opțiunea dorită:", background='#ffc0cb').grid(column=0, row=7, sticky=tk.W, padx=10, pady=5)
operation_var = tk.StringVar()
encrypt_checkbox = tk.Checkbutton(root, text="Encrypt", variable=operation_var, onvalue="encrypt", offvalue="", background='#ffc0cb')
decrypt_checkbox = tk.Checkbutton(root, text="Decrypt", variable=operation_var, onvalue="decrypt", offvalue="", background='#ffc0cb')
encrypt_checkbox.grid(column=1, row=7, padx=(5, 3), pady=3, sticky=tk.W)
decrypt_checkbox.grid(column=1, row=7, padx=(3, 5), pady=3, sticky=tk.E)

root.mainloop()
