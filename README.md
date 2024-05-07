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

You can customize the folder structure and location by editing the script:

- **Change Folder Location**: Modify the `directory` variable in the script to specify the desired location for the project folders.
- **Edit Folder Structure**: Adjust the `project_sub_folders` list to customize the folder structure. You can add, remove, or rename subfolders to suit your workflow.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
