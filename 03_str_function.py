name = "areesha"

print(len(name))

print(name.endswith("sha"))
print(name.endswith("shas"))# it return false because its endswith sha not with shas

print(name.startswith("ar"))#if there is a capital A it give false bcz a and A is different 
print(name.capitalize())# it only workon the first letter

s = "hello world"
index = s.find("world")
print(index)

replaced_string = s.replace("world","Harry")
print(replaced_string)