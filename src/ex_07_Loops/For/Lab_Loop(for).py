# Loops
# range - range( start, stop-1, step)
# Repeat block of code

### Interview QUE.
for i in range(1, 10, 1):
     print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0,10,3):
    print(i)

# it will gives error(no float/points take )
#for i in range(0, 10, 1.5):
#    print(i)

for i in range(2, 10):
    print(i)

# IMP
for i in range(10):
    print(i)

# No Output
for i in range(-1, 10, -1):
    print(i)
    print("bcd")

### Interview QUE.
# How many time code run------- 10 times(print 0 to 9)
for i in range(10):
    print("Heloo world")
### for reverse range
for i in range(10, 0, -1):
    print(i)

### O/p-- range(10)
#num = range(10)
#print(num)

### For real Use
for test_id in range(1,6):
    print("Running the test case : ", test_id)
    print(f"Running the test cases : {test_id}")

for test_id in range(20):
    print("This is even No. ", 2)



