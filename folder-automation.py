#Python automation project that creates folders for my video projects
from ast import main
import os
from tabnanny import process_tokens
import sys



# total words in title
num_words = len(sys.argv) #skip 1 because the first argument is file name
folder_name = ''

#print("Total arguments passed:", num_words)
 
#print("\nArguments passed:", end = " ")
for i in range(1, num_words):
    #print(sys.argv[i], end = " ")
    folder_name += str(sys.argv[i]) + " "
    








# TODO change this to where you want your folder to be located
directory = '/Users/brennanadams/Desktop/'


# TODO add your project folder name here
project_title = str(folder_name)

# TODO change sub folder names here or add more sub folders here
project_sub_folders = ['RAW ' + project_title + ' photos', 'project files', 'after effects', 'RAW Video']


#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_________________________________________________________________________________________________________#


#creating our project path
main_project_path = directory + project_title

#creating folder
os.mkdir(main_project_path)

#creating sub folders

sub_folders_path = main_project_path + '/'

for item in project_sub_folders:
    os.mkdir(sub_folders_path + item)


