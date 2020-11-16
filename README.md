# ExtractSlateSubmissions
Python3 script to extract assignment files from submission folder and structure them to be used for Plagiarism checking using JPLAG


1. Place the script in the directory containing students submission directory (most probably it will be the downloads directory)
2. To run use the following commands in the terminal (assuming submission directory is in downloads)
    #cd Downloads
    #python3 ExtractSubmissions.py "Directory_Name"
3. The script will make another directory using the folder name and suffix "Scrapped" in the current directory
    containing directory for each students and their submissions
4. The script take cares for submissions made using .zip files and .txt files
5. The script is written on the basis of personal requirements so you may need some little tweaks to get on the road
6. For now it works well for python programming assignments
7. The code is not documented (sorry for that) due to lack of time.
8. Exceptions may occur, you are requested to report  them on my email :)
