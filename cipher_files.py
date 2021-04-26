from cryptography.fernet import Fernet
import tkinter
from  tkinter import filedialog

class cipher_files():

    def encrypt(filename, key):
        f=Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt(filename, key):
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open(filename, "wb") as file:
            file.write(decrypted_data)

    def write_key():
        w_key=filedialog.asksaveasfilename(title="Save Key", filetypes=[("Key files", "*.key")])
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open(w_key, "wb") as key_file:
            key_file.write(key)

    def load_key():
        key_f=filedialog.askopenfilename(title="Load Key", filetypes=[("Key files", "*.key")])
        """
        Loads the key from the current directory named `key.key`
        """
        print(open(key_f, "rb").read())

    
    def main():
        window=tkinter.Tk()
        window.withdraw()
        print("1)Encrypt\n2)Decrypt\n3)Write key\n4)Load Key\nq)Exit\n")
        while True:
            fun=input(":")
            if fun=='1':
                try:
                    o_file=filedialog.askopenfilename(title="Load File to Encrypt", filetypes=[("All files", "*")])
                    k_file=filedialog.askopenfilename(title="Load Key", filetypes=[("Key files", "*.key")])
                    k_file_2=open(k_file, "rb").read()
                    encrypt(o_file, k_file_2)
                except:
                    print('Error!\n')

            elif fun=='2':
                try:
                    o_file_d=filedialog.askopenfilename(title="Load File to Decrypt", filetypes=[("All files", "*")])
                    key_file_3=filedialog.askopenfilename(title="Load Key", filetypes=[("Key files", "*.key")])
                    key_file_4=open(key_file_3, "rb").read()
                    decrypt(o_file_d, key_file_4)
                except:
                    print('Error!\n')

            elif fun=='3':
                try:
                    cipher_files.write_key()
                except:
                    print('Error!\n')

            elif fun=='4':
                try:
                    cipher_files.load_key()
                except:
                    print('Error!\n')

            elif fun=='q':
                break

        else:
            print("Invalid command\n")
