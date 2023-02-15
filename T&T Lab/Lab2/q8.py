# Rename key of a dictionary

import q6

q6.dictionary["E1"] = q6.dictionary["e1"]
del q6.dictionary['e1']

print(q6.dictionary.items())