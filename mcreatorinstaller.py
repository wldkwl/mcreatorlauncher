import configparser
import os
import shutil
import subprocess
import sys
import threading
import time
import tkinter
import zipfile
from pathlib import Path
from tkinter import DoubleVar, filedialog, messagebox, ttk
from urllib.parse import urlparse

import requests

versions = [
    "2023.3", "2023.2", "2023.1", "2022.3", "2022.2", "2022.1", "2021.3",
    "2021.2", "2021.1", "2020.5", "2020.4", "2020.3", "2020.2"
]

savedfolder = ""
currentdownloadingversion = ""

config = configparser.ConfigParser()
config.read('settings.ini')
try: 
  savedfolder = config['DEFAULT']['SavedPath']
except KeyError:
  config['DEFAULT'] = {'SavedPath': '/'}
  config['VERSIONS'] = {'2023.3': 'notdownloaded',
                        '2023.2': 'notdownloaded',
                        '2023.1': 'notdownloaded',
                        '2022.3': 'notdownloaded',
                        '2022.2': 'notdownloaded',
                        '2022.1': 'notdownloaded',
                        '2021.3': 'notdownloaded',
                        '2021.2': 'notdownloaded',
                        '2021.1': 'notdownloaded',
                        '2020.5': 'notdownloaded',
                        '2020.4': 'notdownloaded',
                        '2020.3': 'notdownloaded',
                        '2020.2': 'notdownloaded'}
# if config['DEFAULT']['SavedPath']:
#  
# else:
#   savedfolder = config['DEFAULT']['SavedPath']

window = tkinter.Tk()
window.title("MCreator Launcher")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

if getattr(sys, 'frozen', False):
    photo = tkinter.PhotoImage(file=os.path.join(sys._MEIPASS, "files/launchericon.png"))
else:
    photo = tkinter.PhotoImage(file = "files/launchericon.png")
window.iconphoto(False, photo)

progress_var = DoubleVar()

def downloadbutton_event():
  global currentdownloadingversion
  print("downloadbutton pressed")
  match optionmenu.get():
    case "2023.3":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2023.3.36712/MCreator.2023.3.Windows.64bit.zip",))
      currentdownloadingversion = "2023.3"
      fetchthread.start()
      # fetch_zip_file(
      #   savedfolder+"/",
      #   "https://github.com/MCreator/MCreator/releases/download/2023.3.36712/MCreator.2023.3.Windows.64bit.zip"
      # )
    case "2023.2":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2023.2.24119/MCreator.2023.2.Windows.64bit.zip",))
      currentdownloadingversion = "2023.2"
      fetchthread.start()
      # fetch_zip_file(
      #   savedfolder+"/",
      #   "https://github.com/MCreator/MCreator/releases/download/2023.2.24119/MCreator.2023.2.Windows.64bit.zip"
      # )
    case "2023.1":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2023.1.10610/MCreator.2023.1.Windows.64bit.zip",))
      currentdownloadingversion = "2023.1"
      fetchthread.start()
      # fetch_zip_file(
      #   savedfolder+"/",
      #   "https://github.com/MCreator/MCreator/releases/download/2023.1.10610/MCreator.2023.1.Windows.64bit.zip"
      # )


    case "2022.3":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2022.3.48217/MCreator.2022.3.Windows.64bit.zip",))
      currentdownloadingversion = "2022.3"
      fetchthread.start()
    case "2022.2":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2022.2.34517/MCreator.2022.2.Windows.64bit.zip",))
      currentdownloadingversion = "2022.2"
      fetchthread.start()
    case "2022.1":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2022.1.20510/MCreator.2022.1.Windows.64bit.zip",))
      currentdownloadingversion = "2022.1"
      fetchthread.start()


    case "2021.3":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2021.3.54000/MCreator.2021.3.Windows.64bit.zip",))
      currentdownloadingversion = "2021.3"
      fetchthread.start()
    case "2021.2":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2021.2.36710/MCreator.2021.2.Windows.64bit.zip",))
      currentdownloadingversion = "2021.2"
      fetchthread.start()
    case "2021.1":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2021.1.18117/MCreator.2021.1.Windows.64bit.zip",))
      currentdownloadingversion = "2021.1"
      fetchthread.start()


    case "2020.5":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/MCreator/MCreator/releases/download/2020.5.47520/MCreator.2020.5.Windows.64bit.zip",))
      currentdownloadingversion = "2020.5"
      fetchthread.start()
    case "2020.4":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/Pylo/MCreatorArchive/releases/download/2020.4.32115/MCreator.2020.4.Windows.64bit.zip",))
      currentdownloadingversion = "2020.4"
      fetchthread.start()
    case "2020.3":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/Pylo/MCreatorArchive/releases/download/2020.3.22116/MCreator.2020.3.Windows.64bit.zip",))
      currentdownloadingversion = "2020.3"
      fetchthread.start()
    case "2020.2":
      fetchthread = threading.Thread(target=fetch_zip_file, args=(savedfolder+"/",
        "https://github.com/Pylo/MCreatorArchive/releases/download/2020.2.14217/MCreator.2020.2.Windows.64bit.zip",))
      currentdownloadingversion = "2020.2"
      fetchthread.start()

def optionmenu_event(event):
  choice = event.widget.get()
  if config['VERSIONS'][choice] == "downloaded":
    launchbutton.config(state="enabled")
    removebutton.config(state="enabled")
  else:
    launchbutton.config(state="disabled")
    removebutton.config(state="disabled")

def launchbutton_event():
  subprocess.call(savedfolder+"/MCreator"+optionmenu.get().replace(".", "")+"/mcreator.exe")

def removebutton_event():
  shutil.rmtree(savedfolder+"/"+"MCreator"+str.replace(optionmenu.get(), ".", ""))
  config['VERSIONS'][optionmenu.get()] = "notdownloaded"
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  launchbutton.config(state="disabled")
  removebutton.config(state="disabled")

def browsebutton_event():
  folder = filedialog.askdirectory()
  if folder:
    global savedfolder
    # Read and print the content (in bytes) of the file.
    selectedfile.config(text=f"Selected folder: {folder}")
    savedfolder = folder
    config['DEFAULT']['SavedPath'] = folder
    with open('settings.ini', 'w') as configfile:
      config.write(configfile)
    downloadbutton.config(state="enabled")
  else:
    print("No file selected.")

def fetch_zip_file(folderpath, url):
  # Try to get the ZIP file
  statusframe.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
  try:
    response = requests.get(url, stream=True)
    responsecontent = response.content
    total_length = response.headers.get('content-length')
    dl = 0
    total_length = int(total_length)
    for data in response.iter_content(chunk_size=4096):
      dl += len(data)
      done = int(100 * dl / total_length)
      progress_var.set(done)
      statusframe.config(text="Status: Downloading")
  except OSError:
    print('No connection to the server!')
    return None

  # check if the request is succesful
  if response.status_code == 200:
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = os.path.basename(path)
    if filename.endswith(".zip"):
      print('Status 200, OK', os.path.join(os.path.expanduser('~'),folderpath + filename))
      with open(os.path.join(os.path.expanduser('~'),folderpath + filename), 'wb') as file:
        file.write(responsecontent)
      extractthread = threading.Thread(target=extract_version, args=(folderpath + "/" + filename,))
      extractthread.start()
  else:
    print('ZIP file request not successful!.')
    return None

def extract_version(versionzip):
  progress_var.set(0)
  with zipfile.ZipFile(versionzip, 'r') as zip_ref:
    uncompress_size = sum((file.file_size for file in zip_ref.infolist()))
    extracted_size = 0
    for file in zip_ref.infolist():
      extracted_size += file.file_size
      done = (extracted_size * (100/uncompress_size))
      progress_var.set(done)
      statusframe.config(text="Status: Extracting")
      
      if file.filename.startswith("MCreator"+str.replace(currentdownloadingversion, ".", "")):
        zip_ref.extract(file, savedfolder)
      else:
        zip_ref.extract(file, savedfolder+"/"+"MCreator"+str.replace(currentdownloadingversion, ".", ""))
  config["VERSIONS"][currentdownloadingversion] = "downloaded"
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  if optionmenu.get() == currentdownloadingversion:
    launchbutton.config(state="enabled")
    removebutton.config(state="enabled")
  statusframe.grid_forget()
  os.remove(versionzip)

mainframe = tkinter.LabelFrame(frame, text="Version")
mainframe.grid(row=0, column=0, padx=20, pady=20)

optionmenu = ttk.Combobox(mainframe, values=versions)
optionmenu.set("2023.3")
optionmenu.grid(row=0, column=0)
optionmenu.bind("<<ComboboxSelected>>", optionmenu_event)

selectedfile = ttk.Label(mainframe, text="Selected folder: NONE")
selectedfile.grid(row=1, column=0, sticky="w")

selectbutton = ttk.Button(mainframe, text="Browse", command=browsebutton_event)
selectbutton.grid(row=1, column=1)

launchbutton = ttk.Button(mainframe,
                          text="Launch",
                          command=launchbutton_event,
                          state="disabled")
launchbutton.grid(row=2, column=0, sticky="w")

removebutton = ttk.Button(mainframe,
                          text="Uninstall",
                          command=removebutton_event,
                          state="disabled")
removebutton.grid(row=0, column=1, sticky="")

downloadbutton = ttk.Button(mainframe,
                            text="Download",
                            command=downloadbutton_event,
                            state="disabled")
downloadbutton.grid(row=2, column=1, sticky="w")

statusframe = tkinter.LabelFrame(frame, text="Status")
statusframe.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
statusframe.columnconfigure(0, weight=1)
statusframe.grid_forget()

statusprogress = ttk.Progressbar(statusframe, variable=progress_var, maximum=100)
statusprogress.grid(row=0, column=0, sticky="ew")

for widget in mainframe.winfo_children():
  widget.grid_configure(padx=10, pady=5)

for widget in statusframe.winfo_children():
  widget.grid_configure(padx=10, pady=5)

if savedfolder:
  selectedfile.config(text=f"Selected folder: {savedfolder}")
  downloadbutton.config(state="enabled")

if config['VERSIONS'][optionmenu.get()] == "downloaded":
  launchbutton.config(state="enabled")
  removebutton.config(state="enabled")

window.mainloop()