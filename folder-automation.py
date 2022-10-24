#Python automation project that creates folders for my video projects
from ast import main
import os
from tabnanny import process_tokens

# TODO change this to where you want your folder to be located
directory = '/Users/brennanadams/Desktop/'


# TODO add your project folder name here
project_title = 'video test project'

# TODO change sub folder names here or add more sub folders here
project_sub_folders = ['RAW ' + project_title + ' photos', 'project files', 'after effects', 'RAW VIDEO']


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


