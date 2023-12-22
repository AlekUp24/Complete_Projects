import tkinter as tk

# const
SIZE = (270,270)
TITLE = ""
FONT = "Arial"
FONT_SIZE = 14
ICO_PATH = "" #"blank.ico"

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def make_negative():
    global calculation
    try:
        if len(calculation) >0 and calculation[0] != "-":
            calculation = str("-"+calculation)
        elif len(calculation) >0 and calculation[0] == "-":
            calculation = str(calculation[1:])
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

# create window
window = tk.Tk()
window.geometry(f"{SIZE[0]}x{SIZE[1]}")
window.resizable(False, False)
window.iconbitmap(ICO_PATH)
window.title(TITLE)

# text field
text_result = tk.Text(window, height=2, width=15, font=(FONT,24))
text_result.grid(columnspan=5)

# numeric buttons
btn_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=5, font=(FONT,FONT_SIZE)).grid(row=6,column=1, columnspan=2, sticky=tk.EW , padx=0)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=5, font=(FONT,FONT_SIZE)).grid(row=5,column=1, sticky=tk.EW , padx=0)
btn_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=5, font=(FONT,FONT_SIZE)).grid(row=5,column=2, sticky=tk.EW , padx=0)
btn_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=5, font=(FONT,FONT_SIZE)).grid(row=5,column=3, sticky=tk.EW , padx=0)
btn_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=5, font=(FONT,FONT_SIZE)).grid(row=4,column=1, sticky=tk.EW , padx=0)
btn_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=5, font=(FONT,FONT_SIZE)).grid(row=4,column=2, sticky=tk.EW , padx=0)
btn_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=5, font=(FONT,FONT_SIZE)).grid(row=4,column=3, sticky=tk.EW , padx=0)
btn_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=5, font=(FONT,FONT_SIZE)).grid(row=3,column=1, sticky=tk.EW , padx=0)
btn_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=5, font=(FONT,FONT_SIZE)).grid(row=3,column=2, sticky=tk.EW , padx=0)
btn_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=5, font=(FONT,FONT_SIZE)).grid(row=3,column=3, sticky=tk.EW , padx=0)

# math buttons
btn_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=5, font=(FONT,FONT_SIZE)).grid(row=2,column=4, sticky=tk.EW , padx=0)
btn_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=5, font=(FONT,FONT_SIZE)).grid(row=3,column=4, sticky=tk.EW , padx=0)
btn_multi = tk.Button(window, text="*", command=lambda: add_to_calculation("*"), width=5, font=(FONT,FONT_SIZE)).grid(row=4,column=4, sticky=tk.EW , padx=0)
btn_dev = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width=5, font=(FONT,FONT_SIZE)).grid(row=5,column=4, sticky=tk.EW , padx=0)

# func buttons
btn_eval = tk.Button(window, text="=", command=lambda: evaluate_calculation(), width=5, font=(FONT,FONT_SIZE)).grid(row=6,column=3,columnspan=2, sticky=tk.EW, padx=0)
btn_clear = tk.Button(window, text="AC", command=lambda: clear_field(), width=5, font=(FONT,FONT_SIZE)).grid(row=2,column=1, columnspan=2, sticky=tk.EW , padx=0)
btn_negative = tk.Button(window, text="+/-", command=lambda: make_negative(), width=5, font=(FONT,FONT_SIZE)).grid(row=2,column=3, sticky=tk.EW, padx=0)

window.mainloop()
