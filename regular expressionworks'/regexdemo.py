

from re import finditer

text="fatcatrunsveryfasttocaththerat"
mather=finditer("at",text)

for obj in mather:


    print(obj.groups())

    print(obj.start(),obj.group())



