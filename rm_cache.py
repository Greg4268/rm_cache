import os 
import time 
import shutil 

cache_path = "/Users/jmnut/Library/Caches/"
dirs = [d for d in os.listdir(cache_path) if os.path.isdir(os.path.join(cache_path, d))]

def run():

    with open('ascii.txt', 'r') as file:
        content = file.read()  
        print(content) 

    dots = ""
    for i in range(3):
        dots += "."
        print(f"Starting rm_cache auto cache cleaner{dots}", end="\r")
        time.sleep(0.5)
    print()

    for _dir in dirs:
        print(f"[ INFO ] removing directory: {_dir}/")
        remove(_dir)

def remove(_dir):
    full_path = os.path.join(cache_path, _dir)
    if os.path.exists(full_path):
        time.sleep(.1)
        try:
            shutil.rmtree(full_path)
            print(f"[ INFO ] Deleted directory: {full_path}")
        except Exception as e:
            print(f"[ ERROR ] Error deleting {full_path}: {e}")
    else:
        print(f" [ WARNING ] Path does not exist: {full_path}")



