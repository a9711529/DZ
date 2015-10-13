names = ['Alex F', 'Ira N', 'Ira C', 'Ivan A', 'Luda S', 'Petr I']
f = open('students.log', "r")
actions = f.readlines()

##################
# Part 2
##################
index = int(input("Enter index: "))

if index < len(names):
    print(names[index])
else:
    print("Out of range")

##################
# Part 3
##################
srez = str(input("Enter Begin and End: "))
lst = srez.split(' ')
if len(lst) == 2:
    print(names[int(lst[0]):int(lst[1])])
else:
    print(names)

#################
# Part 4
#################
count = 0
for name in names:
    if ('p' in name) or ('P' in name):
        count += 1
print("Names with literal 'p' or 'P': " + str(count))

#################
# Part 5
#################
tmp = []
newLst = names.copy()
for a, name in enumerate(names):
    name = name.split(' ')
    i = 0
    while i < len(names):
        if (names[i].startswith(name[0] + ' ')) and (i != a):
            tmp.append(newLst.pop(i))
            tmp.append(newLst.pop(a))
            names.remove(names[i])
            names.remove(names[a])
            newLst.insert(i,tmp.copy())
            tmp.clear()

        i += 1
del names
print(newLst)

#################
# Part 6
#################
name = input('Enter your name: ')

for act in actions:
    act = act.split(' ')
    if act[3] == name.replace(' ', '_'):
        message = '''
Yor action: {0} - {1}
on date {2} and {3} time \n
'''
        message = message.format(act[2], act[4], act[1], act[0])
        print(message)

#################
# Part 7
#################
action = input('Choice your action (GET, POST, UPDATE): ')
action = action.split(' ')

for act in action:
    for ac in actions:
        ac = ac.split(' ')
        if ac[2] == act.upper():
            message = '''
User name: {0}
action: {1} - {2}
on date {3} and {4} time \n
'''
            message = message.format(ac[3], ac[2], ac[4], ac[1], ac[0])
            print(message)
