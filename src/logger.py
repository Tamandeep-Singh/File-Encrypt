class Logger:
    def __init__(self, tag):
        self.LOG_TAG = tag

    def log(self, message):
        print(f"{self.LOG_TAG}: {message}\n")