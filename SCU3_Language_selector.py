#! /usr/bin/env python2
#Developer: Tetration
#Developers Github address: https://github.com/tetration
#Github repository: https://github.com/tetration/Simcity300_Language_Selector

import os
import shutil
import urllib
import zipfile

def Welcome():
	print("Welcome Simcity 3000 Unlimited Language selector")
	print("This program will help you in changing or adding a new languages inside your") 
	print("Simcity 3000 or Simcity 3000 Unlimited \n")


def check_if_inside_main_game_folder():
	tf=False
		#Checks if its Windows version of the Res folder
	tf=os.path.isdir('SSimData') and os.path.isdir('Text') and os.path.isdir('Hotkeys') and os.path.isdir('Sound')
		#Checks if its Linux version of the Res folder
	tf=os.path.isdir('ssimData') and os.path.isdir('text') and os.path.isdir('hotkeys') and os.path.isdir('sound')
	
	if tf== True:
		print("Simcity 3000 Res directory detected!")
		check_if_language_folder_exists()
	
	else: 
		print("Error this python script is not in the Res directory of Simcity 3000.")
		print("Make sure to place this python script in the Res directory of Simcity 3000 after you exit it")
		input("Press enter to exit")
		
def check_if_language_folder_exists():
	print("Additional Languages folder not detected! Creating it...")
	if os.path.isdir("Additional_Languages")==False:
		os.mkdir("Additional_Languages")
		download_Language_pack()
		extract_and_Delete_zip()

def download_Language_pack():
	print("Downloading extra languages package...")
	urllib.urlretrieve ("https://drive.google.com/uc?export=download&id=1eNZ61IRMv6Xnm8LRTN0trxL7aSpCzU9l","SCU3Languagepack.zip")
	print("Download completed!!")
	

def extract_and_Delete_zip():
	src_file=os.path.join(os.curdir,"SCU3Languagepack.zip")
	extr_file=os.path.join(os.curdir,"Additional_Languages")
	print("Extracting files...")
	zip_ref = zipfile.ZipFile(src_file, 'r')
	zip_ref.extractall(extr_file)
	zip_ref.close()
	print("Extraction complete!")
	print("Deleting zipfile...")
	os.remove(src_file)

def print_menu():
	print("Which Language would you like to put as default?")
	print("1- English")
	print("2- English (United Kingdom)")
	print("3- Portuguese")
	print("4- French")
	print("5- Italian")
	print("6- Spanish")
	print("7- Polish")
	print("8- German")
	print("9- Dutch")
	print("10- Russian")
	print("11- Swedish")
	print("12- Exit Python Script without  making any changes in Simcity 3000 Language")

		
def menu():  
	loop=True
	while loop:          ## While loop which will keep going until loop = False
		print_menu()    ## Displays menu
		choice = input("Enter your choice [1-12]: ")
		if choice==1:     
			print "ENGLISH has been selected"
			switch_Game_language("english")
			## You can add your code or functions here
		elif choice==2:
			print "English (United Kingdom) has been selected"
			switch_Game_language("english-uk")
			## You can add your code or functions here
		elif choice==3:
			print "Portuguese has been selected"
			switch_Game_language("portuguese")
			## You can add your code or functions here
		elif choice==4:
			print "French has been selected"
			switch_Game_language("french")
			## You can add your code or functions here
		elif choice==5:
			print "Italian has been selected"
			switch_Game_language("italian")
		elif choice==6:
			print "Spanish has been selected"
			switch_Game_language("spanish")
		elif choice==7:
			print "Polish has been selected"
			switch_Game_language("polish")
		elif choice==8:
			print "Dutch has been selected"
			switch_Game_language("dutch")
		elif choice==9:
			print "Russian has been selected"
			switch_Game_language("russian")
		elif choice==10:
			print "Swedish has been selected"
			switch_Game_language("swedish")
		elif choice==11:
			print "Exiting the program..."
			## You can add your code or functions here
			loop=False # This will make the while loop to end as not value of loop is set to False
		else:
			# Any integer inputs other than values 1-5 we print an error message
			raw_input("ERROR: Wrong choice please choose an option between 1 to 12 (Press ENTER to try again) \n")


def switch_Game_language(language):

	if os.name =="nt":
		switch_Game_language_Windows(language)
	if os.name=="posix":
		switch_Game_language_Linux(language)

def switch_Game_language_Windows(language):
	#Sources
	source_textFolder=os.path.join(os.curdir,"Additional_Languages\\text\\")+language
	source_hotkeysFolder=os.path.join(os.curdir,"Additional_Languages\\hotkeys\\")+language
	source_ssimdataFolder=os.path.join(os.curdir,"Additional_Languages\\ssimdata\\")+language

	#Destinations
	dest_textFolder=os.path.join(os.curdir,"Text\ENGLISH")
	dest_hotkeysFolder=os.path.join(os.curdir,"Hotkeys\ENGLISH")
	dest_ssimdataFolder=os.path.join(os.curdir,"SSimData\ENGLISH")
	if os.path.isdir(dest_textFolder)==True:
		shutil.rmtree(dest_textFolder)
	#extr_file=os.path.join(os.curdir,"Additional_Languages")
	#os.mkdir(dest_textFolder)
	shutil.copytree(source_textFolder, dest_textFolder)
	shutil.copytree(source_hotkeysFolder, dest_hotkeysFolder)
	shutil.copytree(source_ssimdataFolder, dest_ssimdataFolder)
	os.mkdir(os.path.join(dest_textFolder,language))#Makes a folder with nothing just with the name of the real current language since it wont be possible knowing

def switch_Game_language_Linux(language):
	#Sources
	source_textFolder=os.path.join(os.curdir,"Additional_Languages\\text\\")+language
	source_hotkeysFolder=os.path.join(os.curdir,"Additional_Languages\\hotkeys\\")+language
	source_ssimdataFolder=os.path.join(os.curdir,"Additional_Languages\\ssimdata\\")+language

	#Destinations
	dest_textFolder=os.path.join(os.curdir,"text\english")
	dest_hotkeysFolder=os.path.join(os.curdir,"hotkeys\english")
	dest_ssimdataFolder=os.path.join(os.curdir,"ssimData\english")
	if os.path.isdir(dest_textFolder)==True:
		shutil.rmtree(dest_textFolder)
	#extr_file=os.path.join(os.curdir,"Additional_Languages")
	#os.mkdir(dest_textFolder)
	shutil.copytree(source_textFolder, dest_textFolder)
	shutil.copytree(source_hotkeysFolder, dest_hotkeysFolder)
	shutil.copytree(source_ssimdataFolder, dest_ssimdataFolder)
	os.mkdir(os.path.join(dest_textFolder,language))#Makes a folder with nothing just with the name of the real current language since it wont be possible knowing





def main():#All the steps the program will perform while running and its functions
	Welcome()
	check_if_inside_main_game_folder()
	menu()
	print("Language Patch Complete")

# Initializer
main()
print("Language updated sucessfully! ")
print("In order to change the language again just run this python script again")
input("Press enter to exit this program")
