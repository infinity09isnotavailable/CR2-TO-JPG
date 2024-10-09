# Convert-CR2-TO-JPG
Here, you can find the file to convert cr2 to jpg and tutorial on how to do it.

> first step - install python,

> download the Zip file which has python file in it,

> then extract it,

> open the extracted folder and open python file and edit the folder locations with notepad or other editors,

> For Example;

     #change this, C:\Users\user\Pictures\CR2 'with your actual folder path where your .CR2 files are located.'
     ----> source_dir = r'C:\Users\user\Pictures\CR2' 

    #Do the Same thing here but, put the folder path where you want to save the converted files of .CR2.
     ----> dest_dir = r'C:\Users\user\Pictures\CCR2' 
    
> open command promt where python file is located in the folder,
> in command promt,

> install pillow by Using this command:

     pip install -r requirements.txt

> then run:

     python convert.py
