# Letter Generator

# Program to generate customized messages using a template and a list of
# people.
#
# Learn about file accesses: read and write; also about absolute vs
# relative paths

print('Reading original message ...')

with open('input/lists/message.txt') as file:
    original_message = file.read()

print('Reading list of names ...')

with open('input/message/people.csv') as file:
    for name in file.readlines():
        name = name.replace('\n', '').strip()
        file_name = f'letter_{name.lower()}.txt'
        message = original_message.replace('[name]', name)

        print(f'Saving letter for {name} ...')

        with open(f'output/{file_name}', mode='w') as output:
            output.write(message)

print('Done!')
