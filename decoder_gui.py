import tkinter as tk
from tkinter import filedialog, messagebox
from decode import extract_message

window = tk.Tk()                                        #Spawns the window.
window.title("🔓 Reveal Secret Message (Decoder)")      #Labels the window so the receiver knows this is the Decoder.
window.geometry ("500x520")                              
window.configure(bg="#1a1d24")                          #Keeps the window alive on screen.


# THE IMAGE PICKER FUNCTION
selected_image_path =""                                                     

def select_image():
    global selected_image_path 
    path= filedialog.askopenfilename(
        title="select Encrypted image ",
        filetypes=[("PNG IMAGE","*.png"),("All Image","*.png;*.jpg;.jpeg")]
        
    )
    if path:
        selected_image_path=path
        image_label.config(
            text=f"✅ Loaded:{path.split('/')[-1]}",
            fg="#00e5ff",
            font=("Helvetica",10,"bold")

        )

def on_browse_enter(e):
    browse_btn.config(bg="#22d3ee")

def on_browse_leave(e):
    browse_btn.config(bg="#00b4d8")


browse_btn=tk.Button(
    window,
    text="📁  SELECT ENCRYPTED IMAGE",
    command=select_image,
    bg ="#22d3ee",
    fg="white",
    font=("Helvetica",11,"bold"),
    relief="sunken", bd=9,
    activebackground="white",
    activeforeground="white",
    padx=20,
    pady=8,
    cursor="hand2"
)
browse_btn.pack(pady=(25,10))

browse_btn.bind("<Enter>",on_browse_enter)
browse_btn.bind("<Leave>",on_browse_leave)

image_label=tk.Label(
    window,
    text="No Image selected",
    bg="#1a1d24",
    fg="#94a3b8",
    font=("Helvetica",9)

)
image_label.pack()

key_label=tk.Label(
    window,
    text="ENTER SECRET PIN (NUMBER):",
    bg="#1a1d24",
    fg="#ffffff",
    font=("Helvetica",10,"bold")
)

key_label.pack(pady=(25,5))

key_entry=tk.Entry(
    window,
    width=35,
    font=("Helvetica",12),
    bg="#242936",
    fg="white",
    insertbackground="#00E5FF",
    relief="sunken",bd=9
)
key_entry.pack(ipady=6)
def decode_and_reveal():
    if not selected_image_path:
        messagebox.showerror("Error","please select an encrypted image")
        return

    pin_text=key_entry.get()
    if not pin_text.isdigit():
        messagebox.showerror("Error","please enter a valid number for the PIN!")
        return

    pin=int(pin_text)    

    success,secret=extract_message(selected_image_path,pin)

    if success:
        result_box.config(

            text=secret,
            fg="#00E5FF",
            font=("Helvetica",12,"bold")
        )
        messagebox.showinfo("success 🎉", "Secret message revealed!")
    else:
        result_box.config(

            text="[Failed to decode:wrong PIN or image ]",
            fg="#ff5252",
            font=("Helvetica",10,"italic")
        )
    
        messagebox.showerror("Failed ❌", secret)

         
reveal_btn=tk.Button(
    window,
    text="🔓  REVEAL SECRET MESSAGE",
    command=decode_and_reveal,
     bg="#11998e",
    fg="white",
    font=("Helvetica", 12, "bold"),
    relief="raised",
    bd=3,
    activebackground="#38ef7d",
    padx=20,
    pady=10,
    cursor="hand2"

)
reveal_btn.pack(pady=20)

result_title = tk.Label(
    window,
    text="HIDDEN MESSAGE:",
    bg="#1a1d24",
    fg="#94a3b8",
    font=("Helvetica", 10, "bold")
)
result_title.pack(pady=(10, 5))
# 4. Result Display Box (where the secret appears!):
result_box = tk.Label(
    window,
    text="[ Your secret message will appear here ]",
    bg="#242936",
    fg="#00E5FF",
    font=("Helvetica", 11, "italic"),
    width=40,
    height=3,
    relief="sunken",
    bd=2
)
result_box.pack(pady=5)













window.mainloop()