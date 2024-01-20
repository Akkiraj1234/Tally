path_of_dir='C:\\users\\Public'
import os
if os.path.exists(path_of_dir+'\\'+"tally"):
    pass
else:
    os.mkdir(path_of_dir+'\\'+"tally")
