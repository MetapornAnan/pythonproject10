f_iot = open('iot3.txt', 'r', encoding='utf-8')

data = f_iot.read()

f_iot.close()

print(data)