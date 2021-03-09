from argumentHandler import argumentHandler

def add(args):
    print(args)
    pass

def main():
    inputargs = "test.py add -n name"
    inputprepared = inputargs.split(" ")
    
    hand = argumentHandler({add : 
        {"-l" : [True, str],
         "-n" : [True, str]}}, inputprepared, {'add' : add})
    hand.startFunction()

main()