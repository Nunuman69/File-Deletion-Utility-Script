# 🧹 Duplicate File Remover

This Python script helps you clean up duplicate files in a folder by identifying files with the same base name (e.g., `file.txt`, `file (1).txt`, `file (2).txt`) and **deleting the duplicates**, keeping only the first/original file.

---

## 📁 How It Works

1. The script scans all files in the specified directory.
2. It uses a regular expression to detect duplicate file patterns (e.g., `filename (1).txt`, `filename (2).txt`).
3. It keeps only the first instance of each file and deletes the rest.

---

## 🧠 Duplicate Detection Logic

The script uses this regular expression to group duplicates:

```python
(.+?)(?: \(\d+\))?(\.[^\.]+)$
```

Explanation:
- `(.+?)` — Captures the base filename.
- `(?: \(\d+\))?` — Matches suffixes like `(1)`, `(2)`, etc.
- `(\.[^\.]+)` — Matches the file extension (e.g., `.txt`, `.jpg`).

This helps group files like:
- `document.pdf`
- `document (1).pdf`
- `document (2).pdf`

---

## ⚙️ How to Use

### 1. Update the directory path

Open the script and update this line with the folder path you want to clean:

```python
directory_path = r'd:\TEST FOLDER'  # Change this to your target folder
```

### 2. Run the script

```bash
python remove_duplicates.py
```

It will:
- Print the name of each deleted duplicate.
- Confirm when the operation is complete.

---

## 📌 Example

### Before Running:
```
image.png
image (1).png
image (2).png
notes.txt
notes (1).txt
```

### After Running:
```
image.png
notes.txt
```

---

## ⚠️ Important Notes

- This script deletes files **permanently** from the folder.
- It identifies duplicates **based on filename patterns only**, not by comparing file content.
- **Backup your files** before running, especially if you're unsure.

---

## 🖥 Requirements

- Python 3.x installed on your machine
- Basic understanding of modifying Python scripts

---

## 🙋‍♂️ Author

Created by Ahsan Uddin 
Feel free to contribute or suggest improvements!
