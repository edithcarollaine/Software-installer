import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Pacotes disponíveis para instalação
software_options = {
    "7-Zip": "7zip.7zip",
    "VLC": "VideoLAN.VLC",
    "Winamp": "Winamp.Winamp",
    "Google Chrome": "Google.Chrome",
    "Mozilla Firefox": "Mozilla.Firefox",
    "Notepad++": "Notepad++",
    "Git": "Git.Git",
    "Python 3.12": "Python.Python.3.12",
    "Steam": "Valve.Steam",
    "Microsoft Teams": "Microsoft.Teams"
}

# Caminho base para pastas padrão
base_folder = r"C:\Users\Edith Carollaine\OneDrive\Documentos\pasta teste"

# Pastas padrão
folders = [
    os.path.join(base_folder, "Projetos"),
    os.path.join(base_folder, "Suporte"),
    os.path.join(base_folder, "Logs")
]

# Variável de ambiente
env_var_name = "SUPORTE_PATH"
env_var_value = base_folder

# Funções principais
def install_selected_packages():
    selected = [key for key, var in check_vars.items() if var.get()]
    if not selected:
        messagebox.showwarning("Aviso", "Selecione pelo menos um software para instalar!")
        return

    for software in selected:
        pkg_id = software_options[software]
        print(f"Installing {software} ({pkg_id})...")
        subprocess.run(["winget", "install", "--id", pkg_id, "-e", "--silent"])

    messagebox.showinfo("Sucesso", "Instalação concluída!")

def create_folders_gui():
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder created: {folder}")
    messagebox.showinfo("Sucesso", "Pastas criadas com sucesso!")

def set_env_var_gui():
    subprocess.run(f'setx {env_var_name} "{env_var_value}"', shell=True)
    messagebox.showinfo("Sucesso", f"Variável de ambiente {env_var_name} configurada!")

# Criando interface
root = tk.Tk()
root.title("Windows Initial Configuration")
root.geometry("500x500")

tk.Label(root, text="Selecione os softwares para instalar:", font=("Arial", 12)).pack(pady=10)

# Frame com scrollbar para os checkboxes
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Adicionando checkboxes dinamicamente
check_vars = {}
columns = 2  # Ajustável: número de colunas de softwares
row = 0
col = 0
for software in software_options:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(scrollable_frame, text=software, variable=var)
    chk.grid(row=row, column=col, sticky='w', padx=10, pady=5)
    check_vars[software] = var

    col += 1
    if col >= columns:
        col = 0
        row += 1

# Texto informativo
label_info = tk.Label(root, text="Pastas padrão e variável de ambiente serão criadas automaticamente.", font=("Arial", 10))
label_info.pack(pady=10)

# Botão configurável
btn_configure = tk.Button(root, text="Configurar Tudo", command=install_selected_packages, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_configure.pack(fill="x", padx=50, pady=10)

root.mainloop()
