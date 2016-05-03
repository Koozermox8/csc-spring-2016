def half_pyramid(levels, symbol):
    symbols = "" #empty string called before loop
    for i in range(0, levels):
        symbols = symbols + symbol #prints pyramid using function parameter
        print(symbols)

def full_pyramid(levels, symbol):
    for i in range(1, levels+1): 
        symbols = ""
        x = symbol[0]
        s = i + (i-1) #correctly positions characters when printed
        for j in range(0, levels - i):
            symbols = symbols + " " #prints blank spaces to center symbol/symbols per level
        for j in range(0, s): #begins printing in the proper places for each level
            symbols = symbols + x
        print(symbols)

        
def parabola(xs, xe):
    for i in range(xs, xe):
        y = (i*i)/4 #determines the spacing for printing the parabola
        symbols = ""
        for j in range(0,int(y)):
            symbols = symbols + " " 
        symbols = symbols + "."
        print(symbols)

##def circle(radius):
##    for x in range(-1*radius, radius):
##        y = ((radius*radius)-(x*x))**(1/2)
##        if x == 0 or x == radius or x == radius:
            
    
