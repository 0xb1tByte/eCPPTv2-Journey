# Stack Notes : 
- Stack is **LIFO** (Last in , First out )
- Stack grows **downward**, towards **lower memory addresses**
- Stack has 2 Functions : 
  - **1 - PUSH :** add element to the TOP of the Stack, in other words: **PUSH** stores data in the TOP of the Stack 
  - **2 - POP :** delete element from the TOP of the Stack, in other words: **POP** retrives the data from the TOP of the Stack
- **PUSH** & **POP** affect the **TOP of the Stack** only, (because Stack is LIFO)
- **EBP :** this register points (contains the address value) to the **Stack Base** (first element entered the Stack)
- **ESP :** this register points to the **TOP of Stack** (last element entered the Stack)
- The Stack consists of logical **Stack Frames** (portions/areas of the Stack)

# How Function Works (a deep look inside the Stack) :
- Every Function has its own **Stack Frame**
- When the Function is called, the Stack Frame for that Function is **PUSH**ed (created) to the Stack
- When the Function finishied its work, the Stack Frame is **POP**ed (deleted) from the Stack
- Function contains two important components: 
    - **1 - Prologue:** prepares the Stack to be used
    - **2 - Epilogue:** resets the Stack
- When a Function terminates, it returns control to that statement or instruction that called this Function 



# ASM Notes : 
