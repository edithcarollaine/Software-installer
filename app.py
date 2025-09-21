import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Pacotes disponíveis para instalação
software_options = {
    "7-Zip": "7zip.7zip",
    "VLC": "VideoLAN.VLC",
    "Winamp": "Radionomy.Winamp",
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
root.geometry("400x450")

tk.Label(root, text="Selecione os softwares para instalar:", font=("Arial", 12)).pack(pady=10)

check_vars = {}
for software in software_options:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=software, variable=var)
    chk.pack(anchor='w')
    check_vars[software] = var

tk.Button(root, text="Instalar Softwares Selecionados", command=install_selected_packages, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Criar Pastas Padrão", command=create_folders_gui, bg="#2196F3", fg="white").pack(pady=10)
tk.Button(root, text="Configurar Variável de Ambiente", command=set_env_var_gui, bg="#f39c12", fg="white").pack(pady=10)

root.mainloop()
