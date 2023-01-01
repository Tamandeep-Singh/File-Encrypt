# File-Encrypt

Project Status: In Development
Main Use: Internal Home API (for uploading and downloading files)
API Template Repo: https://github.com/Tamandeep-Singh/express-mongo-boilerplate 


This python project is a tool designed to take a file's contents and encrypt the data stored to a corresponding JSON file. The JSON file will be named under the
following convention: "<original_filename>_encrypted.json" with three key / value pairs. These keys are processed_file, data and timestamp. The processed_file details the file that was passed into the tool and the value for the data key is the base64 encoded encrypted text that the program produced. The timestamp is the current unix epoch time to detail when the file was successfully produced. 

The encryption itself is based on Fernet, which is available from the cryptography module. I built a wrapper class around the Fernet class (named FernetEncrypt) along with a logging class and a file utility module so that basic file I/O functions are facilitated.  The tests folder details the common unit tests for the main files in the lib folder.

For future commits and developments, my current objectives are to create a CLI version of this tool so that it can be invoked from the terminal for any files I want to encrypt and store. The main CLI version of this project will also be used in my internal home API (which will be based on my other template repository for express and mongoDB) so that any user files are encrypted and stored securely. 

# Todo:

1) Decrypted file output should be stored in a separate JSON file (status: done)
2) Adding additional unit tests in /tests (status: done)
3) Testing CLI script via a NodeJS file so that any files that the user uploads can be encrypted (status: not yet completed) -> pending consideration
4) Creating a docker image and adding a dockerfile (status: in progress)






