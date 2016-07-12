# File-Encryption-IBM-Bluemix
-------------------------
Prerequisites:
Create the IBM bluemix app and give the proper credentials in main.py file
Install softclient using pip command.
By default it will upload the file with file name example1.txt, you can change the file name to different one by giving the name in main.py file.
It will look for the file only in the current directory of the script.
-------------------------
This is a simple command line app developed using python.
The script will store a file into IBM Bluemix container after encoding using encode functionality.
Once you select the download option it will download the file to the current directory after decoding it.
I have included the check functionality which is not used, if you want you can use, it will check the file size and restrict the files upload into the container once it reaches 10 MB.
You can also upload any files(like image file) by giving the proper name in the file name variable.
