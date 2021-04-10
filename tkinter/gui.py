from tkinter import *


#criar uma nova janela
window = Tk()

#seta o titulo da janela
window.title('Meu programa')

entry_text = Entry(window, width = 30)

#entrada vde texto
entry_text.pack()
entry_text.focus_set()

#tamanho da janela 
window.geometry('300x150')
def click_button():
    print(entry_text.get())
    
btn = Button(window, text='Clique Aqui', width=20, command=click_button)
btn.pack()
window.mainloop()