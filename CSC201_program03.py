#Jason Vessella
#Program 4

import operator
 
memory = [] #emptry list to save memory
 
def lex_complex_expr(s): 
 
    if '(' in s: 
        _s = s.replace(" ", "") #removes spaces entered
 
        results = [] #empty list stores results of expression
 
        pstr = ""
        inp = False
       
        for c in s:
            if c == ")": #checks if c is the end of the expression
                x,y,z = lex_expr(pstr)
                if simpleExpressionIsValid(x,y,z): #checks if next chunk of input is valid
                    results.append([x,y,z])
                    pstr = ""
                    inp = False
                else:
                    return False #returns false if next part is false
            elif inp == False and (c == "+" or c == "-" or c == "*" or c == "/"):
                results.append(c) 
            elif c == "(": 
                inp = True
            else:
                pstr = pstr + c
 
        return results #returns the results of entered expression
       
    else:
        return lex_expr(s) #runs next function if no parentheses
 
def lex_expr(s):
   
    _s = s.replace(" ", "") #removes spaces
 
    x = ''
    y = ''
    z = '' #declares variables
 
    for i,c in enumerate(_s):
        if c == '+' or c == '-' or c == '/' or c == '*': #checks for operators
            x = _s[:i]
            y = c  #breaks string into three parts, int, operator, int
            z = _s[i+1:] 
            break #stops loop
 
    return x,y,z #returns new values of variables
           
 
def lex_mem(s):
 
    try:
        return int(stmt.split(" ")[1])#tries to get number after the last one
    except IndexError:
        return -1 #if not, -1 returned as error
   
 
def simpleExpressionIsValid(a, s, b):
 
    ops = ['+', '-', '/', '*'] 
   
    try:
        _a = int(float(a))
        _b = int(float(b))
 
        _s = ops.index(s)
       
        return True
    except ValueError: #returns false if expression is invalid
        return False
 
def evaluateSimpleExpression(a, s, b):
   
    ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
 
    _a = int(float(a))
    _b = int(float(b))
 
    return ops[s](_a,_b)
 
# ignores order of operations
def evaluateComplexExpression(cexpr):
 
    if len(cexpr) == 1:
        return evaluateSimpleExpression(cexpr[0][0], cexpr[0][1], cexpr[0][2])
 
    nstr = ""
 
    # Evaluate inner expressions
    for i,l in enumerate(cexpr):
        if l == "+" or l == "-" or l == "*" or l == "/":
            pass
        else:
            cexpr[i] = evaluateSimpleExpression(l[0], l[1], l[2]) #calls other function to solve expression
 
    # Evaluate outter expressions
    result = 0
    i = 3
    x = cexpr[0]
    y = cexpr[1]
    z = cexpr[2]
    while True:
        if not simpleExpressionIsValid(x,y,z) #checks again if part is valid
            return False
 
        x = evaluateSimpleExpression(x,y,z) #evaluates part of the complex expression
 
        if i >= len(cexpr): #checks if more to expression
            break
       
        y = cexpr[i] 
        z = cexpr[i+1] #moves on to next part if more
 
        i += 2
 
    return x
   
   
def addToMemory(expr):
    if len(memory) == 5:
        memory.reverse() #reverses string
        memory.pop() #returns last value of list
        memory.reverse()
    memory.append(expr) #adds expression to memory
 
# Expects int
def viewLastOfMemory(n):
   
    if n > len(memory):
        print("Invalid range to view") #checks if memory called exists
        return
 
    memory.reverse()
 
    for i in range(0, n): #prints all memory
        print(memory[i])
 
    memory.reverse()
 
while True:
 
    print #looks neater with white space
 
    stmt = input('Enter an expression: ') #user input
 
    if stmt == 'end': #ends program if 'end' is typed by user
        break
 
    elif "last" in stmt: #if last is typed
        lm = lex_mem(stmt) 
 
        if lm != -1:
            viewLastOfMemory(lm) 
        else:
            print('Memory stack contains', memory) #prints last recorded expression
 
    else:
 
        arr = lex_complex_expr(stmt) #calls function that checks for complex
 
        if isinstance(arr, tuple):
            result = evaluateSimpleExpression(arr[0], arr[1], arr[2]) #calls simple expression function
 
            if result == False:  
                print('Invalid expression')
            else:
                addToMemory(stmt + ' = ' + str(result)) #if valid, adds to memory and prints result
                print('Result is', result)
 
        elif arr != False:
            result = evaluateComplexExpression(arr) #calls complex function
 
            if result == False:
                print('Invalid expression')
            else:
                addToMemory(stmt + ' = ' + str(result))
                print('Result is', result)
        else:
            print('Invalid expression')
