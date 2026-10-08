import tkinter as tk
from tkinter import filedialog, messagebox
from new import hide_message



window=tk.Tk()
window.title("🔒 Hide Secret Message (Encoder)")
window.geometry("500x500")

window.configure(bg="#1a1d24")  


selected_image_path=""
def select_image():
    global selected_image_path
    path=filedialog.askopenfilename(
        title="select an image",
        filetypes=[("image files ","*.png;*.jpg;*.jpeg")]
    )

    if path:
        selected_image_path = path
        # Success animation: turn bold green with checkmark!
        image_label.config(
            text=f"✅ Loaded: {path.split('/')[-1]}", 
            fg="#2E7D32", 
            font=("Arial", 10, "bold")
        )



def on_enter(e):
    browser_btn.config(bg="#22d3ee")

def on_leave(e):
    browser_btn.config(bg="#00b4d8")

browser_btn =tk.Button(
   window,
   text="📁  BROWSE IMAGE",
   command=select_image,
   bg="#00b4d8",
   fg="white",
   font=("helvetica ",11,"bold"),
   relief="flat",
   activebackground="#22d3ee",
   activeforeground="white",
   padx=20,
   pady=8,
   cursor="hand2"
)
browser_btn.pack(pady=15)
browser_btn.bind("<Enter>",on_enter)
browser_btn.bind("<Leave>",on_leave)

image_label=tk.Label(window,text="no image selected ",bg="#1a1d24",fg="#94a3b8",font=("hellvetica",9))
image_label.pack()
#secret message input

msg_label=tk.Label(
    window,
    text="Enter secret message",
    bg="#054336",
    fg="#fffffe",
    font=("Helvetica",10,"bold")
)

msg_label.pack(pady=(20,5))

msg_entry=tk.Entry(
window,
width=35,
font=("helvetica",12),
bg="#242936",
fg="white",
insertbackground="#00E5FF",
relief="flat"
)
msg_entry.pack(ipady=6)

#pin label
key_label=tk.Label(
text="enter secret pin(number):",
bg="#1a1d24",
fg="#ffffff",
font=("helvetica",10,"bold")

)
key_label.pack(pady=(15,5))

key_entry=tk.Entry(
 window,
 width=35,
 font=("helvetica",12),
 bg="#242936",
 fg="white",
 insertbackground="#00E5FF",
 relief="flat"

)
key_entry.pack(ipady=6)

def encode_and_save():
   if not selected_image_path:
       messagebox.showerror("error","please select an image first!")
       return

   message=msg_entry.get()
   if not message:
       messagebox.showerror("error","please enter a secrect message!")
       return

   pin_text=key_entry.get()
   if not pin_text.isdigit():
        messagebox.showerror("error","pin must be a valid number (e.g.1234)!")
        return

   pin = int(pin_text)

   save_path=filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("png image","*.png")],
            initialfile="secret.png",
            title="save secret iamge as"

        )
   if not save_path:
        
        return

   success,result_text=hide_message(selected_image_path,message,pin,save_path)

   if success:
        messagebox.showinfo("Success 🎉", "Secret message hidden successfully inside your image!")
   else:
        messagebox.showerror("Failed ❌", result_text)

encode_btn=tk.Button(
    window ,
    text="🔒  HIDE & SAVE IMAGE",
    command=encode_and_save,
    bg="#11998e",
    fg=("white"),
    font=("helvetica",12,"bold"),
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"

)
encode_btn.pack(pady=30)
















window.mainloop()