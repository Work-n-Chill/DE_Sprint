# task 2 string palindrome
x = "t a co c at"

def isPalindrome(a):
    a = a.replace(" ", "")
    rev_a = a[::-1]
    if (a == rev_a):
        return True
    else:
        return False
    

print(isPalindrome(x))


# task 3 arab to roman
def toRome(x):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM"]
    
    t = thous[x//1000]
    h = hunds[x//100%10]
    te = tens[x//10%10]
    o = ones[x%10]
    return t+h+te+o
    
print(toRome(10))
print(toRome(1999))


# task 4 brackets validity
def bracketsValidity(str):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    check_list = []
    for s in str:
        if s in brackets_open:
            check_list.append(s)
        if s in brackets_closed:
            if len(check_list) == 0:
                return False
            index = brackets_closed.index(s)
            open_br = brackets_open[index]
            if check_list[-1] == open_br:
                check_list = check_list[:-1]
            else: return False
    return (not check_list)

print(bracketsValidity(")({})"))
print(bracketsValidity("({})"))


# task 5 binary number multiply

def bin_n_multiply(x, y):
    return (bin(int(x, base=2) * int(y, base=2)))


print(bin_n_multiply("101", "101"))
