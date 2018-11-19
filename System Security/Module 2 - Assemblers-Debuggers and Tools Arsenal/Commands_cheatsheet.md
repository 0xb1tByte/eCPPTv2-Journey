
# **1 - Compilers**
- What a Compiler does is convert a **high-level source code** (such as C) into **low-level code** or directly an **object file**

```
	########     1 - GCC   ########
	// to check gcc version
	gcc --version

	// details about gcc 
	gcc -v

	// Help 
	gcc --help

	// compile .C files
	gcc -m32 demo.c -o demo.exe

	// compile .CPP files
	g++ -m32 demo.c -o demo.exe
```	

--------------------------------------------

# **2 - Assemblers**
- What an Assembler does is translate the **Assembly language** to the **Machine code (opcode)**

```
	########     1 - NASM   ########
	// assemble the "demo.asm" , -f for format, in this case it's Microsoft object file format for 32-bit OS
	nasm -f win32 demo.asm -o demo.obj
```

--------------------------------------------

# **3 - Linkers** 
- What a linker does is take one or more **Object files** and combine them to create the **.exe file**

```
	########     1 - GoLink   ########
	// Linking OBJ with libraries to generate .EXE file
	GoLink.exe /entry _main demo.obj kernel32.dll user32.dll
```

--------------------------------------------

# **4 - Disassemblers**
- What a Disassembler does is translate a **Machine language (opcode)** into **Assembly language**

```
	########     1 - objdump   ########
	objdump -d Mintel fileName.exe > disasm.txt
```
