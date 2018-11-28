## 1 - Crypto PART :

### SSH commands
```
	//  with this command: all the traffic sent to localhost's port 3000 will be forwarded to remote host on port 23 through the tunnel , -L used to initiate a tunnel 
	ssh -L  3000:homepc:23 bob@sshserver
	ssh -L localport:remotehost:remoteport username@sshserver.com
```
------------------------------------------------------------

## 2 - Passwords PART (windows 200/XP/2k3/Vista/7/8) :

### Windows password note : 

- SAM file stored at (but it's not accessible while the OS is running)
```
C:\Windows\System32\config
```

- These values are also stored in the registry (but also it's not accessible while the OS is running) at: 
```
HKEY_LOCAL_MACHINE\SAM
```

### Password dump tools : 
- pwdump (need admin prev.)
- fgdump (need admin prev.)
- ophcrack (need admin prev.)
- SAMinside
- L0phtCrack
- oclHashcat
- RainbowCrack
- hashdump (metasploit)
- john 
```
	// the format for LM and NT in john must be 
	user:hashpassword
	
	// running john with bruteforce option
	john --incremental pass.txt
```
