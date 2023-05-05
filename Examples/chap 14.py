s = {{1, 2}, {4, 5}}
s = {[1, 2], [4, 5]}
s = {(1, 2), (4, 5)}

student1 = {"peter", "john", "tim"}
student2 = {"peter", "johnson", "tim"}
print(student1.issuperset({"john"}))
print(student1.issubset(student2))
print({1, 2, 3} > {1, 2, 4})
print({1, 2, 3} < {1, 2, 4})
print({1, 2} < {1, 2, 4})
print({1, 2} <= {1, 2, 4})

set1 = {2, 3, 7, 11}
print(4 in set1)
print(3 in set1)
print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
print(set1.issubset({2, 3, 6, 7, 11}))
print(set1.issuperset({2,3, 7, 11}))


d = {1:[1, 2], 3:[3, 4]}
d = {[1, 2]:1, [3, 4]:3}
d = {(1, 2):1, (3, 4):3}
d = {1:"john", 3:"peter"}
d = {"john":1, "peter":3}



def main():
 d = {"red":4, "blue":1, "green":14, "yellow":2}
 print(d["red"])
 print(list(d.keys()))
 print(list(d.values()))
 print("blue" in d)
 print("purple" in d)
 d["blue"] += 10
 print(d["blue"])
main()



def main():
 d = {}
 d["susan"] = 50
 d["jim"] = 45
 d["joan"] = 54
 d["susan"] = 51
 d["john"] = 53
 print(len(d))
 print(d)
main()