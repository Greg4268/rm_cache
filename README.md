```
                                                             /$$                
                                                            | $$                
  /$$$$$$  /$$$$$$/$$$$         /$$$$$$$  /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$ 
 /$$__  $$| $$_  $$_  $$       /$$_____/ |____  $$ /$$_____/| $$__  $$ /$$__  $$
| $$  \__/| $$ \ $$ \ $$      | $$        /$$$$$$$| $$      | $$  \ $$| $$$$$$$$
| $$      | $$ | $$ | $$      | $$       /$$__  $$| $$      | $$  | $$| $$_____/
| $$      | $$ | $$ | $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$
|__/      |__/ |__/ |__//$$$$$$\_______/ \_______/ \_______/|__/  |__/ \_______/
                       |______/                                                 
                                                                                
```

# MacOS Cache Cleaner 
Simple python script to remove cache files on MacOS to free up space

# Run as a cronjob 
1. in terminal type `crontab -e` 
2. insert `0 7 * * * /path/to/python3 ~/path/to/rm_cache/__init__.py >> ~/path/to/rm_cache/logfile.log 2>&1`
3. save and exit 

### This script is now scheduled to run everyday at 7 AM and remove all files from cache that are not currently in use or require elevated permissions to remove
