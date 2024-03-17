from map_data import *
import customtkinter
from PIL import Image
import time
app=customtkinter.CTk()
app.title("Gmap Vigilante")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}")

entry = customtkinter.CTkEntry(app, placeholder_text="Enter Input(Eg. Gift Shop In Chennai)...",font=("arial",20),width=930,height=10,fg_color=app.cget("bg"),border_color=app.cget("bg"))
entry.pack(anchor='center',pady=(300,0))
canvas = customtkinter.CTkCanvas(app,width=1000,height=0.1)#, bg_color="#00ffff")
canvas.pack()



def opration(event=None):
    loading_text=customtkinter.CTkLabel(app,text="Loading...")
    loading_text.pack(pady=30)
    
    
    text = entry.get()
    if text=="":
        notification.notify(
            title='Invalid Input',
            message="Please Input Any Text To Get Data From Gmaps",
            app_name='Gmap Vigilante',
        )
    else:
        process_init()
        main(text)        
        process_finis(text)
    loading_text.pack_forget()

    print("You entered:", text)
entry.bind("<Return>",opration)

app.mainloop()