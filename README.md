# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Wastebasket.png" alt="Wastebasket" width="30" height="30" /> Automate File Deletion

With the use of cron jobs this simple Python script will allow you to automatically delete files in your downloads folder. This can be useful when running out of space on your primary drive. 

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> Setup 

1. Clone the repo or download the file with the following command: `wget https://raw.githubusercontent.com/hakrishi/auto-file-deletion/main.py`
2. Make the file executable: `chmod +x main.py`
3. Ensure Python3 is installed, downloads can be found [here](https://www.python.org/downloads/)
4. Edit the `downloads_folder` VAR with your own downloads folder path
5. Run the script: `python3 main.py`

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" alt="Gear" width="25" height="25" /> Cron Job Setup

1. Run `crontab -e` 
2. On the very last line add the following: `0 14 * * 0 /path/to/main.py` 
3. Save the file then exit 

This will run the script every Sunday at 2PM. Note that you will need to edit the file path for the script. 

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" alt="Handshake" width="25" height="25" /> Contributions

As always if you find any bugs or issues with the code feel free to open a pull request! 😃