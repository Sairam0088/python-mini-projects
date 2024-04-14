#flames game using python
name1 = input('Enter first name: ')
name2 = input('Enter second name: ')
name1 = name1.lower().replace(" ", "")
name2 = name2.lower().replace(" ", "")
for i in name1:
    if i in name2:
        name1 = name1.replace(i, "", 1)
        name2 = name2.replace(i, "", 1)
combined_length = len(name1) + len(name2)
flames = ['Friend', 'Lover', 'Affection', 'Marriage', 'Enemy', 'Sibling']
while len(flames) > 1:
    count = combined_length % len(flames) - 1
    if count>=1:
        flames = flames[count+1:] + flames[:count]
    else:
        flames = flames[:len(flames)-1]
print('Relationship: ',*flames)

