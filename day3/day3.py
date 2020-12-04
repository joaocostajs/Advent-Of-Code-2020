
import time

start = time.time()


with open('data.txt') as file:
    lines = file.readlines()
    lines = [n.strip() for n in lines]

lineNum = 0
trees = 0


for l in lines:
    positionInLine = lineNum * 3 
    fullLine = ''.join([l] * lineNum)
    if lineNum != 0:
        if fullLine[positionInLine] == "#":
            trees += 1
            print(fullLine)
        # print ''.join([l] * lineNum) 
    lineNum += 1

print(trees)


pass
end = time.time()
delta = end - start
print "took %.3f seconds to process" % delta




# part 2 

# code for the Right 1, down 2. since the code from part 1 works for the rest

# with open('data.txt') as file:
#     lines = file.readlines()
#     lines = [n.strip() for n in lines]

# lineNum = 0
# trees = 0


# for l in lines:
#     positionInLine = lineNum/2
#     fullLine = ''.join([l] * lineNum)
#     if lineNum != 0 and (lineNum%2) == 0:
   
#         if fullLine[positionInLine ] == "#":
#             trees += 1

#     lineNum += 1

# print(trees)

# j = 100 * 276 * 85 * 90 * 37
# print(j)













    



