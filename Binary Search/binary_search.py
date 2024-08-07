import random

## Tìm kiếm nhị phân:
    ## Mảng truyền vào để tìm kiếm nhị phần phải được sắp xếp giá trị tăng dần
    ## [02], [14], [22], [28], [36], [48], [62], [75], [88], [94]

    ## Chia mảng ra làm đôi mảng thành (mảng trái, mảng phải) để tìm kiếm
    ## Bằng cách lấy tổng số phần tử trong mảng chia cho 2 => ở đây 10/2 = 5
    ## left_array  = [ [02], [14], [22], [28], [36] ]
    ## right_array = [ [48], [62], [75], [88], [94] ]

    ## Lấy giá trị của phần tử thứ (5 - 1) [INDEX GIỮA] của mảng TRÁI để so sánh với số x
    ## x = 48 > left_array[4] = 36 => Ta sẽ lấy nửa mảng PHẢI để tìm kiếm nhị phân tiếp

    ## Dọn dẹp bộ nhớ chứa mảng TRÁI vì không có giá trị x cần tìm
    ## [48], [62], [75], [88], [94]

    ## Chia tiếp ra làm đôi mảng bên PHẢI(mảng trái, mảng phải) để tìm kiếm
    ## Bằng cách lấy tổng số phần tử trong mảng chia cho 2 => ở đây 5/2 = 2.5 => 3 & 2
    ## left_array  = [ [48], [62], [75] ]
    ## right_array = [ [88], [94] ]

    ## Lấy giá trị của phần tử thứ (3 - 1) của mảng TRÁI để so sánh với số x
    ## x = 48 < left_array[2] = 75 => Ta sẽ lấy nửa mảng TRÁI để tìm kiếm nhị phân tiếp.

    ## Dọn dẹp bộ nhớ chứa mảng PHẢI vì không có giá trị x cần tìm
    ## [48], [62], [75]

    ## Chia tiếp ra làm đôi mảng bên TRÁI(mảng trái, mảng phải) để tìm kiếm
    ## Bằng cách lấy tổng số phần tử trong mảng chia cho 2 => ở đây 3/2 = 1.5 => 2 & 1
    ## left_array  = [ [48], [62] ]
    ## right_array = [ [75] ]

    ## Lấy giá trị của phần tử thứ (2 - 1) của mảng TRÁI để so sánh với số x
    ## x = 48 < left_array[1] = 62 => Ta sẽ lấy nửa mảng TRÁI để tìm kiếm nhị phân tiếp.

    ## Dọn dẹp bộ nhớ chứa mảng PHẢI vì không có giá trị x cần tìm
    ## [48], [62]

    ## Chia tiếp ra làm đôi mảng bên TRÁI(mảng trái, mảng phải) để tìm kiếm
    ## Bằng cách lấy tổng số phần tử trong mảng chia cho 2 => ở đây 2/2 = 1
    ## left_array  = [ [48] ]
    ## right_array = [ [62] ]

    ## Lấy giá trị của phần tử thứ (1 - 1) của mảng TRÁI để so sánh với số x
    ## x = 48 = left_array[0] = 48 đã tìm ra phần tử bằng với x

    ## KẾT THÚC BÀI TOÁN

## Hàm tạo mảng random
## Input:
## Với 1 param là n là số phần tử mong muốn trong mảng

## Output:
## Trả ra 1 mảng số ngẫu nhiên 

def array_generation(n):
    arr = []                                            # Tạo 1 một mảng rỗng
    firstNumber = random.randint(-100, 100)             # Tạo 1 số nguyên đầu tiên ngẫu nhiên từ (-100 -> 100)
    arr.append(firstNumber)                             # Thêm số đầu tiên trên vào mảng

    for index in range(1, n):                           # Loop từ (1 -> n - 1) chạy từ 1 nguyên do trong mảng arr[0ơ là số đầu tiên rồi
        plusNumber = random.randint(1, 10)              # Tạo ngẫu nhiên 1 số nguyên ngẫu nhiên có giá trị từ (1 -> 10)
        plusNumber += arr[index - 1]                    # Lấy giá trị TỔNG của số nguyên trước đó + số nguyên vừa tạo
        arr.append(plusNumber)                          # Thêm vào mảng số nguyên bằng giá trị tổng vừa tạo
    return arr                                          # Loop rồi thì return ra mảng

## Tạo hàm in mảng cho dễ debug
## Input:
## Với param là mảng cần in

## Output:
## In ra vị trí cùng với giá trị từng phần tử trong mảng

def print_array_with(array):                         
    n = len(array)                                      # Lấy n là số phần tử có trong mảng
    for index in range(n):                              # Loop để lấy index của từng phần tử trong mảng (0 -> n-1)
        print(f"arr[{index}] = {array[index]}")         # In ra vị trí cùng giá trị mỗi 1 phần tử

## Hàm tìm kiếm nhị phân
## Input:
## Với 2 param truyền vào là x giá trị cần tìm trong mảng và mảng số nguyên ngẫu nhiên

## Output:
## Trả ra vị trí(index) của x hoặc -1 (nếu không tìm thấy vị trí của x)

def binary_search_with(array, x):
    lenght = len(array)                             # Lấy lenght là số phần tử có trong mảng
    left = 0                                        # Tạo 1 biến LEFT để nắm giá trị BIÊN TRÁI
    right = lenght - 1                              # Tạo 1 biến RIGHT để nắm giá trị BIÊN PHẢI và phải -1 đi vì có biến LEFT rồi 

    for _ in range(lenght):                         # Sử dụng Loop for với số lần lặp bằng độ dài của mảng
        if left > right:                            # Nếu biên trái lớn hơn biên phải, kết thúc vòng lặp
            break
        
        mid = (left + right) // 2                   # Lấy INDEX GIỮA bằng cách lấy trung bình cộng lấy phần nguyên của biên TRÁI và PHẢI 
        mid_value = array[mid]                      # Lấy giá trị tại INDEX GIỮA ĐÓ

        # print(f"left = {left} , right = {right} => mid {mid} _value = {mid_value}")
        
        if mid_value == x:                          # Nếu giá trị tại INDEX GIỮA bằng giá trị cần tìm, trả về INDEX GIỮA
            # print(f"mid = {mid}")
            return mid  
        elif mid_value < x:                         # Nếu giá trị tại INDEX GIỮA nhỏ hơn giá trị cần tìm, tìm kiếm ở nửa phải
            left = mid + 1
            # print(f"left = {left}")
        else:                                       # Nếu giá trị tại INDEX GIỮA lớn hơn giá trị cần tìm, tìm kiếm ở nửa trái
            right = mid - 1
            # print(f"right = {right}")
    
    return -1                                       # Trả về -1 nếu không tìm thấy giá trị cần tìm

## Hàm chính (main) để thực thi tìm kiếm x trên mảng random
def main():
    randomArray = array_generation(20)                  # Tạo ra 1 mảng có 20 phần tử số ngẫu nhiên
    print_array_with(randomArray)                       # In mảng cho dễ Debug

    print('-------------------------------------------')
    x = int(input('Nhập x: '))                          # Lấy x từ giá trị người dùng nhập vào từ bàn phím
    xIndex = binary_search_with(randomArray, x)         # Tìm vị trí của x trong mảng ngẫu nhiên (randomArray)

    if xIndex != -1:                                    ## In ra thông báo có tìm thấy hay không
        print(f"Tìm thấy x = {x} tại vị trí {xIndex}")
    else:
        print(f"KHÔNG tìm thấy x = {x}")

## Chỉ định hàm MAIN:
if __name__ == "__main__":
    main()