# นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
# สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน
# ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

# 1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด
# 2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด
# 3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

# ****ห้ามใช้คำสั่ง for, while, do while*****
# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว


def asteroid_collision(asts, index=0):
    if index >= len(asts) - 1:
        return asts

    if asts[index] > 0 and asts[index + 1] < 0:
        if abs(asts[index]) == abs(asts[index + 1]):
            return asteroid_collision(asts[:index] + asts[index + 2:], max(index - 1, 0))
        elif abs(asts[index]) > abs(asts[index + 1]):
            return asteroid_collision(asts[:index + 1] + asts[index + 2:], max(index - 1, 0))
        else:
            return asteroid_collision(asts[:index] + asts[index + 1:], max(index - 1, 0))
    else:
        return asteroid_collision(asts, index + 1)

x = input("Enter Input : ").split(",")
x = list(map(int, x))
result = asteroid_collision(x)
print(result)
