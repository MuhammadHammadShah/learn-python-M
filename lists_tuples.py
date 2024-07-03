frnd = ["apple", "orange"]
frnd[1] = "banana"
print(frnd)
frnd.append("mango")
print(frnd)
frnd.remove("apple")
print(frnd)
frnd.insert(1, "peach")
print(frnd)


a = (9, 8, 7, 8)
print(type(a))
b = a.index(8)
print(b)
c = a.count(8)
print(c)
d = a.count(9)
print(d)

s = set()
print(s)
print(type(s))
s.add(1)
print(s)
print(type(s))

# words = {
#     "kursi": "chair",
#     "makan": "butter",
#     "billi": "cat",
#     "mez": "table",

# }

# word = input("name the word you want the meaning of : ")

# print(words[word])

# print(20 == 20.0)  # true
# print(20 == "20.0")  # false


# post = input("Enter the post : ")

# if ("Hammad".lower() in post.lower()):
#     print("The post is about Hammad")
# else:
#     print("The post is not about Hammad")


# l = [1, 3, 4, 5, 7, 9]
# for i in l:
#     print(i)
# else:
#     print("done")

# for i in range(100):
#     if (i == 15):
#         break
#     print(i)
# else:           # it will not print done because it break on 14.
#     print("done")

# for i in range(20):
#     if (i == 15):
#         continue  # it will eat 15 and upon 19 loop ends so printed done
#     print(i)
# else:
#     print("done")

# n = int(input("enter the number: "))
# i = 0
# while i < 11:
#     print(f"{n} X {i} = {i*n}")
#     i += 1
#     break  # it will break after first iteration


# n = int(input("enter the number: "))
# i = 0
# while i < 11:
#     # it will complete the table of the number your desired
#     print(f"{n} X {i} = {i*n}")
#     i += 1


# n = int(input("Enter the number:"))
# i = 1
# sum = 0
# while (i <= n):
#     sum += i
#     i += 1
#     # print(sum)
# print(sum)


# factorial

# n = int(input("Enter the Number: "))
# product = 1
# for i in range(1, n+1):
#     product *= i
#     # print(product)
# print(f"the factorial of number {n} is {product}")
