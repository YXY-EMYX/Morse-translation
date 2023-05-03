import tkinter as tk
from tkinter import messagebox

# 摩斯电码字典
MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# 将英语翻译成摩斯电码
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

# 将摩斯电码翻译成英语
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def translate():
    message = text_input.get("1.0",'end-1c')
    if (btn_var.get() == 1):
        result = encrypt(message.upper())
    else:
        result = decrypt(message)
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, result)

root = tk.Tk()
root.title("Morse Code Translator")

btn_var = tk.IntVar()
btn_var.set(1)

text_input = tk.Text(root, height=8, width=30)
text_input.pack()

radiobtn1 = tk.Radiobutton(root, text="Text to Morse", variable=btn_var, value=1)
radiobtn1.pack()

radiobtn2 = tk.Radiobutton(root, text="Morse to Text", variable=btn_var, value=2)
radiobtn2.pack()

btn = tk.Button(root, text="Translate", command=translate)
btn.pack()

text_output = tk.Text(root, height=8, width=30)
text_output.pack()

root.mainloop()
