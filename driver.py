import os, subprocess

def Ext(i, j):
    return "_"+str(i)+"_"+str(j)+".txt"

def Inp(i, j):
    return "input" + Ext(i, j)
    
def Out(i, j):
    return "output" + Ext(i, j)
    
def GetList(fname):
    l = []
    with open(fname) as f:
        l.append(f.read().splitlines())
    return l[0]

mat = "601341p"

print("Loading your programs...")

i = 1
fname = mat + str(i) + ".py"
while os.path.exists(fname):
    print("Running "+fname+"...")
    j = 1
    while os.path.exists(Inp(i, j)):
        os.system("python "+fname+" < "+Inp(i, j)+" > "+Out(i, j))
        print("Test Case #"+str(j)+"...")
        
        errors = 0
        
        # Loading Outputs
        a = GetList("correct"+Ext(i, j))
        b = GetList(Out(i, j))
            
        for k in range(len(a)):
            check = '=' if a[k]==b[k] else 'X'
            print("| " + a[k] + " | " +check+" | "+ b[k] + " |")
            if (a[k] != b[k]): errors += 1
        
        print("ERRORS: "+str(errors))
        
        
        j += 1
    i += 1
    fname = mat + str(i) + ".py"