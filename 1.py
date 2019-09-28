import random
secret=random.randint(1,10)
print('------------9703-------------')
count1=0
guess=0
print("猜数字：",end=" ")
#temp=input("猜数字")
#guess=int(temp)
while guess != secret and count1<=10 :
	temp=input()
	while not temp.isdigit():
		temp=input("请输入一个整数：")
	guess=int(temp)
	count1=count1+1
	if guess== secret:
		print("恭喜")
	else:
		if guess >secret:
			print("大了")
		else:
			print("小了")
print("结束")
num = int(input("请输入一个整数："))
while num:
    print(' '*(num-1)+'*'*num)
    num -= 1