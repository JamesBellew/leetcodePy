import random
myTweet = random.randint(1,1500000)
print('the odds of you winning is ' ,1500000/10,'/1')
for i in range(10):
    num = random.randint(1,1500000)
    print(num,' : Mr Beast')
    print(myTweet,' : Me')
    if num == myTweet:
        print('you just won a lot of money')
    else:
        print(":(")


