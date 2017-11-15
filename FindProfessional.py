'''
Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.
'''
def findProfession(level, pos):
    if level == 1 and pos == 1:
        return "Engineer"
    else:
        ans = "E"
        i = 2
        while i <= level:
            j = 0
            temp = ""
            while j < len(ans):
                if ans[i] == "D":
                    temp += "DE"
                else:
                    temp += "ED"
                j += 1
            ans = temp
            i += 1
        return "Doctor" if ans[pos-1] == "D" else "Engineer"
        
        
