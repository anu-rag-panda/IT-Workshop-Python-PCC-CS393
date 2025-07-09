# Accessing and slicing
s = "HelloWorld"
print(s[0])        # H
print(s[2:7])      # lloWo
print(s[::-1])     # dlroWolleH (reversed)

# Using string methods
s = "  Python Is Fun!  "
print(s.lower())        # python is fun!
print(s.strip())        # Python Is Fun!
print(s.replace("Fun", "Awesome"))  # Python Is Awesome!
print(s.split())        # ['Python', 'Is', 'Fun!']
