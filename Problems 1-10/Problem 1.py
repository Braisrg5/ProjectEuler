def sum35(n):
    return sum([i for i in range(n) if i%3 == 0 or i%5 == 0])


if __name__ == "__main__":
    print(sum35(10)) # 23
    print(sum35(1000)) # 
    