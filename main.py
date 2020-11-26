import random

while True:
    
    select = input("If you want to select the chapter and the amount of questions type: choose\nIf want an otomatic chapter number type: oto\n") 
   
    if select.lower()=="choose" or select.lower()=="oto":
        
        num = input("How questions do you want to assign?\n")
        
        for i in range(0,int(num)):
        
            if select.lower()=="choose":
        
                chapNum = input("Chapter number: ")
                queNum = input("Question number: ")
                chapter = random.randint(1,int(chapNum))
                question = random.randint(1,int(queNum))
                print("\nChapter:",chapter," Question:",question)
            
            else:
            
                chapter = random.randint(1,3)
                question = random.randint(1,16)
                print("\nChapter:",chapter," Question:",question)
     
        break           
    
    else:
        print("Wrong selection.")
        


