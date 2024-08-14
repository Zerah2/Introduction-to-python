#Let's store a favourite number
FavouriteNumber = 88
print(f"My favourite number is {FavouriteNumber}")

#string variable
greeting = "Hello, PLP"
print(greeting)

#boolean
is_python_fun = True
print(f"is python fun ? {is_python_fun}")

#control flow: if, elif, else
temperature = 30
if temperature > 25:
    print("It's hot outside! Wear shorts.")
elif temperature > 15:
    print("It's warm. Maybe try a light jacket.")
else:
    print("Be warned! It's cold here, please bundle up!")

#For and while loops
for i in range(5):
    print(f"This is a for loop iteration {i} ")

    #while
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown  -= 1
print("Blast off!")

#Define a function
def greet(name):
    return f"Hello, {name}"
#Apply the function
print(greet("Abenjo"))
print(greet("Hannah"))