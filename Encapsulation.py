
#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
'''It describes the idea of bundling data and methods
that work on that data within one unit, e.g., a class in Java.
This concept is also often used to hide the internal representation,
or state, of an object from the outside'''


class MyValue(object):
    # setting new value
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val
    # Get the setted value
    def get_val(self):
        print(self.val)
    # Increment the setted value by one
    def increment_val(self):
        self.val = self.val + 1
        print(self.val)

a = MyValue()
a.set_val(10)
a.get_val()
a.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with an int
c = MyValue()
c.val = 15
c.get_val()
c.increment_val()
print("\n")
#
# # Trying to break encapsulation in a new instance with a str
b = MyValue()
b.val = "MyNewString"  # <== Breaking encapsulation, works fine
b.get_val()        # <== Prints the val set by breaking encap
b.increment_val()  # This will fail, since str + int wont work
print("\n")
