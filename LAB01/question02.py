import re

f=open("LAB01\weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()

pattern = re.compile(r'\b(?:0*(\d+)|([1-9]\d*))(\.\d+)?\b')
result = [match.group(1) or match.group(2) for match in pattern.finditer(content)]

print(result)
print(len(result))