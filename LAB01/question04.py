import re

f=open("LAB01\weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()

pattern=re.compile("\((.+?)\)")
result=pattern.findall(content)

print(result)
print(len(result))