#How to print right triangle pattern in one line

print(*('*'*i for i in range(1, int(input('Enter size: '))+1)), sep='\n')