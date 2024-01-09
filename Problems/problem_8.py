'''The four adjacent digits in the 1000-digit number in the file that have the
greatest product are 9 x 9 x 8 x 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
'''


from functools import reduce

def loadNumber():
    '''Loads the 1000-digit number from the file and returns it as a string.
    '''
    file = open("resources/big_number.txt", "r")
    num = "".join([i.replace("\n","") for i in file.readlines()])
    file.close()
    return num


def prodAdjDig(n):
    '''Finds the nth adjacent digits in the 1000-digit number with the 
    greatest product.
    '''
    num = loadNumber()
    digits = len(num) 
    totalProds = digits - n + 1
    biggest = 1
    for i in range(totalProds):
        # We select, convert to int and multiply the apropiate adjacent digits
        adj = [int(dig) for dig in num[i:n+i]]
        product = reduce(lambda x, y: x*y, adj)
        if product > biggest: biggest = product
    return biggest


if __name__ == "__main__":
    print(prodAdjDig(4)) # 5832
    print(prodAdjDig(13)) # 23514624000
    
    
