from pickle import *
class Sports:
    def __init__(self):
        print('This channel provides sports news')
    
class Politics:
    def __init__(self):
        print('This channel provides political news')
class Education:
    def __init__(self):
        print('This channel provides educational news')
class news:
    def __init__(s):
        print('this is a news channel')
    def getAllNews(s):
        s.sport=Sports()
        s.politics=Politics()
        s.education=Education()
    
        
n=news()  
#serialisation of object  
with open('sport.scr','wb') as f:
    dump(n,f)
    print('\nserialisation completed\n')
    
    
    
#deserialisation of object  
with open('sport.scr','rb') as f:
    new_obj=load(f)
    
new_obj.getAllNews()