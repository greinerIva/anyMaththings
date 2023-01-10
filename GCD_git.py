
def divisors(num):    
    divisor = []
    for i in range(1, num+1): 
        if num % i == 0:
            divisor.append(i)
    return divisor

def gcd_all_divs(nums):
    '''Находит НОД чисел
    Сравнивая делителями нулегого числа с делителями остальных чисел
    '''
    # сейчас мы будем вычислять делители
    # записывать делители каждого числа в свой список
    # и эти списки записывать в ещё один список
    num_divisors = []
    for i in range(len(nums)):    
        num_divisors.append(divisors(nums[i]))    
    
    # сейчас мы будем перебирать от большего к меньшему делители одного числа
    # и сравнивать с другими делитилями чтобы найти делитель который есть во всех этих числах    
    for i in range (len(num_divisors[0])):
        divisors_0 = num_divisors[0][-1-i]
                
        gcd_found = True
        for y in range(1, len(nums)):
            gcd_check = False
            for j in range(len(num_divisors[y])):
                divisor = num_divisors[y][-1-j]
                if divisor == divisors_0:
                    gcd_check = True
                    gcd = divisors_0
                    break
            if gcd_check != True:
                gcd_found = False
                break
        if gcd_found:
            break
    return gcd


def gcd_all_divs_in(nums):
    '''Находит НОД чисел 
    Ищя делители нулегого числа в делителях остальных чисел
    '''
    # сейчас мы будем вычислять делители
    # записывать делители каждого числа в свой список
    # и эти списки записывать в ещё один список
    num_divisors = []
    for i in range(len(nums)):    
        num_divisors.append(divisors(nums[i]))    
    
    # сейчас мы будем перебирать от большего к меньшему делители одного числа
    # и сравнивать с другими делитилями чтобы найти делитель который есть во всех этих числах    
    for i in range (len(num_divisors[0])):
        divisors_0 = num_divisors[0][-1-i]
                
        gcd_found = True
        for y in range(1, len(nums)):
            gcd_check = divisors_0 in num_divisors[y]
            if gcd_check != True:
                gcd_found = False
                break
        if gcd_found:
            result = divisors_0
            break
    return result    
    

if __name__ == "__main__":    
    print("введите натуральные числа. Когда вы ведёте ноль, ввод будет недоступен")
    do = True
    n_num = 0
    nums = []
    
    # сейчас мы будем генерить числа 
    while do:
        num = int(input())
        if num == 0:
            do = False 
        else:
            nums.append(num)
    
    print(f"НОД{nums} = {gcd_all_divs_in(nums)}")
    print(gcd_all_divs(nums))

#10.01.2023 created by Ivan L. Github - greinerIva
