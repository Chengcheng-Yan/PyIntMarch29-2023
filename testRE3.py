import re

text="filename=data.content.txt"

"""
\d     a digit
+         1 or more occurrence
{min,max} between [min,max] occurrences
{2,}    2 or more occurrences
{3}     3 occurrences
{1,} <=> +
{0,} <=> *
{0,1} <=> ?
.    any character except a new line
\.   the character .
[123]
\d <=> [0123456789]
\d <=> [0-9]
[^0-9] any character except a digit
\D <=> [^0-9]
[^a-z]
[^xyzXYZ]
\s <=> "white space"
\S <=> a character which is not a white Space
[aft5] => a or f or t or 5
[^aft5] => any character except a f t or 5

\d <=> [0-9]
\D <=> [^0-9]
$ : means the end of the string
^ : means the beginning of the string
"""

#regexp=re.compile(r"\.[^0-9]{3}$")
regexp=re.compile(r"^filename$")
matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
    print(matchobj.group(0))

else:
    print("The string text does not 'match'")