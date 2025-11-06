x=int(input('please enter the seconds:\n'))
hours=x//3600
minuts=(x%3600)//60
seconds=(x%60)%3600
print(f'the hours is {hours} and the minuts {minuts} and the secands is {seconds}')
