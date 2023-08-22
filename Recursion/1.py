# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# ให้เขียน Recursive หาค่า Max ของ Input

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

# Example usage
number_list = list(map(int,input("Enter Input : ").split(" ")))
max_number = find_max(number_list)
print("Max :", max_number)