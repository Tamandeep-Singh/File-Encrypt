import sys
import argparse
sys.path.insert(0, '/home/tam/Projects/File-Encryptor/lib')
import file_encryptor as FileEncryptor

parser = argparse.ArgumentParser(
    prog="File Encryptor CLI",
    description="This CLI tool uses Fernet Encryption to encrypt a file's contents and store them in a corresponding JSON file. This JSON file can then also be decrypted with the decrypted contents being outputted to the console."
)

parser.add_argument("-f", "--filename", help="the file that you would like to encrypt.", metavar="file")
parser.add_argument("-e", "--encrypt", help="encrypts a files contents to a corresponding JSON file.", action="store_true")
parser.add_argument("-d", "--decrypt", help="decrypts an encrypted JSON file and outputs the decrypted data.", action="store_true")

args = parser.parse_args()

if args.filename and args.encrypt:
    FileEncryptor.process_file_data(args.filename)

if args.filename and args.decrypt:
    FileEncryptor.decrypt_json_file(args.filename)