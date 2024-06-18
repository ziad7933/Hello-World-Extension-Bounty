# Hello-World-Extension-Bounty
This is for a bounty testing Google's LevelDB

## Initialization
1. Open the extensions page in Chrome by typing "chrome://extensions/" in the address bar.
2. Enable Developer Mode on the top right corner of the screen.
3. Click "Load Unpacked"
4. Navigate and select the "hello_world_extension" folder and it should appear as an extension.
5. Take note of the ID as you will need that to run the "read_leveldb.py" file.

## Run
To run the file, simply open a terminal in the "leveldb_reader" file and type "python3 read_leveldb.py" or "python read_leveldb.py", whichever works for you.

## Dependencies
You might need to download plyvel if you haven't already in your system. Make sure you have the correct python and pip version installed. From my experimentations, plyvel works best with python version 3.7-3.10 but has some issues with 3.12. Best create a virtual environment and setup python 3.10 or lower and the appropriate pip and then install plyvel.
