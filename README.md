This little Python program compresses all modified files into a backup folder.

This program runs in the backgroud, for this the following is necessary:

1.- Place the program and the backup folder in the path of the directory where the files will be.

2.- Run the program as follows:
  $ chmod +x programa.py
  $ nohup python programa.py & 

3.- To find the process and kill it:
ps ax | grep programa.py 
kill PID
