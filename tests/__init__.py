import sys
import os.path

root_dir = os.path.dirname(os.path.dirname(__file__))
jsondb_dir = os.path.join(root_dir, 'jsondb')
sys.path.append(jsondb_dir)
