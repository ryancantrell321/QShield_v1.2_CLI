# Pandora QShield

![Logo](https://i.ibb.co.com/VYr8X9p/Logo.png)

## Version: 1.2 CLI  
### Release: January 2025  
#### © RyanCantrell321, Pandora Dynamics  
#### License: [GNU General Public License (GPL) v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

![Python 3.12](https://img.shields.io/badge/python-3.12-darkgreen)  ![GPL v3.0](https://img.shields.io/badge/GPL-v3.0-orangered) ![GitHub Downloads](https://img.shields.io/github/downloads/ryancantrell321/QShield_v1.2_CLI/total)

---

## ⬇️ Downloads
[Download QShield_v1.2](https://github.com/ryancantrell321/QShield_v1.2_CLI/releases)

---

## About

Welcome to **Pandora QShield CLI** – a user-friendly backup and restore solution designed to keep your qBittorrent settings secure! With Pandora QShield, you can safely back up and restore your application settings, ensuring your preferences and configurations are preserved during Windows reinstallation, migration, or qBittorrent reinstallation.

---

## 🎯 Key Features
- **Portability:** No installation required.
- **Secure Backup & Restore:** Easily save and restore qBittorrent settings to a location of your choice.
- **Performance Optimization:** Multi-instance defense mechanism and memory efficiency algorithm.
- **Precise Event Logs:** Includes a logging system to record all actions for easy debugging.

---

## 📥 Minimum System Requirements
- Intel or AMD processors (post-2014)
- 64-bit Windows 10 Update 2020++ or Windows 11
- RAM: 6 GB or better
- qBittorrent version 4.0 or newer
- Free disk space: 5 GB or more

> **NOTE:** NOT TESTED ON ARM64 PROCESSORS.

---

## 🐞 Known Bugs
In some devices, qBittorrent may lose internet connectivity after a restore. To resolve this, manually set the connection interface in qBittorrent to **"Any Interface"**:  

#### qBittorrent > Settings > Advanced > Network Interface > Any Interface


We plan to address this bug in a future update.

---

## 📚 How to Install Python (For Method 1):
### Install Python version 3.11.11, 3.12.8 or 3.13.1:
- Download from [python.org/downloads/windows](https://www.python.org/downloads/windows/)
- During installation, check "Add python.exe to PATH" 

---

## 📚 How to Run (3 Methods: The choice is yours)

### Method 1: Using python, directly from the source
**QShield is portable. No installation needed. Follow these steps:**
1. Download `qShield_v1.2(source).zip`.
2. Extract the downloaded `.zip` file.
3. Open the folder named `qShield_v1.2`.
4. Open `Windows Powershell/Windows Terminal/CMD` as `admin`
5. `cd` into the directory you extracted the folder to. Example: `cd D:\Backups\qShield_v1.2`
6. Type in the following `pip install -r requirements.txt` and press `Enter`
7. Type in the following `python main.py` and press `Enter`
8. Enjoy.

#### Note: If you are not interested in such heavy technicalities, please check Method 2 and 3


### Video Tutorial (Method 1)
[![Watch Video](https://i.ibb.co.com/BLchYdC/Picture1.png)](https://www.youtube.com/watch?v=mZEZTqEct68)


---

### Method 2: Using .exe
**QShield is portable. No installation needed. Follow these steps:**
1. Download `qShield_v1.2.zip`.
2. Extract the downloaded `.zip` file.
3. Open the folder named `qShield_v1.2`.
4. Double-click `qShield_v1.2.exe` and grant admin privileges.

### Video Tutorial (Method 2)
[![Watch Video](https://i.ibb.co.com/BLchYdC/Picture1.png)](https://www.youtube.com/watch?v=mZEZTqEct68)


---
### Method 3: Using GUI [Full of User Interface Bugs]
Visit GitHub repository for the GUI version to learn more: [ryancantrell321/Pandora_QShield](https://github.com/ryancantrell321/Pandora_QShield)

---

## 💻 Usage

### General Guidelines
- Path strings must be entered without quotation marks.  
- Paths can include underscores but must not contain spaces or hyphens.  
- Ensure your disk directories remain in the same location as when the data was backed up.

### Backup Instructions
1. Press `1` for backup.  
   The software retrieves data from the following directories:  
   - `%localappdata%\qBittorrent`
   - `%appdata%\qBittorrent`
2. Specify a location to save the backup.  
   The location must exist and cannot include spaces or hyphens (underscores are allowed).
3. The backup process will proceed.

### Restore Instructions
1. Press `2` to restore.  
   The tool will automatically extract data from the `.zip` file it previously created and restore it to the original directories.
2. Specify the file path and name of the `.zip` file.
3. **Important:** Ensure qBittorrent is completely closed before restoring data.

---

## 📷 Screenshots and Usage Video

### Screenshots
![Screenshot 1](https://i.ibb.co.com/BLchYdC/Picture1.png)  
![Screenshot 2](https://i.ibb.co.com/SmK2HfP/Picture2.png)  
![Screenshot 3](https://i.ibb.co.com/xh7Ht7Q/Picture3.png)  
![Screenshot 4](https://i.ibb.co.com/YNsch2T/Picture4.png)

---

## ⚠️ With Great Power Comes Great Responsibility!
Use this data deletion tool only if you experience qBittorrent interface corruption.  

[Download qShield Deleter](https://github.com/ryancantrell321/qShield_Deleter/releases/)

---

## 📑 License
Pandora QShield is licensed under the [GNU General Public License (GPL) v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🌐 Future Enhancements
- Password-protected secure backups.
- Cloud storage support.

---

## 💿 Virus Scan Results

#### Avast! and its affiliates might produce false positives! 

| File Name        | Virus Scan Link         |
|------------------|-------------------------|
| qShield_v1.2.zip | [Scan Result](https://virusscan.jotti.org/en-US/filescanjob/jqk8wp2jer) |
| qShield_v1.2.exe | [Scan Result](https://virusscan.jotti.org/en-US/filescanjob/b6nifv86j2)         |

---

## 📞 Contact Us
- **Email:** [pandoradynamics@gmail.com](mailto:pandoradynamics@gmail.com)  
- **Facebook:** [Pandora Dynamics](https://facebook.com/pandoradynamics22)  
- **Instagram:** [Pandora Dynamics](https://instagram.com/pandoradynamics22)  

![Pandora Dynamics Logo](https://i.ibb.co.com/gTnpSd6/Pandora-Dynamics-Logo-5-1.png)
