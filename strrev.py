line = str(raw_input())
x=line.split()
print(" ".join(i[::-1] for i in x ))
