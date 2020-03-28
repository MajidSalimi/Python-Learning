#Opens a read-only File
f=open('MyFile.txt','r')
#Reads file's content
file_content=f.read();
#closes the file
f.close()
#opens or creates a writable files
f2=open('a_file.txt','w')
#writes in the file
f2.write("This is my first program with files")
f2.close()