# File-Encryptor
This python project is a tool designed to take a file's contents and encrypt the data stored to a corresponding JSON file. The JSON file will be named under the
following convention: "<original_filename>_encrypted.json" with three key / value pairs. These keys are processed_file, data and timestamp. The processed_file details the file that was passed into the tool and the value for the data key is the base64 encoded encrypted text that the program produced. The timestamp is the current unix epoch time to detail when the file was successfully produced. 

The encryption itself is based on Fernet, which is available from the cryptography module. I built a wrapper class around the Fernet class (named Encryptor) along with a logging class and a file utility module so that basic file I/O functions are facilitated. Tests detail the common unittests for the main files in the lib folder.

For future commits and developments, my current objectives are to create a CLI version of this tool so that it can be invoked from the terminal for any files I want to encrypt and store. The main CLI version of this project will also be used in my internal home API (which will be based on my other template repository for express and mongoDB) so that any user files are encrypted and stored securely. 


