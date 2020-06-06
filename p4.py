birthdays = {'Sahil':'July 1', 'Aastha':'Nov 6'}

print('water')
print('Fire')
print('Ice')
print('Earth')
print('GOD')

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
       print(birthdays[name] + ' is the birthdate of ' + name)
    else:
       print('I do not have birthday information for ' + name)
       print('What is their birthday?')
       bday = input()
       birthdays[name] = bday
       print('Birthday database updated.')
       print('testing....')
