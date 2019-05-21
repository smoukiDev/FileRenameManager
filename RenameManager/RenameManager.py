
import os

def main():
    path = "W:/GCP/RenameManager/RenameManager/TestFiles"
    subString = "sm"
    fileNamePrefix = "file"
    renameFileNames(path, subString, fileNamePrefix)

def renameFileNames(path: str, subString : str, fileNamePrefix: str):
    amount = 0
    fileNameIndex = 1
    fileNamesAffected = []
    for fileName in os.listdir(path):
        if fileName.lower().find(subString.lower()) != -1:
            fileNamesAffected.append(fileName)
            fileExtension = [""]
            if fileName.find(".") != -1:
                fileExtension = fileName.split(".")            
            newFileName = fileNamePrefix + str(fileNameIndex) + "." + fileExtension[len(fileExtension)-1]
            os.rename(path + "/" + fileName, path + "/" + newFileName)
            amount += 1
            fileNameIndex += 1
       
    print("Total files affected: %d" % (amount))
    print("List of Affected files:")
    for filename in fileNamesAffected:
        print(filename)
    

def listFileNames(path: str):
    amount = 0
    fileNames = []
    for filename in os.listdir(path):
        amount += 1
        fileNames.append(filename)

    print("Total amount of files in dirrectory: %d" % (amount))
    print("Files available in dirrectory:")
    for filename in fileNames:
        print(filename)

if __name__ == '__main__':
    main()