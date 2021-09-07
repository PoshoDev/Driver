import os, subprocess

mat = "601341p"

def main():
    print("Loading programs for "+mat+"...")
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
            a, la = GetList("correct"+Ext(i, j))
            b, lb = GetList(Out(i, j))
            for k in range(len(a)):
                check = '=' if a[k]==b[k] else 'X'
                print("| " + Spaces(a[k], la) + " | " +check+" | "+ Spaces(b[k], lb) + " |")
                if (a[k] != b[k]): errors += 1
            print("ERRORS: "+str(errors))
            j += 1
        i += 1
        fname = mat + str(i) + ".py"

def Ext(i, j):
    return "_"+str(i)+"_"+str(j)+".txt"

def Inp(i, j):
    return "input" + Ext(i, j)
    
def Out(i, j):
    return "output" + Ext(i, j)
    
def GetList(fname):
    l = []
    biggest = 0
    with open(fname) as f:
        l.append(f.read().splitlines())
        for i in range(len(l[0])):
            if len(l[0][i]) > biggest:
                biggest = len(l[0][i])
    return l[0], biggest
    
def Spaces(res, size):
    for i in range(size-len(res)):
        res += ' '
    return res
    
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
        
if __name__ == "__main__":
    main()