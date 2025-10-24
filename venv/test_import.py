# # test_import.py
# import sys
# import os

# sys.path.insert(0, '/path/to/your/project')

# try:
#     from pipelines.reddit_pipeline import connect_reddit_pipeline
#     print("✅ Import successful")
    
#     # Test function call với dummy data
#     # connect_reddit_pipeline('test', 'test', 'day', 1)
    
# except ImportError as e:
#     print(f"❌ Import failed: {e}")
# except Exception as e:
#     print(f"❌ Function call failed: {e}")
# successful
# test_constants.py
import sys
import os

# Thêm path
sys.path.insert(0, '/your/project/path')

try:
    from utils.constants import CLIENT_ID, SECRET
    print(f"✅ CLIENT_ID: {CLIENT_ID} (type: {type(CLIENT_ID)})")
    print(f"✅ SECRET: {SECRET} (type: {type(SECRET)})")
except Exception as e:
    print(f"❌ Error importing constants: {e}")
    import traceback
    traceback.print_exc()