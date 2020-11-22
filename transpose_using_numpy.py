import numpy


def trans(A):
    return numpy.transpose(A)


def matrix_input():
    m = int(input("Enter the number of rows: "))
    matrix = [list(map(int, input("Enter space separated elements of row "
                                  + str(i + 1) + ": ").split())) for i in range(m)]
    return matrix


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print("A = " + str(A))
ans = input("If you want transpose of matrix A press Y or else press any other key to make a new matrix: ")
if ans.lower() == "y":
    mat = A
else:
    mat = matrix_input()
print("Transpose of " + str(mat) + " is \n" + str(trans(mat)))
