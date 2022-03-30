n,div=map(int,input().split())
sm=0
# for i in range(n):
#     rem= i % div
#     sm+=rem 
sm=(div*(div-1))//2
sm*= (n//div)
print(sm)