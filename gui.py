import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
from password_manager import add_password, get_password, list_services, delete_password

masterPass= "password"

def add_password_gui():
    service = simpledialog.askstring("Nuevo Servicio", "Introduce el nombre del servicio:")
    if not service:
        return
    password = simpledialog.askstring("Nueva Contraseña", f"Introduce la contraseña para {service}:")
    if not password:
        return
    add_password(service, password)
    messagebox.showinfo("Éxito", f"Contraseña para {service} guardada correctamente.")

def retrieve_password_gui():
    service = simpledialog.askstring("Recuperar Contraseña", "Introduce el nombre del servicio:")
    if not service:
        return
    password = get_password(service)
    if password:
        messagebox.showinfo("Contraseña Recuperada", f"Contraseña para {service}: {password}")
    else:
        messagebox.showwarning("Error", "Servicio no encontrado.")

def list_services_gui():
    services = list_services()
    if services:
        messagebox.showinfo("Servicios", f"Servicios almacenados: {', '.join(services)}")
    else:
        messagebox.showinfo("Servicios", "No hay servicios almacenados.")

def delete_password_gui():
    service = simpledialog.askstring("Eliminar Servicio", "Introduce el nombre del servicio:")
    if not service:
        return
    if delete_password(service):
        messagebox.showinfo("Éxito", f"Servicio {service} eliminado correctamente.")
    else:
        messagebox.showwarning("Error", "Servicio no encontrado.")

def main_gui():
    master_password = simpledialog.askstring("Contraseña Maestra", "Introduce la contraseña maestra:", show="*")
    if master_password != masterPass:
        messagebox.showerror("Acceso Denegado", "Contraseña incorrecta.")
        return

    root = tk.Tk()
    root.title("PyVault")
    root.geometry("850x550")
    root.configure(bg="#363636")
    root.resizable(False, False)

    banner_image = Image.open(".\\vault.png") 
    banner_image = banner_image.resize((850, 200), Image.Resampling.LANCZOS) 
    banner_photo = ImageTk.PhotoImage(banner_image)
    banner_label = tk.Label(root, image=banner_photo, bg="#363636")
    banner_label.image = banner_photo 
    banner_label.pack(fill=tk.BOTH)

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14), padding=10, relief="flat", background="#4CAF50", foreground="black", anchor="center", width=20)

    ttk.Button(root, text="Agregar Nueva Contraseña", command=add_password_gui, style="TButton").pack(fill=tk.X, padx=20, pady=5)
    ttk.Button(root, text="Recuperar Contraseña", command=retrieve_password_gui, style="TButton").pack(fill=tk.X, padx=20,  pady=5)
    ttk.Button(root, text="Listar Servicios", command=list_services_gui, style="TButton").pack(fill=tk.X, padx=20,  pady=5)
    ttk.Button(root, text="Eliminar Servicio", command=delete_password_gui, style="TButton").pack(fill=tk.X, padx=20,  pady=5)
    ttk.Button(root, text="Salir", command=root.quit, style="TButton").pack(fill=tk.X, padx=300,  pady=10)

    root.mainloop()
