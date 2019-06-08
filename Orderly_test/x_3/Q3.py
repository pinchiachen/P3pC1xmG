import os
import xlwings as xw
import random
import string
import numpy as np

s = os.getcwd()
path = f'{s}/ilovecoffee'

class CsvHanlder():
    def __init__(self):
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)

    def create_csv(self):
        wb = xw.Book()
        sheet = wb.sheets['工作表1']
        sheet.cells(1, 1).value = "customer_id"
        sheet.cells(1, 2).value = "customer_email"
        sheet.cells(1, 3).value = "customer_mobile"
        sheet.cells(1, 4).value = "frequency"

        # ID產生器(7位英文大小寫 + 數字)
        def id_generator(size = 7, chars = string.ascii_letters + string.digits):
            return (''.join(random.choice(chars) for x in range(size)))

        # 產生ID(1位隨機英文大小寫 + 7位ID產生器)
        for i in range(2, 502):
            sheet.cells(i, 1).value = random.choice(string.ascii_letters) + id_generator()

        # 創建英文名字列表
        name = ["Kobe", "Shaq", "Lebron", "Steven", "Kevin", "Derek", "Allen", "Alex", "Charlie", "Nick" ]

        # 產生email
        for i in range(2, 502):
            sheet.cells(i, 2).value = random.choice(name) + "." + sheet.cells(i, 1).value

        # 電話產生器(隨機9位數字)
        def phone_generator(size = 9, chars = string.digits):
            return (''.join(random.choice(chars) for x in range(size)))

        # 不斷生成電話並且利用set刪除重複的電話，直到電話數量到達500
        numbers = []
        while len(numbers) < 500:
            numbers.append("+886" + " " + phone_generator())
            numbers = list(set(numbers))
        for i in range(2, len(numbers)+2):
            sheet.cells(i, 3).value = numbers[i - 2]

        # 產生frequency
        for i in range(2, 502):
            sheet.cells(i, 4).value = random.randint(0,20)

        # 存檔
        wb.save(f'{path}\customers.csv')

    def calculate_csv(self):
        wb = xw.Book(f'{path}\customers.csv')
        sheet = wb.sheets['工作表1']
        nums = []
        for i in range(2, 502):
            nums.append(sheet.cells(i, 4).value)
        print(f"中位數 = {np.median(nums)}\n眾數 = {np.argmax(np.bincount(nums))}\n平均數 = {np.mean(nums):.5f}")

if __name__ == '__main__':
    CsvHanlder()




