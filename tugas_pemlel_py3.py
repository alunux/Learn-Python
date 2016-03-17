#!/bin/env python3
from sys import argv

def sort_min_to_max(nim):
    '''
    This function using Merge Sort algorithm and sort nim from min to max number
    parameter: nim = a list of integer
    return   : nim = a list of integer
    Note     : nim is a list data type
    '''
    if len(nim) > 1:
        mid = len(nim) // 2
        left_side = nim[:mid]
        right_side = nim[mid:]

        sort_min_to_max(left_side)
        sort_min_to_max(right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                nim[k] = left_side[i]
                i += 1
            else:
                nim[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            nim[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            nim[k] = right_side[j]
            j += 1
            k += 1

    return nim

def sort_max_to_min(nim):
    '''
    This function using Merge Sort algorithm and sort nim from max to min number
    parameter: nim = a list of integer
    return   : nim = a list of integer
    Note     : nim is a list data type
    '''
    if len(nim) > 1:
        mid = len(nim) // 2
        left_side = nim[:mid]
        right_side = nim[mid:]

        sort_max_to_min(left_side)
        sort_max_to_min(right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] > right_side[j]:
                nim[k] = left_side[i]
                i += 1
            else:
                nim[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            nim[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            nim[k] = right_side[j]
            j += 1
            k += 1
    return nim

def fill_matrix(nim):
    '''
    Generate value for Matrix X and Matrix Y from nim.
    parameter: nim = a list of integer
    return   : x = a 2x3 matrix, y = a 3x3 matrix
    Note     : x, y, and nim are list data type
    '''
    x = [
            [0, 0, 0],
            [0, 0, 0]
        ]
    y = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    count_nim = 0

    for row_x in range(len(x)):
        for col_x in range(len(x[row_x])):
            x[row_x][col_x] = int(nim[count_nim])
            count_nim += 1

    for row_y in range(len(y)):
        for col_y in range(len(y[row_y])):
            y[row_y][col_y] = int(nim[count_nim])
            count_nim += 1

    return x, y

def multiply_matrix(x, y):
    '''
    Multiply Matrix X and Matrix Y
    parameter: x = a 2x3 matrix, y = a 3x3 matrix
    return   : z = a 2x3 matrix
    Note     : x, y, and z are list data type
    '''
    z = [
            [0, 0, 0],
            [0, 0, 0]
        ]

    for r_x in range(len(x)):
        for c_y in range(len(y[0])):
            for r_y in range(len(y)):
                z[r_x][c_y] += x[r_x][r_y] * y[r_y][c_y]

    return z

def print_matrix(matrix):
    '''
    Print all element in a matrix
    parameter: matrix = a matrix
    return   : nothing
    Note     : matrix is a list data type
    '''
    for element in matrix:
        print (element)

def print_help():
    '''
    Print information about the program
    '''
    print ("Usage: python3 tugas_pemlel.py your_NIM" \
          "\n- if your_NIM is even, then tugas_pemlel.py will execute sorting "\
          "program \n- if your_NIM is odd, then tugas_pemlel.py will execute " \
          "matrix multiplication program")

def main(argument):
    '''
    This is the main function
    '''
    nim = str(argument[1])
    if len(nim) == 15:
        if int(nim) % 2 == 0:
            print ("NIM Anda Genap: %s" % nim)
            print ("Sorted NIM (MIN->MAX): %s" \
                  % "".join(map(str, sort_min_to_max(list(map(int, nim))))))
            print ("Sorted NIM (MAX->MIN): %s" \
                  % "".join(map(str, sort_max_to_min(list(map(int, nim))))))
        else:
            print ("NIM Anda Ganjil: %s" % nim)

            x, y = fill_matrix(nim)
            z = multiply_matrix(x, y)

            print ("\nMatrix X dengan ukuran %s x %s" % (len(x), len(x[0])))
            print_matrix(x)
            print ("\nMatrix Y dengan ukuran %s x %s" % (len(y), len(y[0])))
            print_matrix(y)
            print ("\nHasil perkalian Matrix X dan Matrix Y adalah Matrix Z " \
                  "dengan ukuran %s x %s" % (len(z), len(z[0])))
            print_matrix(z)
    else:
        print ("NIM harus 15-digit")

if __name__ == '__main__':
    if len(argv) == 2:
        main(argv)
    else:
        print_help()
