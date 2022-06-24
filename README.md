# ye_sorter
A simple script that sorts files into alphabetical folders

To use: put it in a directory and run it.  It'll go through every file in its current directory and sort them.  It WON'T go through sub-directories.  This is by design.

Can create folders for files or create every folder in the alphabet, choose between generic and per-number folders, create folders in upper or lower case, and that's about it.  

If a file name begins with one or more non-alphanumeric characters, they will be ignored.  If a file name consists entirely of non-alphanumeric characters, the file itself will be ignored.

I made this one evening because it was faster than manually sorting a bunch of files.  Enjoy it if you feel like it might help.  I tested it pretty thoroughly, but I can make no guarantees that it won't behave unexpectedly outside of a Windows 11 setting.

Note: This won't work on external devices that you can't mount as drives.  Namely, Android devices, at least without some major finagling.  This is a quirk of the Android OS and can't be fixed, at least not in the scope of this project.
