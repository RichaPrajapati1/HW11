# Note: 
#   Please save this as diagnostic_firstname.txt
#       (replace firstname w/ yours)
#   Do not edit lines that say: "# Last line in ____"
###############################################################################
# Imports  # there will only be one import added here.
import os
import this

###############################################################################
# Write f01 that prints "Hello World!" and calls f02. (three lines)
def f01():
    print ("Hello World")
    f02()
###############################################################################
# Write f02 that sets the variables x, y, and z equal to the words 
# necessary to have the f03 print "i love python!" (five lines)
def f02():
    x = 'I'
    y = 'love'
    z = 'python'
    f03(x,y,z)  # Last line in f2()
###############################################################################
# Finish f03 (replace the ????). 
def f03(*words):
    truth = " ".join(words)  # This is broken.
    truth_emphasized = truth + "!"
    print truth_emphasized
    f04(truth)  # Last line in f03()
###############################################################################
# Write f04 that prints truth backwards (edit one line only)
# Ex. f4("Littlest Bear") prints "raeB tselttiL"
def f04(string):
    print string[::-1]
    f05(string)  # Last line in f04()
###############################################################################
# Write f05 that for each char in a word passed as a parameter, prints that 
# word on a new line, and for each consecutive print, prints it indented by one
# more char. (possibly a few lines)
# Ex. f05("Info")
# Info
#  Info
#   Info
#    Info
def f05(word):
    space = 1
    for char in word:
        print (" "*space + word)
        space += 1
    f06("South Hall", "Python Rocks!")  # Last line in f05()
###############################################################################
# Write f06 that takes two strings:
# (1) prints: "'string' is longer than 'string' by x chars"
#   replace string and string w/ the actual strings, replace x w/ proper value
# (2) prints: "'string' has only xx.xx% the number of chars of 'string'"
#   replace string and string w/ the actual strings
#   replace xx.xx w/ proper value
# (several lines)
# Ex. f06("short_string", "longer_string")
# 'longer_string' is longer than 'short_string' by 1 chars
# 'short_string' has only 92.31% the number of chars of longer_string
def f06(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 > len2:
        x = len1 - len2
        percent = (float(len1)/len2)*100
        print ("{0} is longer than {1} by {2} chars" .format(string1,string2,x))
        print ("{0} has only {2}% the number of chars of {1}" .format(string1,string2,percent))
    elif len2 > len1:
        x = len2 - len1
        percent = (float(len2)/len1)*100
        print ("{0} is longer than {1} by {2} chars" .format(string2,string1,x))
        print ("{0} has only {2}% the number of chars of {1}" .format(string2,string1,percent))
    else:
        print ("{0} is same as {1}" .format(string2,string1))
        print ("{0} has 100% the number of chars of {1}" .format(string2,string1))
    various_solutions()  # Last line in f06()
###############################################################################
# Write f07, f08, f09, f10 to find the sum of all the multiples of 3 or 5 
# below 500 (starting at 1)
# f07 should demonstrate a while loop, returning the sum
# f08 should demonstrate a for loop, returning the sum
# f09 should demonstrate list comprehension, returning the sum
# f10 should demonstrate recursion, returning the sum
# check_solution_vals() will call the functions and check solutions.
# only edit the parameters in the function calls (if you want to)
###############################################################################
def various_solutions():
    """ This checks solutions. ONLY EDIT PARAMETERS PASSED TO FUNCTIONS. """
    while_ = f07(500)
    for_ = f08(500)
    list_comprehension = f09(500)
    recursion = f10(500)
    # DO NOT EDIT BELOW THIS LINE
    vals = [while_, for_, list_comprehension, recursion]
    for val in vals:
        print val
    if len(set(vals)) == 1:
        print("Not sure if it's right, but all your solutions agree!")
    else: print ("Oops...")
    f11_args = [1,"2", 3.0, '4', 5.0, 6]  # Last lines in various_solutions()
    for arg in f11_args:
        f11(arg)
    f12()
###############################################################################
def f07(num):
    sum_mul = 0
    while num > 0:
        if (num%3 == 0) or (num%5 == 0):
            sum_mul += num
        num -= 1
    return sum_mul

###############################################################################
def f08(num):
    sum_mul = 0
    for num in range(1,num+1):
        if (num%3 == 0) or (num%5 == 0):
            sum_mul += num
    return sum_mul

###############################################################################
def f09(num):
    list_ = [i for i in range(num+1) if (i%3 == 0) or (i%5 == 0)]
    return sum(list_)
  
###############################################################################
def f10(num):
    if num == 0:
        return 0
    else:
        if (num%3 == 0) or (num%5 == 0):
            sum_mul = num + f10(num-1)
        else:
            return f10(num-1)
    return sum_mul


###############################################################################
# Write f11() to take arguments, printing them as floats if they started as
# strings, integers if they started as floats, and as the value 0 if they
# started as ints.
def f11(args):
    if isinstance(args,str):
        print float(args)
    elif isinstance(args,float):
        print int(args)
    elif isinstance(args,int):
        print 0
    else:
        pass
  
###############################################################################
# Write f12() to ask for raw_input from the user. Change the input to a float.
# Create log_file.txt to log the input that cannot be changed to a float. 
#   - write one faulty input per line
# Print, as a list, all converted input.
# Proceed to the last line, calling f13, when the user types done or "done"
# Ex. log_file.txt
#   TEST
#   123abc
#   python rules
# Ex. printing
#   [1.0, 1.3, 2.443]
def f12():
    print_file =[]
    print_python = []
    user_input = raw_input("Enter an input: ")
    while user_input.strip().lower() != 'done':
        try:
            user_float = float(user_input)
        except ValueError:
            print_file.append(user_input)
        else:
            print_python.append(user_float)
        user_input = raw_input("Enter an input: ")
    print print_python
    with open("log_file.txt","w") as fout:
        for thing in print_file:
            fout.write(thing+'\r\n')
    
    f13()  # Last line in f12()
###############################################################################
# Fix the error in f13:
def f13():
    for each in "string":
        print each
    f14()  # Last line in f13()
###############################################################################
# Write f14 to print the path and filename of this script. DO NOT HARD CODE.
# You must add an import statement. Please do so at the top of the file.
# Ex. /Users/dsg/Desktop/python-boot-camp/HW11/diagnostic.py
def f14():
    print os.path.abspath("diagnostic.py")
    f15()  # Last line in f14()
###############################################################################
# Write f15 to print the goal below. Do not print any strings.
# Do not take more than nine lines to code.
# Goal:
# [[0], [], [], [], [], [], [], [], [], []]
# [[], [0], [], [], [], [], [], [], [], []]
# [[], [], [0], [], [], [], [], [], [], []]
# [[], [], [], [0], [], [], [], [], [], []]
# [[], [], [], [], [0], [], [], [], [], []]
# [[], [], [], [], [], [0], [], [], [], []]
# [[], [], [], [], [], [], [0], [], [], []]
# [[], [], [], [], [], [], [], [0], [], []]
# [[], [], [], [], [], [], [], [], [0], []]
# [[], [], [], [], [], [], [], [], [], [0]]
def f15():
    list1 = []
    list2 = [0]
    print_list = []
    for i in range(10):
        for j in range(10):
            if i == j:
                print_list.append(list2)
            else:
                print_list.append(list1)
        print print_list
        print_list = []

    f16([1,2,3],[4,5,6])  # Last line in f15()
###############################################################################
# Write f16() that takes two lists and prints a list with the nth elements of 
# each list sharing a tuple.
# Ex.
# [1,2,3] and [4,5,6] would produce [(1, 4), (2, 5), (3, 6)]
def f16(list1, list2):
    print zip (list1,list2)
    f17()  # Last line in f16()
###############################################################################
# Write f17() to take the 2nd line from few_words.txt, and print a list
# with the index of the word in that line and the word, sharing tuples.
# Ex. [(0, 'To'), (1, 'be'), (2, 'or'), (3, 'not'), (4, 'to'), (5, 'be')]
def f17():
    with open("few_words.txt","rb") as fin:
        line = fin.read().split("\n")
    list1 =[(idx,word) for idx,word in enumerate(line[1].split(" "))]
    print list1
    # Be sure to save the list that you print to list_
    list_ =  list1  # Change to your list 
    f18(list_)  # Last line in f17()
# Write f18 to take the list above and create a dictionary, use the words as
# keys and the numbers as values.
# Print the dictionary.
# Call the dictionary in f19()
def f18(list_):
    d ={idx:word for (idx,word) in list_}
    print d
    f19(d)  # Last line in f18()
# Write f19 to update that dictionary by changing the values by adding the 
# number of chars in the word to the current value (if the resulting value
# would be even), otherwise change the value to the ascii number for the last
# char in the word. Print the new dictionary.
def f19(d):
    for key in d:
        len_val = len(d[key])
        if len_val%2 == 0:
            d[key] = d[key]+str(len_val)
        else:
            d[key] = ord(d[key][len_val-1])
    print d
    f22()  # Last line in f19()
# Write f21() to find if a word is capitalized. Return True/False.
# Ex.
# f21("Yes") = True, f21("NO") = False, 
# f21("nope") = False, f21("nADA") = False
def f21(word):
    if word == word.capitalize():
        print True
    else:
        print False
 
# Write f22() to use f21() to (1) print a list of all capitalized words in 
# few_words.txt sorted by length. Then (2) remove all duplicate words.
# (3) If our favorite word (Python) is in the list, move it to the front of the 
# list (because it deserves to be there). (4) Make Python all uppercase.
# (5) If magic is in the list. Delete it. 
# (6) Add an exlamation mark to Python.
# (7) To show how special Python is to us, put all the other words in a nested
# list so they don't contaminate Python.
# (8) This latest version (second print in this function)
# Ex. second print:
# ['PYTHON!', ['Other1', 'Other_2']]
def f22():
    list_ = []
    with open("few_words.txt","rb") as fin:
        line = fin.read().strip().split("\n")
#a list of all capitalized words in few_words.txt
    for lines in line:
        list_ += [word for word in lines.strip().split(" ") if word == word.capitalize()]
    print list_
#sorting the above list
    list_ = sorted(list_,key = len)
#removing duplicates
    list_ = sorted(list(set(list_)),key = len)
#moving Python to the front
    python_index = 0
    for idx,word in enumerate(list_):
        if word == 'Python':
            python_index = idx
    list_.insert(0, list_.pop(python_index))
#making python uppercase
    list_[0] = list_[0].upper()
#Deleting magic from list
    magic_idx = 0
    for idx,word in enumerate(list_):
        if word == 'Magic':
            magic_idx = idx
    if magic_idx != 0:
        list_.pop(magic_idx)
 #Adding exclamation mark to python
    list_[0] += '!'
    list2 = []
    list2.append(list_[1:])
    list2.insert(0, list_[0])
    print list2
    f23([["o","o","x"],["x","o","x"],["o","","x"]])  # Last lines in f22()
    f23([["o","","o"],["x","o","x"],["o","x","x"]])
    f23([["o","o","x"],["x","x","x"],["o","","o"]])
# Write f23() that takes a list of three lists of len 3, and says who won in 
# tic-tac-toe (you can expect all moves to have been legal, made turn-by-turn)
# you can expect there is a winner. Print the x or o and the type of win:
# "col1", "col2", "row3", "falling_back_diag", "falling_front_diag" 
# Ex. of rows (not a finished game)
# row1 = ["o","",""]
# row2 = ["","x",""]
# row3 = ["","",""]
# Ex. of print: x, col2
def f23(lists_):
# # checking for columns
    for i in range(3):
        flag = True
        for j in range(2):
            if lists_[i][j] == lists_[i][j+1]:
                flag = flag and True
            else:
                flag = False
        if flag == True:
            print("{0}, col{1}" .format(lists_[i][j],i+1))


# checking for rows
    for j in range(3):
        flag = True
        for i in range(2):
            if lists_[i][j] == lists_[i+1][j]:
                flag = flag and True
            else:
                flag = False
        if flag == True:
            print("{0}, col{1}" .format(lists_[i][j],j+1))

# checking for falling back diag
    i = 0
    flag = True
    for j in range(2):
        if lists_[i][j] == lists_[i+1][j+1]:
            flag = flag and True
            pattern = lists_[i][j]
        else:
            flag = False
        i += 1
    if flag == True:
        print("{0}, falling_back_diag" .format(lists_[i][j]))
# checking for falling front diag
    i=2
    flag = True
    for j in range(2):
        if lists_[i][j] == lists_[i-1][j+1]:
            flag = flag and True
            pattern = lists_[i][j]
        else:
            flag = False
        i -= 1
    if flag == True:
        print("{0}, falling_front_diag" .format(pattern))


# Write main() that calls f01, then prints the The Zen of Python, by Tim Peters.
# (three lines)
def main():
    f01()
    import this


# Write the boilerplate code. (two lines)
if __name__ == '__main__':
    main()


