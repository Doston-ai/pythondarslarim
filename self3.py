#Create a countdown program that starts at 10 and counts down to 1.

#When it reaches 1, print "Liftoff!".
def function():

    n = 10
    
    while n>0:
        if n==1:
            print('Liftoff!')
        else:
            print(n)
        n-=1    
function()
