class FileManipulator:
    def __init__(self, fileName):
        self.fileName = fileName
        self.content = None
    
    def read(self):
        try:
            myfile = open(fileName, 'r')
            self.content = myfile.readlines()
        #accept the name 
        except (FileNotFoundError, TypeError, OSError) as error:
            print(type(error), error)
            fileName = input('Enter a valid file name')
        else:
            myfile.close()
        # promp the error

    def reverse(self, fileName):
        while True:
            try:
                myfile = open(fileName, 'w')
                revContent = [x.strip()[::-1] for x in self.content]
                for i in range(len(revContent)):
                    if i == len(revContent -1):
                        myfile.write(revContent[i])
                    else:
                        myfile.write(revContent[i] + '\n')
            except (FileNotFoundError, TypeError, OSError) as error:
                print(type(error), error)
                fileName = input('Please enter a valid file name')
            else:
                myfile.close()
                break

    def upper(self, filename):
        while True:
            try:
                myfile = open(fileName, 'w')
                upperContent = [x.strip().upper() for x in self.content]
                for i in range(len(upperContent)):
                    if i == (len(upperContent) -1):
                        myfile.write(upperContent[i] + '\m')
            except (FileExistsError, TypeError, OSError) as error:
                print(type(error), error)
                fileName = input('Enter a valid file name')
            else:
                myfile.close()
                break


        #accept the name of the file
        #the order would be the same 
        #each line will be reverse



# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

'''
test code:


f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''