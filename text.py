f = open(r'C:\Users\Sahip\Desktop\Kodland_Python\text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close() 

f = open('metinbelgesi.txt', 'w', encoding='utf-8')
text = 'Yeni Yazı'
f.write(text)
f.close()