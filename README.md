# Windows Initial Configuration Tool

A simple Python-based GUI tool to automate the installation of common software, create standard folders, and set an environment variable on Windows machines.

This tool is ideal for **IT support technicians** or anyone who wants to quickly set up a Windows environment for work or development.

---

## 📦 Requirements

- Python 3.8+ (if you want to run the original script).
- Standard Python libraries:
- `os`
- `tkinter`

⚠️ No extra dependencies are required.

## Features

- Install multiple applications using [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/).
- Create standard folders for projects, logs, and support files.
- Automatically set an environment variable pointing to the base folder.
- User-friendly GUI with checkboxes to select the software to install.
- Scrollable and dynamic layout that adapts to the number of applications.

---

## Included Software

The following applications are available for installation:

| Application     | Winget ID            |
| --------------- | -------------------- |
| 7-Zip           | `7zip.7zip`          |
| VLC             | `VideoLAN.VLC`       |
| Winamp          | `Winamp.Winamp`      |
| Google Chrome   | `Google.Chrome`      |
| Mozilla Firefox | `Mozilla.Firefox`    |
| Notepad++       | `Notepad++`          |
| Git             | `Git.Git`            |
| Python 3.12     | `Python.Python.3.12` |

> Note: The list of available applications can be updated directly in the script.

---

## ▶️ How to Run

There are **two ways** to use this tool:

🔹 **Option 1 — Run with Python**

1. Clone or download this repository.
2. Make sure you have Python 3.8+ installed.
3. Run the script in terminal/cmd:

```bash
python setup_gui.py
```

🔹 **Option 2 — Use the Executable (Recommended)**  
Download the ready-to-use Windows executable:  
👉 [Download instalador.exe](https://www.dropbox.com/scl/fi/2dreycxofsiunbj8zck0c/instalador.exe?rlkey=uwqae1gqmd4b4w966z82v3w86&st=w6v9lqib&dl=0)

After downloading, simply **double-click on `instalador.exe`** to open the interface.

> **Important:** Run as Administrator to allow Winget to install software.
