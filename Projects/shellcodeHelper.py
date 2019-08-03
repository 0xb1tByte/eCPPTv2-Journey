"""
shellcodeHelper : simple script to help you during shellcode development
Version : 1.0
Pyhton Version : 2.7
Platform : Windows
License : GNU LESSER GENERAL PUBLIC LICENSE Version 3
"""
import binascii
#from capstone import *
from ctypes import *
# loading a sample DLL file for testing purposes
kernel32 = windll.kernel32

# TODO :
#        1 - Convert ASM to Byte Code ===========================================> UNDER DEV.
#        2 - Convert Byte Code to ASM ===========================================> UNDER DEV.
#        3 - Convert ASCII to hex with \x prefix ================================> DONE
#        4 - Convert Spaces in HEX with \x prefix ===============================> DONE
#        5 - Resolve function address in .dll file ==============================> DONE
#        6 - Split a string to 4 byte string ====================================> UNDER DEV.
#        7 - Add "push" bytecode at the beginning of string Byte Code ===========> UNDER DEV.
#        8 - Add a terminator (Byte Code) which is "\x68\x20\x20\x20\x20\00" ====> UNDER DEV.
#        9 - Search for a null bytes in a given shellcode =======================> UNDER DEV.
#        10 - Test the shellcode (I'm not sure if I can do it with python!) =====> UNDER DEV.

def Banner():
    print("""
\033[37m+---------------------------------------------------+   
     _       _ _\033[1;31m _____ _____ __    _____ _____ _____ \033[0m
 ___| |_ ___| | \033[1;31m|  |  |   __|  |  |  _  |   __| __  |\033[0m
|_ -|   | -_| | \033[1;31m|     |   __|  |__|   __|   __|    -|\033[0m
|___|_|_|___|_|_\033[1;31m|__|__|_____|_____|__|  |_____|__|__|\033[0m
                                                     
\033[0mBy: \033[1;31mAlaa , aka: b1tByte\033[0m | github: 0xb1tByte\033[0m
\033[37m+---------------------------------------------------+                                     
""")

class shellHELPER:
    # --------------------- Class Methods --------------------- #

    # [3] - This method converts ASCII to HEX then add "\\x" notation before each byte
    def ASCII_2_HEX(b):
        return ''.join('\\x' + binascii.hexlify(byte) for byte in b)
    # TEST
    ascii2hex = ASCII_2_HEX('cmd')
    #print (ascii2hex)

    #====================================================================#

    # [4] - This method replaces the spaces in HEX with "\\x" prefix
    def replace_Spaces_In_HEX(hexWithSpace):
        return '\\x' +hexWithSpace.replace(" ","\\x")
    # TEST
    hexwithspace = replace_Spaces_In_HEX("2e 65 78 65")
    #print (hexwithspace)

    #====================================================================#

    # [5] - This method resolves function address in .dll file
    def resolve_Function_Address(dll, func):
        handle = kernel32.GetModuleHandleA(dll)
        address = kernel32.GetProcAddress(handle, func)
        kernel32.CloseHandle(handle)
        return address
    # TEST
    address = resolve_Function_Address('kernel32.dll','Sleep')
    #print ("address is :", hex(address) )
    #print(windll.kernel32)
    #print(cdll.msvcrt)

    # --------------------- END --------------------- #
def main():
    Banner()
    sh = shellHELPER()


if __name__ == "__main__":
    main()
