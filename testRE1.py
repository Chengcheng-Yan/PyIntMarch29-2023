import re

text="value -67466 THIs end"

"""
\d     a digit <=> [0123456789] <=> [0-9]
+      1 or more occurrences
{min,max} between [min,max] occurrences
{2,}    2 or more occurences
{3}     3 occurrences
{1,} <=> +
{0,} <=> *
{0,1} <=> ?
[abcAR65]
"""

#regexp=re.compile(r"\d{4}") # \w \D \s \S ...
#regexp=re.compile(r"th[eai]", re.I) 
#regexp=re.compile(r"\d{4}", re.I) 
#regexp=re.compile(r"\d{4,6}", re.I) 
#regexp=re.compile(r"[+-]{0,1}\d{4}", re.I) 
regexp=re.compile(r"[+-]?\d{4}", re.I) 

if regexp.search(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")
