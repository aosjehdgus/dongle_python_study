# 1087 : [기초-종합] 여기까지! 이제 그만~

# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.


# 입력
# 언제까지 합을 계산할 지, 정수 1개를 입력받는다.
# 단, 입력되는 자연수는 100,000,000이하이다.


# 출력
# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.


# 입력 예시   
# 57

# 출력 예시
# 66

# while 무한루프 이용 (메모리 33764 시간 24 코드 길이 140B  )

# n = input()
# i = 1
# data = 0

# while True:
    
#     data += i
#     i += 1

#     if data >= int(n):
#         print(data)
#         break

# for 문 이용 (메모리 33752 시간 25 코드 길이 142B)

# n = input()
# data = 0

# for i in range (1, int(n)+1):
    
#     data += i

#     if data >= int(n):

#         break
        
# print(data)       

# 1088 : [기초-종합] 3의 배수는 통과?

# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

# 입력
# 정수 1개를 입력받는다.
# (1 ~ 100)


# 출력
# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.


# 입력 예시   
# 10

# 출력 예시
# 1 2 4 5 7 8 10

# i = 1


# n = input()

# for i in range (int(n) + 1):

#     if i % 3 != 0 :

#         print(i)
    
#     else : 

#         continue

# 1089 : [기초-종합] 수 나열하기1

# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.

# a, d, n = map(int, input().split())

# data = a + (n-1) * d

# print(data)

