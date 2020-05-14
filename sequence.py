from pprint import pprint
import os

BIT0 = []
BIT1 = []
BIT2 = []

helpText = '''
1. First enter the number of tones you want to use.
2. Then enter the number of times you want to generate the tone
3. Then enter the keys as indicated below
4. Mention the duration you want one tone to run for as well
5. Open the asc file and run the simulation.
6. A 'output.wav' file will be generated with the final output
'''

print(helpText)

#  Need to change this
mapping = {'0': 262, '1': 294, '2': 311, '3': 349, '4': 391, '5': 466, '6':  588, '7': 622}
pprint(mapping)

seq = 0
duration = 0
totalDuration = 0

N = int(input('Enter number of tunes: '))
Y = int(input('Number of repetitions: '))
for i in range(N):
    seq = int(input("Tone " + str(i) + " : "))
    duration = int(input("Duration of tune (in milliseconds) " + str(i) + " : "))
    if seq > 7:
        seq = 7
    elif seq < 0:
        seq = 0
    totalDuration += duration
    bit0 = (seq % 2)*5
    bit1 = int((seq/2) % 2)*5
    bit2 = int((seq/4) % 2)*5

    if len(BIT0) > 0 and bit0 != int(BIT0[-1].split(" ")[1]):
        BIT0.append("+{}ms {}".format(str(0.000001), str(bit0)))

    if len(BIT1) > 0 and bit1 != int(BIT1[-1].split(" ")[1]):
        BIT1.append("+{}ms {}".format(str(0.000001), str(bit1)))

    if len(BIT2) > 0 and bit2 != int(BIT2[-1].split(" ")[1]):
        BIT2.append("+{}ms {}".format(str(0.000001), str(bit2)))

    BIT0.append("+{}ms {}".format(str(duration), str(bit0)))
    BIT1.append("+{}ms {}".format(str(duration), str(bit1)))
    BIT2.append("+{}ms {}".format(str(duration), str(bit2)))

with open('bit0.txt', 'w') as bit0File:
    for bit in BIT0:
        bit0File.write('')

with open('bit1.txt', 'w') as bit1File:
    for bit in BIT1:
        bit1File.write('')

with open('bit2.txt', 'w') as bit2File:
    for bit in BIT2:
        bit2File.write('')

if Y > 1:
    if int(BIT0[0].split(" ")[1]) != int(BIT0[-1].split(" ")[1]):
        BIT0.append("+{}ms {}".format(str(0.000001), BIT0[0].split(" ")[1]))

    if int(BIT1[0].split(" ")[1]) != int(BIT1[-1].split(" ")[1]):
        BIT1.append("+{}ms {}".format(str(0.000001), BIT1[0].split(" ")[1]))

    if int(BIT2[0].split(" ")[1]) != int(BIT2[-1].split(" ")[1]):
        BIT2.append("+{}ms {}".format(str(0.000001), BIT2[0].split(" ")[1]))

for _ in range(Y):
    with open('bit0.txt', 'a') as bit0File:
        for bit in BIT0:
            bit0File.write(bit+os.linesep)

    with open('bit1.txt', 'a') as bit1File:
        for bit in BIT1:
            bit1File.write(bit+os.linesep)

    with open('bit2.txt', 'a') as bit2File:
        for bit in BIT2:
            bit2File.write(bit+os.linesep)

ascFile = ''
with open('final_with_clk.asc', 'r') as dataFile:
    ascFile = dataFile.readlines()

totalDuration = str(Y*totalDuration)
index = ascFile.index(list(line for line in ascFile if '!.tran' in line)[0])
newLine = " ".join(ascFile[index].split(' ')[:-1]) + " {}m\n".format(totalDuration)

ascFile[index] = newLine

with open('final.asc', 'w') as outputFile:
    for line in ascFile:
        outputFile.write(line)
