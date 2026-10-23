def collatz(number):
    '''
    Inputs --> Int
    Outputs:
    Even --> number // 2
    Odd --> 3 * number + 1
    '''
    num_process = 0
    if number % 2 == 0:
        num_process = number // 2
    else:
        num_process = 3 * number + 1
        
    print(num_process, end=' ')
    return num_process
    
def main():
    inpt = int(input("Enter your number: "))
    check = True
    new_num = inpt
    
    while new_num != 1:
        new_num = collatz(new_num)

if __name__ == "__main__":
    main()
