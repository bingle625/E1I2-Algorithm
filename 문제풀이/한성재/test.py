
f1 = open("D:/Han-Seongjae/algorithm/E1I2/문제풀이/한성재/proverbs.txt")
lines = f1.readlines()
f2 = open("test.txt", "w")
f2.writelines(lines)
f3 = open("test.txt")
print(f3.read())
