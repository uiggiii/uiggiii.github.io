def two_of_three(i,j,k):
    return i ** 2 +j ** 2 +k ** 2 - max(i,j,k) ** 2
print(two_of_three(5,9,3))
