# get integer from user
user_num = int(input('hello there, enter a postive integer:'))
# print user_num for debugging
print(user_num)

#iteration
for i in range(1, user_num):
    if i%3 == 0:
        print('fizz')
    if i%5 == 0:
        print('buzz')
    else: 
        print(f'{i}')

