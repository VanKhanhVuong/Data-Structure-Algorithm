import random

''' Sắp xếp nổi bọt

    Input : Ta có 1 mảng số nguyên ngẫu nhiên chưa sắp xếp arr = [62, 60, 76, 45]
    Output: Sắp xếp lại theo thứ tự arr = [45, 60, 62, 76]

    Step 1.1:
        arr = [62, 60, 76, 45]
        length = 4
        i = 0
        j = 2

        [62, 60, 76, 45] ta xét arr[ j ] và arr[ j + 1 ] thì arr[2] = 76 > arr[3] = 45
                => Hoán đổi vị trí giữa arr[2] & arr[3] cho nhau
                => [62, 60, 45, 76]

    Step 1.2:
        arr = [62, 60, 45, 76]
        length = 4
        i = 0
        j = 1 

        [62, 60, 45, 76] ta xét arr[ j ] và arr[ j + 1 ] thì arr[1] = 60 > arr[2] = 45
                => Hoán đổi vị trí giữa arr[1] & arr[2] cho nhau
                => [62, 45, 60, 76]

    Step 1.3:
        arr = [62, 45, 60, 76]
        length = 4
        i = 0
        j = 0 

        [62, 45, 60, 76] ta xét arr[ j ] và arr[ j + 1 ] thì arr[0] = 62 > arr[1] = 45
                => Hoán đổi vị trí giữa arr[0] & arr[1] cho nhau
                => [45, 62, 60, 76]

    Step 2.1:
        arr = [45, 62, 60, 76]
        length = 4
        i = 1
        j = 2 

        [45, 62, 60, 76] ta xét arr[ j ] và arr[ j + 1 ] thì arr[2] = 60 < arr[3] = 76
                => Giữ nguyên vị trí không cần hoán đổi
                => [45, 62, 60, 76]

    Step 2.2:
        arr = [45, 62, 60, 76]
        length = 4
        i = 1
        j = 1 

        [45, 62, 60, 76] ta xét arr[ j ] và arr[ j + 1 ] thì arr[1] = 62 > arr[2] = 60
                => Hoán đổi vị trí giữa arr[1] & arr[2] cho nhau
                => [45, 60, 62, 76]

    Step 3.1:
        arr = [45, 60, 62, 76]
        length = 4
        i = 2
        j = 2 

        [45, 60, 62, 76] ta xét arr[ j ] và arr[ j + 1 ] thì arr[2] = 62 < arr[3] = 76
                => Giữ nguyên vị trí không cần hoán đổi
                => [45, 60, 62, 76]
        => Ở vòng lặp cuối cùng mà không hoán đổi gì nữa thì thoát khỏi vòng lặp rồi print ra mảng cuối cùng
        
'''


def array_generation(n):
    arr = []                                            # Tạo 1 một mảng rỗng
    firstNumber = random.randint(-100, 100)             # Tạo 1 số nguyên đầu tiên ngẫu nhiên từ (-100 -> 100)
    arr.append(firstNumber)                             # Thêm số đầu tiên trên vào mảng

    for index in range(1, n):                           # Loop từ (1 -> n - 1) chạy từ 1 nguyên do trong mảng arr[0ơ là số đầu tiên rồi
        plusNumber = random.randint(1, 100)              # Tạo ngẫu nhiên 1 số nguyên ngẫu nhiên có giá trị từ (1 -> 10)
        arr.append(plusNumber)                          # Thêm vào mảng số nguyên bằng giá trị tổng vừa tạo
    return arr                                          # Loop rồi thì return ra mảng

def bubble_sort_with(array):
    lenght = len(array)

    for i in range(lenght):                             # i = [0, lenght - 1]                i chạy từ 0                        -> lenght(tổng mảng) - 1
        are_swapping = False                            # Tạo 1 biến flag thể hiển đã hoán đổi xong chưa ? Ban đầu đặt là False
        for j in range(lenght - 2, i - 1, -1):          # j = [lenght - 2, i]                j chạy từ lenght (tổng mảng) - 2   -> i
            print(f"So sánh: array[{j}] = {array[j]} và array[{j + 1}] = {array[j + 1]} i = {i} & {j}")
            if array[j] > array[j + 1]:                 # Trường hợp nếu 2 phần tử array[j] & array[j + 1] sai vị trí thì hóa đổi vị trí lại cho nhau

                array[j], array[j + 1] = array[j + 1], array[j]     # Có thể hiểu là array[j] = array[j + 1]
                                                                    #                array[j + 1] = array[j] mà không cần tạo biến tạm như vài ngôn ngữ khác
                are_swapping = True                                 # Đặt lại are_swapping thành TRUE vì đang hoán đổi vị trí lại !
                print(f"Hoán đổi: {array}")


        if are_swapping == False:                       # Kiểm tra xem biến are_swapping còn TRUE nữa không nếu còn thì lặp vòng lặp tiếp
            break                                       #                                còn nếu là FALSE thì tất cả các phần tử hoán đổi vị trí xong rồi
                                                        #   ==> NÊN BREAK vòng lặp này

## Hàm chính (main) để thực thi tìm kiếm x trên mảng random
def main():
    randomArray = array_generation(4)                  # Tạo ra 1 mảng có 20 phần tử số ngẫu nhiên
    print("Mảng ban đầu")
    print(randomArray)                       # In mảng cho dễ Debug
    print("\nBắt đầu sắp xếp nổi bọt:\n")
    bubble_sort_with(randomArray)


## Chỉ định hàm MAIN:
if __name__ == "__main__":
    main()