# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/extend (x)/appear (a)/read (r)


f_iot = open('iot4.txt', 'a', encoding='utf-8')

f_iot.write('Wow...')
f_iot.write('Hi...\n')
f_iot.write('สวัสดี...\n')

f_iot.close()