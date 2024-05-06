import tkinter as tk 
#Calculator logic 

calculation = ""

def add_to_calculation(symbol):
    global calculation
    
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evalutate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Erro")
        pass
    
    
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("New Time Roman", 24))
text.result.grid(columnspan=5)
root.mainloop()
