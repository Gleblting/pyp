import time
start_time= time.time()
def fun(a, b):
    return a + b
end_time= time.time()
y = fun(5, 6)
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.0345