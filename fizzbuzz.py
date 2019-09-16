

# My version of fizzbuzz for python 3
# I also wanted to practice string interpolation in this example.


fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = "FizzBuzz!!"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{fizzbuzz} {i}")
    elif i % 3 == 0:
        print(f"{fizz} {i}")
    elif i % 5 == 0:
        print(f"{buzz} {i}")
