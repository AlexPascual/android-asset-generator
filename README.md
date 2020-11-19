# android-asset-generator
___
## Description
android-assset-generator is a command line program for generate ldpi, mdpi, hdpi, xhdpi, xxhdpi and xxxhdpi density images for your Android Studio Project.
___
## Requeriments
* python-resize-image [View package](https://pypi.org/project/python-resize-image/)
___

## Installing
       pip install android-asset-generator
___

## Usage
* Prepare a folder that contains only the images you want to convert to the different densities.
* Run the following command.

       android-asset-generator  path   density

Argument | Description | Example
---------|------------ | -----------
path     | Full path string of your asset folder. It can be a path or "this" if your console workspace is the asset folder | C:\Users\MyUser\Desktop\img xhdpi or this
density  | The source density. If your images are mdpi, put mdpi as argument | ldpi, mdpi, hdpi, xhdpi, xxhdpi or xxxhdpi

> **Note:** You must not switch order of the arguments

* The generated images will be saved in different folders within the specified path following the Android Studio standard:
 - drawable-ldpi
 - drawable-mdpi
 - drawable-hdpi
 - drawable-xhdpi
 - drawable-xxhdpi
 - drawable-xxxhdpi

* The source images will be moved to the corresponding folder without having suffered alterations.
* The last step is to import the generated folders to your Android Studio. project
___

## Examples
        android-asset-generator C:\Users\MyUser\Desktop\img xhdpi
> The asset folder path is C:\Users\MyUser\Desktop\img and asset density is xhdpi

        android-asset-generator this
> The asset folder path is the console current directory and asset density is hdpi by default
___

## Compatibility
Operating System | Test Results
-|-
Windows 10 | passed
MacOS | No tested
Linux | No tested
___
## GitHub Repository
To be uploaded
___
## Licence
The project is licensed under the MIT License
