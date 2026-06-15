                                #Exception Handling

#When we run a program in python there are various exception that can be raised.
#like- syntax Error, name error ,Zero division error etc

#Exception Handling Functionalities

# try - this will catch the exception if any and pass to -

# Execpt - Except will deal with the Exception you can have custom Exception or Universal Catcher.

# Else -Else will be executed if no exception occers or it wont be executed

# finally - This will definitely run no matter what happens

# Raise - Raises a custom error as you need.


# Example

a = int(input("Provide your number1: "))
b = int(input("Provide your number2: "))

try:
    print(a/b)

except Exception as err:
    print(f"Sorry an error occured as {err}")

print(a+b)

#Example 2

a = int(input("Provide your number1: "))
b = int(input("Provide your number2: "))

try:
    print(a/b)

except ZeroDivisionError as err:
    print(f"Sorry an error occured as {err}")
else:
    print("There was no errors")
finally:
    print("I will execute no matter what !!")

print(a+b)


# Example 3

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("You must be 18+")
    print("Access granted")
except Exception as e:
    print("Error:", e)


