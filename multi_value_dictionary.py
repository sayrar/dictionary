from collections import defaultdict

class Dictionary:
    def __init__(self):

        self.d = defaultdict(list)

    def keys(self):


        key_list = list(self.d.keys())
        if(len(key_list)==0):
            print("(empty set)")

        for i in range(len(key_list)):
            print("%s) %s" %(i+1, key_list[i]))



        return key_list

    def members(self, key):
        if(key in self.d.keys()):
            for i in range(len(self.d[key])):
                print("%s) %s" %(i+1, self.d[key][i]))
            return self.d[key]
        else:
            print(") ERROR, key does not exist.")
            

    def add(self, key, value):

        if(value  in self.d[key]):
            print("ERROR, member already exists for key")
            return

        self.d[key] += [value]
        print('Added')
        
    def remove(self, key, value):
        #Check if key exists
        if(key not in self.d.keys()):
            print('Error, key does not exist')
            return
        if(value not in self.d[key]):
            print('Error, member does not exist')
            return
        self.d[key].remove(value)
        if(len(self.d[key]) == 0):
            self.d.pop(key)

        print('Removed')


    def removeall(self, key):

        if(key not in self.d.keys()):
            print("ERROR, key does not exist")
        else:
            self.d.pop(key)
            print("Removed")

    def clear(self):

        self.d.clear()
        print('Cleared')

    def keyexists(self, key):

        if(key in self.d.keys()):
            print('true')
            return True
        else:
            print('false')
            return False
    
    def memberexists(self, key, value):

        if(value in self.d[key]):

            print('true')
            return True
        else:
            print('false')
            return False

    def allmembers(self):

        _list = []
        for key in self.d:
            _list.append(self.d[key])
        _list = [val for sublist in _list for val in sublist]

        if (not _list):
            print('(empty set)')
            return None
        else:
            for i in range(len(_list)):
                print("%s) %s" %(i+1, _list[i]))

        return _list

    def items(self):

        if(not self.d.items()):
            print ('(empty set)')
            return None
        count = 1
        for key in self.d.keys():
            for vals in self.d[key]:
                print("%s) %s: %s" %(count, key, vals))
                count = count +1

        return self.d.items()



if __name__ == '__main__':
    d = Dictionary()
    while True:

        
        command = input("> ").split()

        if(len(command)==0):
            print("Please enter a valid command")

        elif(len(command)>3):
            print('More arguments than expected - Please try again')


        elif(command[0] == 'KEYS'):
            d.keys()
        
        elif(command[0] == 'MEMBERS'):
            if(len(command) != 2):
                print('2 arguments are needed - Please try again')
            else:
                d.members(command[1])

        elif(command[0] == 'ADD'):
            if(len(command) != 3):
                print('3 arguments are needed - Please try again')
            else:
                d.add(command[1], command[2])

        

        elif(command[0] == 'REMOVE'):
            if(len(command) != 3):
                print('3 arguments are needed - Please try again')
            else:
                d.remove(command[1], command[2])
        
        elif(command[0] == 'REMOVEALL'):
            if(len(command) != 2):
                print('3 arguments are needed - Please try again')
            else:
                d.removeall(command[1])
            

        elif(command[0] == 'CLEAR'):
            d.clear()

        elif(command[0] == 'KEYEXISTS'):
            if(len(command) != 2):
                print('2 arguments are needed - Please try again')
            else:
                d.keyexists(command[1])

        elif(command[0] == 'MEMBEREXISTS'):

            if(len(command) != 3):
                print('3 arguments are needed - Please try again')
            else:
                d.memberexists(command[1], command[2])

        elif(command[0] == 'ALLMEMBERS'):

            d.allmembers()

        elif(command[0] == 'ITEMS'):

            d.items()

        elif(command[0] == 'Q'):
            break
        
    
        

