f1 = open('tanu_whatsapp.txt', 'r+', encoding='UTF-8')

full_text = f1.readlines()

new_conv = []
for i in full_text:
    if '-' in i:
        new_conv.append(i.split('-')[1].strip())

new_file = ". ".join(new_conv)
new_file = new_file.replace('\"', '\'')
new_file = new_file.replace('Tanushree:', 'fanbot:')
new_file = new_file.replace('Ashwin:', 'You:')

# limit on new file
new_file = new_file[:2049]

print(len(new_file))
f2 = open('extracted_tanu_whatsapp.txt', 'w+', encoding='UTF-8')

f2.write(new_file)

f1.close()
f2.close()