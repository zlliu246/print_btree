import os
import re

with open('pyproject.toml') as f:
    text = f.read()

old_version = re.findall('version = "(.*?)"', text)[0]
a, b, c = old_version.split('.')
x = int(c) + 1
new_version = f'{a}.{b}.{x}'
text = re.sub(old_version, new_version, text)

with open('pyproject.toml', 'w') as f:
    f.write(text)    

commands = [
    'rm -rf ./dist',
    'python3 -m build',
    'python3 -m twine upload dist/*'
]

for command in commands:
    print(command)
    os.system(command)