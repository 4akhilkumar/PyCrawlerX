"""
PyCrawlerX - A Python Path Crawling Tool for Windows and Linux.
"""
import os
import sys

class PyCrawlerX:
    """
    PyCrawlerX - A Python Path Crawling Tool for Windows and Linux.
    """
    def __init__(self):
        """
        Initialize the class.
        """
        self.path_ = None
        self.content = {}
        self.clean_content = {}
        self.curr_files_count = 0
        self.curr_dirs_count = 0

    def __pycrawlerx_logo(self) -> None:
        """
        Print the PyCrawlerX Logo.
        """
        print(
            """
░▒█▀▀█░█░░█░▒█▀▀▄░█▀▀▄░█▀▀▄░█░░░█░█░░█▀▀░█▀▀▄░▀▄░▄▀
░▒█▄▄█░█▄▄█░▒█░░░░█▄▄▀░█▄▄█░▀▄█▄▀░█░░█▀▀░█▄▄▀░░▒█░░
░▒█░░░░▄▄▄▀░▒█▄▄▀░▀░▀▀░▀░░▀░░▀░▀░░▀▀░▀▀▀░▀░▀▀░▄▀▒▀▄
                                    - By @activare
            """
        )

    def __is_dir_of_file(self, dir_or_file) -> None:
        """
        Check if the given path is a file.

        Args:
            dir_or_file (str): The path of the file or directory.

        Returns:
            None
        """
        self.curr_files_count += os.path.isfile(dir_or_file)
        self.curr_dirs_count += os.path.isdir(dir_or_file)

    def __clean_name(self, dir_or_file) -> str:
        """
        Clean the name of the file or directory.

        Args:
            dir_or_file (str): The path of the file or directory.

        Returns:
            str: The cleaned name of the file or directory.
        """
        return os.path.basename(dir_or_file)

    def __execute_file(self, file_path) -> None:
        """
        Execute the file.

        Args:
            file_path (str): The path of the file to execute.

        Returns:
            None
        """
        user_input = input("Do you want to execute this file? (y/n): ")
        if user_input == "y":
            os.system(f"python {file_path}")
            print("File executed.")
        self.__crawl(os.path.dirname(file_path))

    def __execute_all_files(self) -> None:
        """
        Execute all the files in the current directory.

        Returns:
            None
        """
        user_input = input("Do you want to execute all the files in this directory? (y/n): ")
        if user_input == "y":
            for file in os.listdir(self.path_):
                file_path = os.path.join(self.path_, file)
                if os.path.isfile(file_path):
                    os.system(f"python {file_path}")
            self.__crawl(self.path_)

    def __crawl(self, path_) -> None:
        """
        Crawl the path and list out the content in that path.
        Content can be files or directories.

        Args:
            path_ (str): The path to crawl.

        Returns:
            None
        """
        self.path_ = path_
        __inc_num = 0
        self.curr_files_count = 0
        self.content = {}
        self.clean_content = {}
        if os.path.isdir(self.path_):
            if len(os.listdir(self.path_)) > 0:
                for dir_or_file in os.listdir(self.path_):
                    __inc_num += 1
                    self.__is_dir_of_file(os.path.join(self.path_, dir_or_file))
                    __clean_name = self.__clean_name(dir_or_file)
                    self.content[__clean_name] = os.path.join(self.path_, dir_or_file)
                    self.clean_content[__inc_num] = __clean_name

                if self.curr_files_count >= 2:
                    self.clean_content[len(self.clean_content) + 1] = "All Files"
                if os.path.dirname(self.path_):
                    self.clean_content[len(self.clean_content) + 1] = "Back"
                self.clean_content[len(self.clean_content) + 1] = "Exit"
            else:
                __message = "\nThis directory is empty.\n"
                self.clean_content[len(self.clean_content) + 1] = "Back"
                self.__cli_menu(__message)
        elif os.path.isfile(self.path_):
            self.__execute_file(self.path_)
        self.__cli_menu()

    def __content_info(self, message: str = None) -> None:
        """
        Print the content information.
        """
        print("=====================================================")
        print(f"Current Directory: {self.path_}")
        print("=====================================================")
        if message:
            print(message)
        for key, value in self.clean_content.items():
            print(f"{key}. {value}")
        print("=====================================================")

    def __cli_menu(self, message: str = None) -> None:
        """
        A CLI Menu for PyCrawlerX.

        Returns:
            None
        """
        self.__content_info(message)
        __user_input = int(input("Enter your choice: "))
        if self.clean_content[__user_input] == "Exit":
            sys.exit()
        elif self.clean_content[__user_input] == "Back":
            self.__crawl(os.path.dirname(self.path_))
        elif self.clean_content[__user_input] == "All Files":
            self.__execute_all_files()
        else:
            self.__crawl(path_ = self.content[self.clean_content[__user_input]])

    def load_environment_variables(self, key_value: dict) -> None:
        """
        Create the environment variables using key_value dictionary

        Args:
            key_value (dict): The dictionary with key and value

        Returns:
            None
        """
        for key, value in key_value.items():
            os.environ[key] = value

    def run_pycrawlerx(self, folder_path) -> None:
        """
        Run the PyCrawlerX.

        Args:
            path_ (str): The path to crawl.

        Returns:
            None
        """
        self.__pycrawlerx_logo()
        self.__crawl(path_ = folder_path)
        self.__cli_menu()
