import random

## Hàm tạo mảng random
## Input:
## Với 1 param là n là số phần tử mong muốn trong mảng

## Output:
## Trả ra 1 mảng số ngẫu nhiên 

def array_generation(n):
    arr = []                                            # Tạo 1 một mảng rỗng
    for index in range(n):                              # Loop từ (0 -> n - 1)
        randomNumber = random.randint(-100, 100)        # Tạo 1 số nguyên ngẫu nhiên từ (-100 -> 100)
        arr.append(randomNumber)                        # Cho số ngẫu nhiên này vào mảng
    return arr                                          # Loop rồi thì return ra mảng

## Hàm tìm kiếm tuyến tính
## Input:
## Với 2 param là mảng chứa x (arr) và x cần tìm

## Output:
## Trả ra vị trí(index) của x hoặc -1 (nếu không tìm thấy vị trí của x)

def linear_search_with(array, x):
    n = len(array)                                      # Lấy n là số phần tử có trong mảng
    for index in range(n):                              # Loop để lấy index của từng phần tử trong mảng (0 -> n-1)
        if array[index] == x:                           # So sánh từng phần tử trong mảng                                 
            return index                                # Nếu phần tử nào có giá trị bằng x thì TRẢ RA vị trí (index) của phần tử đó.
    return - 1                                          # Nếu Loop hết mảng vẫn chưa tìm ra phần tử nào bằng x thì TRẢ RA là -1

## Tạo hàm in mảng cho dễ debug
## Input:
## Với param là mảng cần in

## Output:
## In ra vị trí cùng với giá trị từng phần tử trong mảng

def print_array_with(array):                         
    n = len(array)                                      # Lấy n là số phần tử có trong mảng
    for index in range(n):                              # Loop để lấy index của từng phần tử trong mảng (0 -> n-1)
        print(f"arr[{index}] = {array[index]}")         # In ra vị trí cùng giá trị mỗi 1 phần tử

## Hàm chính (main) để thực thi tìm kiếm x trên mảng random
def main():
    randomArray = array_generation(20)                  # Tạo ra 1 mảng có 20 phần tử số ngẫu nhiên
    print_array_with(randomArray)                       # In mảng cho dễ Debug

    print('-------------------------------------------')
    x = int(input('Nhập x: '))                          # Lấy x từ giá trị người dùng nhập vào từ bàn phím
    xIndex = linear_search_with(randomArray, x)         # Tìm vị trí của x trong mảng ngẫu nhiên (randomArray)

    if xIndex != -1:                                    ## In ra thông báo có tìm thấy hay không
        print(f"Tìm thấy x = {x} tại vị trí {xIndex}")
    else:
        print(f"KHÔNG tìm thấy x = {x}")

## Chỉ định hàm MAIN:
if __name__ == "__main__":
    main()