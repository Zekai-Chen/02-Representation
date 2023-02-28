import math #in standard library
Basic = {1:"2(0)",2:"2"} 
#Two basic situation for recursion

def RecurPow2(Number):
    if Number in Basic:
        return Basic[Number]
    else:
        Power=int(math.log2(Number)) #import at first faster than __import__('math').log2() everytime
        #math.log2()
        #Return Value:	A float value, representing the base-2 logarithm of a number
        Min2Power=pow(2,Power)
        #Number = Min2Power + small number may exist
        return (RecurPow2(Min2Power)+"+"+RecurPow2(Number-Min2Power)) if (Number!=Min2Power) else ("2("+RecurPow2(Power)+")")
        #Follow the rule of writing from right to left, in order of most significant digit to least significant digit

Number=int(input())
print(RecurPow2(Number))

