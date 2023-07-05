#!/usr/bin/env python3

"""
This program organizes files in a folder according to their extension name into a new created folder.
The new folder is named 'Auto-Organized' followed by date and time at that instance.

Usage :-
For organizing:   python3 organizer.py
For unorganizng (i.e. undo the last organize command):  python3 organizer.py -u 


"""
from pathlib import Path
import shutil
from datetime import datetime 
import sys

#------------------------------------------------------
def deco_while_function(f):
	def wrapper():
		while 1:
			try:
				f()
				break
			except Exception as exc:
				print(exc)
				continue
			except KeyboardInterrupt:
				return
	return (wrapper)

@deco_while_function
def organize():
	ans = input("Do you want to proceed organising files by extensions? Y / N\n")
	if ans.lower() not in ['y','n']:
		raise ValueError("Incorrect format")
	if ans.lower()	 == "y":
		print("Lets go")
	else:
		print("Calm down")
#---------------------------------------------------

# For now only the funciton below works for organizing things, the above functionalties to be completed"

def organize_all(script_name):
	p = Path()
	p_org = p / ('Auto-Organized-' + str(datetime.now().replace(microsecond = 0))) 
	p_org.mkdir()
	for file in p.glob('*'):
		if file.name != script_name and file.is_file():
			file_ext_folder = p_org / ('Files ' + file.suffix[1:])
			try:
				file.rename(file_ext_folder / (file.name))
			except FileNotFoundError:
				file_ext_folder.mkdir()
				file.rename(file_ext_folder / (file.name))
	print("Done")


def undo_organize_all():
	p = Path()
	prefix = 'Auto-Organized-'
	for pth in p.glob('*'):
		if prefix in str(pth):
			for file in pth.glob('*/*'):
				if file.is_file():
					file.rename(p / (file.name))
			pth.rmdir()
	Print("Undone") 





def main():
	if len(sys.argv) == 2 and sys.argv[1] == '-u':
		undo_organize_all()
	else:
		organize_all(sys.argv[0])


if __name__ == '__main__':
	main()
