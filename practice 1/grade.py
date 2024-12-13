p,i,e = int(input("Project Marks: ")),int(input("Internal Marks: ")),int(input("External Marks: "))
if not(p>=50 and i>=50 and e>=50):
    print("Failed in project: ",p) if p<50 else None
    print("Failed in internal: ",i) if i<50 else None
    print("Failed in external: ",e) if e<50 else None
else:
    tot = 0.7*p + 0.1*i + 0.2*e
    print("Your Grade is: {}".format("A" if tot>90 else "B" if tot>80 else "C"))