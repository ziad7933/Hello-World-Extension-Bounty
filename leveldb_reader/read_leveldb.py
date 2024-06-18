import os
import plyvel

EXTENSION_ID = 'Put the extension ID here'
LEVELDB_PATH = os.path.expanduser(
    '/Users/ziadhossain/Library/Application Support/Google/Chrome/Default/Local Extension Settings/' + EXTENSION_ID)

def fetch_from_leveldb(db_path):
    try:
        db = plyvel.DB(db_path, create_if_missing=False)
        try:
            for key, value in db:
                print(f'Key: {key.decode("utf-8")}, Value: {value.decode("utf-8")}')
        finally:
            db.close()
    except Exception as e:
        print(f'Error accessing LevelDB: {e}')

if __name__ == '__main__':
    fetch_from_leveldb(LEVELDB_PATH)
