#
# Get the fizzbuzz content based on the numeric value
#
# @param int value
#
# @return string
#
def fizzbuzz(value):

    output = ''

    if value % 3 == 0:
        output += 'fizz'

    if value % 5 == 0:
        output += 'buzz'

    if output == '':
        output = str(value)

    return output


#
# Main program
#
max_value = input("What's the highest number you want to check? ")
max_value = int(max_value)

i = 1
while (i <= max_value):
    content = fizzbuzz(i)
    print(content)
    i += 1

