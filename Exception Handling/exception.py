try:
   fh = open("testfile", "w")
   try:
      print("File is opened for Writing.")
      str1 = raw_input("Input a text to write in file: ")
      fh.write(str1)
      print("Text is written in file.")
   finally:
      print("Going to close the file")
      fh.close()
except IOError:
   print("Error: can't find file or write data")

print("==============================================================")

try:
   fh = open("testfile", "r")
   try:
      print("File is opened for Reading.")
      str = fh.read()
   finally:
      print("Text in file is:")
      print(str)
      print("Going to close the file")
      fh.close()
except IOError:
   print("Error: can't find file or read data")
