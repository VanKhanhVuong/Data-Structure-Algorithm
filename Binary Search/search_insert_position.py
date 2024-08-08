
'''
https://leetcode.com/problems/search-insert-position/description/

Đề bài:
Input:  Cho một mảng số nguyên (nums) đã được sắp xếp tăng dần và một số nguyên (target) 
Output: Hãy trả về 
    + Vị trí (index) của phần tử trong mảng (nums) nếu nó bằng số nguyên (target)
    + Và nếu số nguyên (target)
        + Lớn hơn phần tử trong mảng (nums) thì thêm phía bên phải phần tử lớn thua số nguyên (target) trong mảng (nums)
        + Nhỏ hơn phần tử trong mảng (nums) thì thêm phía bên trái phần tử nhỏ thua số nguyên (target) trong mảng (nums)
        
Ý tưởng:
    Ta có nums = [1,3,5,6] và target là x

    ---------------
    Nếu target = 3
        left = 0
        right = len(nums) - 1 = 3
        

        -------------[1] Vòng lặp 1-------------------------------------------------
        left = 0
        right = 3
        mid = (0 + 3) // 2 = 1
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[1] = 3 == target = 3
            => Trả về vị trí mid = 1 như thuật toán tìm kiếm nhị phân bình thường

    ---------------
    Nếu target = 2
        left = 0
        right = len(nums) - 1 = 3
    
        -------------[1] Vòng lặp 1-------------------------------------------------
        left = 0
        right = 3
        mid = (0 + 3) // 2 = 1
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[1] = 3 > target = 2
            => right = mid - 1 = 1 - 1 = 0

        -------------[2] Vòng lặp 2-------------------------------------------------
        left = 0
        right = 0
        mid = (0 + 0) // 2 = 0
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[0] = 1 < target = 2
            => left = mid + 1 = 1

        -------------[3] Vòng lặp 3-------------------------------------------------
        left = 1
        right = 0
        mid = (1 + 0) // 2 = 1
            => DỪNG VÒNG LẶP NGUYÊN DO LÀ LEFT ĐÃ LỚN HƠN RIGHT VÀ TRẢ RA LEFT = 1
            => Ta (insert) thêm target = 2 vào nums[2] = 2 =>  nums = [1,2,3,5,6] (Thỏa mãn bài toán)
        
    ---------------
    Nếu target = 7
        left = 0
        right = len(nums) - 1 = 3
    
        -------------[1] Vòng lặp 1-------------------------------------------------
        left = 0
        right = 3
        mid = (0 + 3) // 2 = 1
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[1] = 3 < target = 7
            => left = mid + 1 = 1 + 1 = 2
        
        -------------[2] Vòng lặp 2-------------------------------------------------
        left = 2
        right = 3
        mid = (2 + 3) // 2 = 2
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[2] = 3 < target = 7
            => left = mid + 1 = 2 + 1 = 3

        -------------[3] Vòng lặp 3-------------------------------------------------
        left = 3
        right = 3
        mid = (3 + 3) // 2 = 3
        Ta sẽ lấy target so sánh với nums[mid] 
        nums = [1,3,5,6]
            => nums[3] = 5 < target = 7
            => left = mid + 1 = 3 + 1 = 4

        -------------[4] Vòng lặp 4-------------------------------------------------
        left = 4
        right = 3
        mid = (3 + 3) // 2 = 3
            => DỪNG VÒNG LẶP NGUYÊN DO LÀ LEFT ĐÃ LỚN HƠN RIGHT VÀ TRẢ RA LEFT = 4
            => Những phần tử trong mảng vẫn nhỏ hơn target = 7
            => Ta (insert) thêm target = 7 vào nums[4] = 7 =>  nums = [1,3,5,6,7] (Thỏa mãn bài toán)

        -----------------------------------------------------------------------------
        *** LƯU Ý TRONG PYTHON 5 // 2 = 2 NGUYÊN DO LÀ // LÀ CHIA LẤY PHẦN NGUYÊN ***
        -----------------------------------------------------------------------------
'''

def search_insert_position(array, x):
    lenght = len(array)                             
    left = 0                                        
    right = lenght - 1                          

    for _ in range(lenght):                         
        if left > right:                           
            break
        
        mid = (left + right) // 2                   
        mid_value = array[mid]
        if mid_value == x:                          
            return mid
        elif mid_value < x:                         
            left = mid + 1
        else:                                       
            right = mid - 1
        # print(f"mid[{mid}] : {mid_value}, left: {left}")     

    array.insert(left, x)
    print(array)                              
    return left
    
## Hàm chính (main) để thực thi tìm kiếm x trên mảng random
def main():
    array = [1,3,5,6]
    x = 7                        
    print(f"Đã thêm x = {x} vào mảng và vị trí là: {search_insert_position(array, x)}")

## Chỉ định hàm MAIN:
if __name__ == "__main__":
    main()