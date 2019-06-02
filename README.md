# Toolhouse: a database exploration


### Technologies Used:
- [Python v3.x](https://docs.python.org/3/)
- [QtFramework v5](https://doc.qt.io/)
- [SQLite v3](https://www.sqlite.org/index.html)

### Python Dependencies:
- [sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pyinstaller](https://www.pyinstaller.org/documentation.html)

## Installation:
1. Click "Clone or Download"
2. Download the .ZIP folder
3. Place .ZIP folder in appropriate location
4. Unzip .ZIP folder
5. Navigate to folder: dist
6. Navigate to folder: toolhouse
7. Scroll down to: toolhouse.exe (windows type 'Application')
8. Execute this file

## Notes:
- The .exe file may take a long time to open; this is normal
- Be sure when downloading the master branch that your aspect ratio is 16:9 or something similar
- This was developed using a Microsoft Surface Product. There is a seperate branch for the 3:2 aspect ratio that these devices use
- In the case where a table's composite PK is also a FK

        ON DELETE and ON UPDATE are set to CASCASE


- In the case where a table simple has a FK

        ON DELETE is changed to SET NULL

###  In the case where the toolhouse.db is irreparable:
0. Close the program

1. Naviage to folder: introtoDatabase

2. Copy file: toolhouse.db

3. Navigate to folder: dist

4. Naviage to folder: toolhouse

5. Paste toolhouse.db into dist

6. Run toolhouse.exe again
> Written with [StackEdit](https://stackedit.io/).
