
class Scripts(object):
    """ A text in multiple languages 
    Input is a dict: ex. {"en": "Hello, World!", "la": "Ave, Munde!"}
    """ 
    def __init__(self, input=None):
        self.text = input
    
def translate(scripts, f, i=script.text.keys[0]):
    """ Translate text of Scripts instance from language i to language f """
    if f in scripts.text:
        while True:
            abort = input("Overwrite current version? (y/N)").lower()
            if abort in ['n', '']: return
            elif abort == 'y': scripts.text[f] = [
            else: print("Oops! (y/N)")
        scripts.text[f] = ""
    for line in scripts.text[i].split('\n'):
        print(line)
        scripts.text[f]
        
        
        
