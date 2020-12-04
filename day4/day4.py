
import time

start = time.time()


with open('data.txt') as file:
    lines = file.readlines()
    lines = [n.strip() for n in lines]
arrayOfPassports = []
temporaryData = ""
for l in lines:
    if l != "":
        temporaryData+= l
    if l == "":
        arrayOfPassports.append(temporaryData)
        temporaryData = ""
    
## after loop finnishes there is the last temporary data still to be save soo will be done here
arrayOfPassports.append(temporaryData)
temporaryData = ""


fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"]
exception = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

correct = 0
for idx, el in enumerate(arrayOfPassports):
    if all(x in arrayOfPassports[idx] for x in fields) or all(x in arrayOfPassports[idx] for x in exception):
        print("true")
        correct+=1
    else: 
        print("false")

print(correct, "correct")
pass
end = time.time()
delta = end - start
print "took %.3f seconds to process" % delta




# part 2 







    



