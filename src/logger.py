# -----------------------------------------------------------
# filename: logger.py
#
# Description: Basic logger class that can be expanded upon for future projects
# Github Repo: https://github.com/Tamandeep-Singh/File-Encryptor
# Released under MIT License 
# -----------------------------------------------------------

class Logger:
    def __init__(self, tag):
        self.LOG_TAG = tag

    def log(self, message:str) -> None:
        """Logs a message from any file that imports the Logger (designed to be in the format: [LOG_TAG]: <method>"""
        print(f"{self.LOG_TAG}: {message}\n")