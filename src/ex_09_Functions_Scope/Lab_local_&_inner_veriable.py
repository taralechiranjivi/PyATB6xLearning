# Inner Veriavles
pb_global_b = 12

def my_function():
    pb_a = 10
    print(pb_a)
    print(pb_global_b)

# print(pb_a)
print(pb_global_b)
my_function()


public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)
    # print(private_toilet)

# Local variables
public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)
home()

# Local & Inner Function
def outer_function():
    var1 = 30 # local

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function2():
        print(var1)


    inner_function()
    inner_function2()

outer_function()
#inner_function()


