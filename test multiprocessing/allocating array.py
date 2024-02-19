# def split_list(input_list, n):
#     k, remainder = divmod(len(input_list), n)
#     sublists = [input_list[i * k + min(i, remainder):(i + 1) * k + min(i + 1, remainder)] for i in range(n)]
#     return sublists

# # Example usage:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = split_list(my_list, 2)
# print(result.pop(0))
# for i in result:
#     print(i)
# print(result)
a="akjff skdjf"
b=a.split()
print(b)