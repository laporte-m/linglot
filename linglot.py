
class Scripts(object):
    """ A text in multiple languages 
    Input is a dict: ex. {"en": "Hello, World!", "la": "Ave, Munde!"}
    """ 
    def __init__(self, text={}, name="Not a name"): 
        self.text = text
        self.lngs = list(text)

    def read(self, lng, res):
        ''' Acquire translation from text file'''
        with open(res, 'r') as file:
            self.text[lng] = file.read()

    def squash(self, srcs=None):
        ''' Zip together same lines from different translations '''
        if not srcs: 
            srcs = self.lngs
        return list(zip(*[self.text[lng].split('\n') for lng in srcs]))

    def write(self, lng, res=None):
        ''' Write translation to text file '''
        if not res: 
            res = "{}.txt".format(lng)
        file = open(res, 'w')
            
    
def translate(scripts, target, src=None):
    """ Manual, line-by-line translate text of Scripts object 
        from language i to language f 
    """
    if not src: src = scripts.lngs[0]
    if target in scripts.text:
        while True:
            abort = input("Overwrite current version? (y/N)").lower()
            if abort in ['n', '']: 
                return
            elif abort == 'y':     
                break
            else:                  
                print("Oops! (y/N)")

    lines_in = scripts.text[src].split('\n')
    lines_out = []
    for i, line in enumerate(lines_in):
        if line:
            print("{}, {}:\t{}".format(src, i, line))
            new = input("{}, {}:".format(target, i))
        else:
            new = '\n'
        lines_out.append(new)
    scripts.text[target] = '\n'.join(lines_out)
        
        
        
