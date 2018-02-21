#import First
#import imp
import math
import random
import re



print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1, 2, 3, 4]))

s = 'spam'
print(len(s))
print(s[0])
print(s[1])


line = 'aaa,bbb,cccc,ddd'
print(line.split(','))

#print(dir(s))
help(s.replace)  # Получение справки


match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())

#imp.reload(First)
