# Lists
from typing import List

colleges= ['Buet', 'Du', 'ju']
print(colleges[0])
print(colleges[2])

colleges[2] ="World University of Bangladesh"
print(colleges[2])
print(colleges)
print(colleges[1:3])

list2 = ['table','chair','fan','clothes','bottle']

# list2.append('microphone')
list2.insert(3,'microphone')
print(list2)
list2.remove('microphone')
print(list2 + ['pillow','tubelight','bed'])
print(list2)
print(len(list2))
print(max(list2))
print(min(list2))
