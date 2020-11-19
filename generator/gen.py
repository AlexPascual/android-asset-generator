from PIL import Image
from resizeimage import resizeimage
import os
import sys
import codecs

root = ''
density = 'hdpi'
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

def main():
    #path argument validation
    try:
        sys.argv[1]
        if sys.argv[1].lower() == "this":
            root = os.getcwd()
        elif not os.path.isdir(sys.argv[1]):
                root = sys.argv[1]
                print("[ ERROR ] This directory doesn't exists")
                sys.exit()
        else:
            print("[ ERROR ] Path not valide")
    except IndexError as e:
        print("[ ERROR ] You must define a directory path as argument")
        sys.exit()

        #source density validation
    try:
        sys.argv[2]
        density = sys.argv[2]
    except IndexError as e:
        print("[ WARNIG ] Density not defined, hpdi selected by default")
        density = "hdpi"
    if not density in densities:
        print("[ ERROR ] Density doesn't exists")
        sys.exit()


    #checking if exist elements
    if len(os.listdir(root)) <=0:
        print("[ ERROR ] Folder empty")
        sys.exit()

    #creating directories
    for densityDirectory in densities:
        try:
            os.mkdir(root+"/drawable-"+densityDirectory)
        except OSError as e:
            pass


    #moving images to his directory
    for file in os.listdir(root):
        if os.path.isfile(os.path.join(root, file)) and (file.endswith(".jpg") or file.endswith(".png")):
            destination = os.path.join(root, folders[density])
            os.replace(os.path.join(root, file), os.path.join(destination, file))

    #resizing images and setting on his directories
    for file in os.listdir(root+"/drawable-"+density):

        with open(root+"/drawable-"+density+"/"+file, 'r+b') as f:
            with Image.open(f) as image:
                width, height = image.size
                print(f"[ IMG DETECTED ] {file} detected")
                for newDensity in densities:
                    if not newDensity == density:
                        destination = destination = os.path.join(root, folders[newDensity])
                        newWidth = width/multipliers[density] * multipliers[newDensity]
                        newHeight = height/multipliers[density] * multipliers[newDensity]
                        print(f"\tconverting to: {newDensity}")
                        cover = resizeimage.resize_cover(image, [newWidth, newHeight], validate=False)
                        cover.save(os.path.join(destination, file), image.format)

        print(f"[ DONE ] {file} converted successfully\n")
    print(f"\n\n[ FINISHED ] Image Assets created successfully")




if __name__ == "__main__":


    main()
