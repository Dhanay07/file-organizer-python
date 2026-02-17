import os
import shutil

path = "C:/Users/Asgard/Downloads"

folders = {
	"Images": [".jpg", ".jpeg", ".png", ".gif"],
	"Documents": [".pdf", ".docx", ".txt"],
	"Videos": [".mp4", ".mkv"],
	"Music": [".mp3", ".wav"],
	"Program": [".exe", ".msi"],
	"Zip": [".zip"]
}

for folder in folders:
	folder_path = os.path.join(path, folder)
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

files = os.listdir(path)

for file in files:
	file_path = os.path.join(path, file)

	if os.path.isfile(file_path):
		for folder, extensions in folders.items():
			if file.lower().endswith(tuple(extensions)):
				dest = os.path.join(path, folder, file)
				shutil.move(file_path, dest)
				break
print("Files organized successfully ")