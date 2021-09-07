import os, subprocess

mat = "601341p"

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
    
def RunPython(fname, i, j):
    os.system("python "+fname+".py < "+Inp(i, j)+" > "+Out(i, j))

def RunCpp(fname):
    return

def RunJava(fname):
    return

def LookFor(name, ext):
    if os.path.exists(name + ext):
        return True
    return False

def RunCode(mat, i, j):
    name = mat + str(i)
    if LookFor(mat, ".py"):
        RunPython(name, i, j)
        return True
    elif LookFor(mat, ".cpp"):
        RunCpp(name, i, j)
        return True
    elif LookFor(mat, ".java"):
        RunJava(name, i, j)
        return True
    return False
        



print("Loading your programs...")

i = 1
fname = mat + str(i) + ".py"
while os.path.exists(fname):
    print("Running "+fname+"...")
    j = 1
    while os.path.exists(Inp(i, j)):
        RunCode(mat, i, j)
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