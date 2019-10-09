#%%
sum = 0
secondsum = 0
for x in range(10):
    sum = sum + x
    secondsum = secondsum + x * x

#%%
def double(input):
    for x in input:
        print(x*2)


#%%
def exponent(x,y):
    z = x 
    for n in range(1,y):
        z = z * x
    return z

#%%
exponent(5, 3)

#%%
