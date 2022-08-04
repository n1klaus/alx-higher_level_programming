* 0-answer.txt - name of the function would you use to print the type of an object
* 1-answer.txt - name of the function to get the variable identifier 
* 2-answer.txt
> Answer to if `a` and `b` point to the same object
    > a = 89
    > b = 100
* 3-answer.txt
> Answer to if `a` and `b` point to the same object
    > a = 89
    > b = 89
* 4-answer.txt
> Answer to if `a` and `b` point to the same object
    > a = 89
    > b = a
* 5-answer.txt
> Answer to if `a` and `b` point to the same object
    > a = 89
    > b = a + 1
* 6-answer.txt
> Answer to what is printed
    > s1 = "Best School"
    > s2 = s1
    > print(s1 == s2)
* 7-answer.txt
> Answer to what is printed
    > s1 = "Best"
    > s2 = s1
    > print(s1 is s2)
* 8-answer.txt
> Answer to what is printed
    > s1 = "Best School"
    > s2 = "Best School"
    > print(s1 == s2)
* 9-answer.txt
> Answer to what is printed
    > s1 = "Best School"
    > s2 = "Best School"
    > print(s1 is s2)
* 10-answer.txt
> Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = [1, 2, 3] 
    > print(l1 == l2)
* 11-answer.txt
> Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = [1, 2, 3] 
    > print(l1 is l2)
* 12-answer.txt
> Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = l1 
    > print(l1 == l2)
* 13-answer.txt
> Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = l1 
    > print(l1 is l2)
* 14-answer.txt
>Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = l1
    > l1.append(4)
    > print(l2)
* 15-answer.txt
> Answer to what is printed
    > l1 = [1, 2, 3]
    > l2 = l1
    > l1 = l1 + [4]
    > print(l2)
* 16-answer.txt
> Answer to what is printed
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* 17-answer.txt
> Answer to what is printed
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* 18-answer.txt
> Answer to what is printed
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
* `19-copy_list.py` - function `def copy_list(l):` that returns a copy of a list.
* 20-answer.txt
> Answer to if it is a tuple
    > a = ()
* 21-answer.txt
> Answer to if it is a tuple
    > a = (1, 2)
* 22-answer.txt
> Answer to if it is a tuple
    > a = (1)
* 23-answer.txt
> Answer to if it is a tuple
    > a = (1, )
* 24-answer.txt
> Answer to what is printed
    > a = (1)
    > b = (1)
    > a is b
* 25-answer.txt
> Answer to what is printed
    > a = (1, 2)
    > b = (1, 2)
    > a is b
* 26-answer.txt
> Answer to what is printed
    > a = ()
    > b = ()
    > a is b
* 27-answer.txt
> Answer to if the last line will print 139926795932424
    > id(a)
        > 139926795932424
    > a
        [1, 2, 3, 4]
    > a = a + [5]
    > id(a)
* 28-answer.txt
> Answer to if the last line will print 139926795932424
    > a
        > [1, 2, 3]
    > id (a)
        > 139926795932424
    > a += [4]
    > id(a)
* `100-magic_string.py` - function `magic_string()` that returns a string **“BestSchool”** n times the number of the iteration
* `101-locked_class.py` -  class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`
* 103-line1.txt
> Answer to how many int objects are created by the execution of the first line
    > a = 1
    > b = 1
* 103-line2.txt
> Answer to how many int objects are created by the execution of the second line
    > a = 1
    > b = 1
* 104-line1.txt
> Answer to how many int objects are created by the execution of the first line
    > a = 1024
    > b = 1024
    > del a
    > del b
    > c = 1024
* 104-line2.txt
> Answer to how many int objects are created by the execution of the second line
    > a = 1024
    > b = 1024
    > del a
    > del b
    > c = 1024
* 104-line3.txt
> Answer to after the execution of line 3, if the int object pointed by `a` deleted
    > a = 1024
    > b = 1024
    > del a
    > del b
    > c = 1024
* 104-line4.txt
> Answer to after the execution of line 4, if the int object pointed by `b` deleted
    > a = 1024
    > b = 1024
    > del a
    > del b
    > c = 1024
* 104-line5.txt
> Answer to how many int objects are created by the execution of the last line
    > a = 1024
    > b = 1024
    > del a
    > del b
    > c = 1024
* 105-line1.txt
> Answer to before the execution of line 2 **(print("Love"))**, how many int objects have been created and are still in memory?
    > print("I")
    > print("Love")
    > print("Python")
* 106-line1.txt
> Answer to how many string objects are created by the execution of the first line
    > a = "SCHL"
    > b = "SCHL"
    > del a
    > del b
    > c = "SCHL"
* 106-line2.txt
> Answer to how many string objects are created by the execution of the second line
    > a = "SCHL"
    > b = "SCHL"
    > del a
    > del b
    > c = "SCHL"
* 106-line3.txt
> Answer to after the execution of line 3, if the string object pointed by `a` deleted
    > a = "SCHL"
    > b = "SCHL"
    > del a
    > del b
    > c = "SCHL"
* 106-line4.txt
> Answer to after the execution of line 4, if the string object pointed by `b` deleted
    > a = "SCHL"
    > b = "SCHL"
    > del a
    > del b
    > c = "SCHL"
* 106-line5.txt
> Answer to how many string objects are created by the execution of the last line
    > a = "SCHL"
    > b = "SCHL"
    > del a
    > del b
    > c = "SCHL"