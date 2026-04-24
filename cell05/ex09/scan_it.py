import sys
import re

search_word = sys.argv[1] 
target_text = sys.argv[2] 


matches = re.findall(r'\b' + re.escape(search_word) + r'\b', target_text)

print(len(matches))