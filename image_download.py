import requests
import shutil

## Function to download a card at the given "url" and add it to the specified "download_directory"
def download_image(url, download_directory, file_name):

    full_file_name = download_directory +  file_name + ".png"
    
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(full_file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved:', file_name)
