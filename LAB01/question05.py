import re

f=open("weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()

pattern=re.compile("\d+/\d+/\d+")
result=pattern.findall(content)

print(result)
print(len(result))