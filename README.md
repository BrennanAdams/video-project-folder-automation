# Video Project Folder Automation

This Python script automates the creation of folder structures for video projects, designed specifically for photographers and videographers. It streamlines the organization of assets, editing files, and raw footage from shoots, facilitating efficient video editing workflows.

## Installation

1. Clone this repository to your local machine using:
    ```bash
    git clone https://github.com/your-username/video-project-folder-automation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd video-project-folder-automation
    ```

## Usage

### Command Line Interface

Navigate to the directory where the script is located in your terminal and run the script using Python. You must provide the name of your project as an argument when running the script.

```bash
python video-project-folder-automation.py "Project Name"
```

Replace `"Project Name"` with the desired title for your project folder.

### Customization

Before running the script, you may need to customize the folder structure and location according to your preferences. Follow these steps to customize the script:

1. **Change Folder Location**: Open the script (`video-project-folder-automation.py`) in a text editor and modify the `directory` variable to specify the desired location for the project folders. By default, the script creates folders on the desktop (`/Users/brennanadams/Desktop/`).

    ```python
    # TODO: Change this to where you want your folder to be located
    directory = '/Users/brennanadams/Desktop/'
    ```

2. **Edit Folder Structure**: Adjust the `project_sub_folders` list to customize the folder structure. You can add, remove, or rename subfolders to suit your workflow.

    ```python
    # TODO: Change subfolder names here or add more subfolders here
    project_sub_folders = [
        '01_Assets',
        '02_Editing_Files',
        '02_Editing_Files/02_After_Effects',
        '02_Editing_Files/01_Premiere_Pro',
        '03_Raw_Footage',
        '03_Raw_Footage/01_RAW_Video',
        '03_Raw_Footage/02_RAW_Photos' + project_title,
        '04_Draft_Renders',
        '05_Deliverables',
        '01_Assets/01_Footage',
        '01_Assets/02_Audio',
    ]
    ```

After customizing the script, proceed with the command line usage as described above.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
