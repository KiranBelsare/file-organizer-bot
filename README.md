# 📂 File Organizer Bot 🔄

A Python mini project that **automatically organizes messy folders** by sorting files into folders based on their type (images, documents, code files, etc).

---

## 🛠️ What It Does

- Loops through all files in a folder
- Detects file types using extensions
- Automatically creates folders like:
  - `Images/`
  - `Documents/`
  - `Python Files/`
  - `Others/`
- Moves files into their respective folders

---

## 📁 File Types Handled

| File Type      | Folder Created   |
|----------------|------------------|
| `.png`, `.jpg` | `Images`         |
| `.pdf`, `.txt` | `Documents`      |
| `.py`          | `Python Files`   |
| others         | `Others`         |

---

## 💻 Technologies Used

- Python 3
- `os` module
- `shutil` module

---

## 🚀 How to Run

```bash
1. Place this script in the folder containing your files
2. Update `folder_path` in the script if needed
3. Run it:
   python3 file_organizer.py

🧠 Motivation

I built this as part of my Python Bootcamp journey to master file handling, automation, and real-world logic.
This is my first hands-on project where I understood every single line — and published it proudly 💪✨

👩‍💻 Author

Made with love by @KiranBelsare 💻👑
Let’s build the empire. 🚀

