import os
import sys
import codecs
from PIL import Image
from resizeimage import resizeimage

root = ''
density = 'hdpi'
isFile = False

densities = {
    'ldpi': 'ldpi',
    'mdpi':'mdpi',
    'hdpi':'hdpi',
    'xhdpi':'xhdpi',
    'xxhdpi':'xxhdpi',
    'xxxhdpi':'xxxhdpi'
}

multipliers = {
    'ldpi': 3,
    'mdpi': 4,
    'hdpi': 6,
    'xhdpi': 8,
    'xxhdpi': 12,
    'xxxhdpi': 16
}

folders = {
    'ldpi': "drawable-ldpi",
    'mdpi': "drawable-mdpi",
    'hdpi': "drawable-hdpi",
    'xhdpi': "drawable-xhdpi",
    'xxhdpi': "drawable-xxhdpi",
    'xxxhdpi': "drawable-xxxhdpi"
}




def isPathArgument(path):
    if path.lower() == "this":
        return True
    elif os.path.exists(path):
        return True
    else:
        relPath = os.getcwd()
        relPath = os.path.join(relPath, path)
        if os.path.exists(relPath):
            return True
    return False




def isDensityArgument(value):
    if value in densities:
        return True
    return False




def getPathString(string):
    if string.lower() == "this":
        return os.getcwd()
    elif os.path.isdir(string) or os.path.isfile(string):
        return string
    elif os.path.isdir(os.path.join(os.getcwd(), string)) or os.path.isfile(os.path.join(os.getcwd(), string)):
        return os.path.join(os.getcwd(), string)





def createDrawableFolders(origin):
    global isFile
    if isFile:
        origin = os.path.dirname(origin)

    for folder in folders:
        try:
            os.mkdir(os.path.join(origin,folders[folder]))
        except OSError as e:
            pass




def createImagesSet(src):
    with open(src, 'r+b') as f:
        with Image.open(f) as image:
            width, height = image.size
            filename = os.path.basename(src)
            rootFolder = os.path.dirname(os.path.dirname(src))
            print(f"[ IMG DETECTED ] {filename} detected")
            for newDensity in densities:
                if not newDensity == density:
                    destination = os.path.join(rootFolder, os.path.join(folders[newDensity], filename))
                    newWidth = width/multipliers[density] * multipliers[newDensity]
                    newHeight = height/multipliers[density] * multipliers[newDensity]
                    print(f"\tconverting to: {newDensity}")
                    cover = resizeimage.resize_cover(image, [newWidth, newHeight], validate=False)
                    cover.save(destination, image.format)




#WHEN PATH IS A FOLDER
def folder():
    global root, density, isFile
    #checking if exist elements
    if len(os.listdir(root)) <=0:
        print("[ ERROR ] Folder empty")
        sys.exit()

    #checking if folder contains images
    imageDetected = False
    for file in os.listdir(root):
        if file.endswith(".jpg") or file.endswith(".png"):
            imageDetected = True
            break
    if not imageDetected:
        print("[ ERROR ] Folder does not contain image files.")
        sys.exit()

    #creating directories
    createDrawableFolders(root)

    #moving images to his directory
    for file in os.listdir(root):
        if os.path.isfile(os.path.join(root, file)) and (file.endswith(".jpg") or file.endswith(".png")):
            destination = os.path.join(root, folders[density])
            os.replace(os.path.join(root, file), os.path.join(destination, file))

    #resizing images and setting on his directories
    srcFolder = os.path.join(root,folders[density])
    for file in os.listdir(srcFolder):
        createImagesSet(os.path.join(srcFolder, file))
        print(f"[ DONE ] {file} converted successfully\n")

    print(f"\n\n[ FINISHED ] Image Assets created successfully")





#WHEN PATH IS A SINGLE FILE
def single():
    global density, root, isFile
    #Creating folders
    createDrawableFolders(root)
    src = ''
    #Moving image to his folder
    if root.endswith(".jpg") or root.endswith(".png"):
        destination = os.path.join(os.path.dirname(root), os.path.join(folders[density], os.path.basename(root)))
        src = destination
        os.replace(root, destination)

    #Resizing images
    createImagesSet(src)
    print(f"\n\n[ FINISHED ] Image Assets created successfully")





def main():
    global density, root, isFile
    if len(sys.argv) >= 4:
        print("[ ERROR ] More than 2 arguments have been detected")
        sys.exit()
    elif len(sys.argv) == 1:
        root = os.getcwd()
        density = "hdpi"
    else:
        #Evaluating arg1
        if isPathArgument(sys.argv[1]):
            root = getPathString(sys.argv[1])
            try:
                sys.argv[2]
                if isDensityArgument(sys.argv[2]):
                    density = sys.argv[2]
                else:
                    print("[ WARNING ] density argument not detected. Set hdpi as default? (Y/N): ")
                    opc = input()
                    if opc.lower() == "y":
                        density = "hdpi"
                    else:
                        while True:
                            tempDensity = input("Enter a density (ldpi, mdpi, hdpi, xhdpi, xxhdpi or xxxhdpi): ")
                            if tempDensity in densities:
                                density = densities[tempDensity]
                                break
                            else:
                                print("No valid density")
            except IndexError as e:
                density = "hdpi"


        elif isDensityArgument(sys.argv[1]):
            density = sys.argv[1]

            try:
                sys.argv[2]
                if isPathArgument(sys.argv[2]):
                    root = getPathString(sys.argv[2])
                else:
                    opc = input("[ WARNING ] path argument not detected. Set current directory as default? (Y/N): ")
                    if opc.lower() == "y":
                        root = getPathString("this")
                    else:
                        while True:
                            temp = input("Enter a full directory path or 'this': ")
                            if isPathArgument(temp):
                                root = getPathString(temp)
                                break
                            else:
                                print("No valid density")
            except IndexError as e:
                root = getPathString("this")
        else:
            print("[ ERROR ] First argument given error.\n\t-The folder is empty\n\t-The image file doesn't exist.\n\t-Path doesn't exist.\n\t-It is not a valid path argument.\n\t-It is not a valid density.")
            sys.exit()

    isFile = os.path.isfile(root)
    if isFile:
        single()
    else:
        folder()





if __name__ == "__main__":
    main()
