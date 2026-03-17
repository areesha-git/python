# write a program to fill in a letter template given below with name and date 
# Dear <|name|>,
# You are selected!
# <|Date|>

letter = '''Dear <|name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|name|>","Areesha").replace("<|Date|>","24 september"))
