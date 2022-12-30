import sys
import argparse
sys.path.insert(0, '/home/tam/Projects/File-Encrypt/lib')
import file_encrypt as FileEncrypt

def get_parser() -> argparse.ArgumentParser:
    """Creates and returns the argument parser."""
    parser = argparse.ArgumentParser(
        prog = "File Encrypt CLI",
        description = "This CLI tool uses Fernet Encryption to encrypt a file's contents and store them in a corresponding JSON file. This JSON file can then also be decrypted with the decrypted contents being outputted to the console."
    )
    return parser

def setup_parser_args(parser: argparse.ArgumentParser) -> None:
    """Sets all arguments for the parser."""
    parser.add_argument("-f", "--filename", help="file to encrypt or decrypt", metavar="file")
    parser.add_argument("-e", "--encrypt", help="encrypts the file to an encrypted JSON file", action="store_true")
    parser.add_argument("-d", "--decrypt", help="decrypts a file and displays its contents", action="store_true")


def process_args(parser: argparse.ArgumentParser) -> None:
    """Process all arguments and performs encryption or decryption of files accordingly."""
    args = parser.parse_args()
    #check if no args passed
    if not len(sys.argv) > 1:
        print("No arguments passed, please refer to the help guide below: \n")
        parser.print_help()
        
    if args.filename and args.encrypt:
        FileEncrypt.process_file_data(args.filename)
    
    if args.filename and args.decrypt:
        FileEncrypt.decrypt_json_file(args.filename)



def setup_parser():
    """Creates the parser and executes its operations."""
    parser = get_parser()
    setup_parser_args(parser)
    process_args(parser)
   

if __name__ == "__main__":
    setup_parser()