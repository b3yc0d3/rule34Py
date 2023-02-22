import requests # request img from web
import shutil # save img locally
import os # just for the file extension in line 24

from rule34Py import rule34Py
r34Py = rule34Py()
search = r34Py.search(["nekopara"], limit=3)

def download(url, file_name):
    res = requests.get(url, stream = True)
    
    # rule34.xxx apis will always return a status
    # of 200 (which kinda sucks)
    if res.status_code == 200:
        
        # open a file to write to
        with open(file_name,'wb') as f:
            
            # write the raw body data of the requests
            # response to that file
            shutil.copyfileobj(res.raw, f)
            
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')



for result in search:
    filename, file_extension = os.path.splitext(result.image)
    
    # call function to start downloading
    download(result.image, str(result.id) + file_extension)