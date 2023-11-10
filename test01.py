# Exception Handing
# ข้อผิดพลาด การจัดการ
# Exception ข้อผิดพลาดที่เกิดขึ้นตอนโปรแกรมทำงาน
# try-except-finally

try :
    num1 = int( input('ป้อนตัวเลขตัวที่ 1 :'))
    num2 = int( input('ป้อนตัวเลขตัวที่ 2 :'))

    sum = num1 + num2
    result = num1 / num2

    print(f'ผลรวมของ {num1} + {num2} คือ {sum}')
    print(f'ผลรวมของ {num1} / {num2} คือ {sum}')
except ValueError :
    print('ป้อนตัวเลขเท่านั้นห้ามใส่ตัวอักษร....สงสัยติดต่อ IT')
except ZeroDivisionError :
    print('ป้อนตัวเลขตัวที่ 2 ห้ามเป็น 0....สงสัยติดต่อ IT')
except Exception :
    print('มีข้อผิดพลาดเกิดขึ้น ต้องขอประทานอภัยอย่างสูง ช่วยติดต่อ IT ด้วย จะแก้ไขให้')
finally :
    print('Wow...')
    print('Hello...')