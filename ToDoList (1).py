#arian & yazmin
#01/11/24
#to do list

#initialize


symbolList= [" ╣"]

def completed(word):
    word = input("what would you like to mark as done?")
    i = symbolList.index(word)
    symbolList[i] = " ╣"

BDL = ["powder", "Blush", "Jacket", "Heels", "Perfume", "Toner"]

while True: 
    option = input(print("what option do you want to do \n1.view \n2.add \n3.done \n4.remove \n5.exit"))
    if option == "view":
        print(BDL)
        if option == "add":
            BDL.append(input("what do you want to add?"))
            print(BDL)

    if option == "done":
       word=input("what would you like to mark as done?")
       x=BDL.index(word)
       BDL[x]=(word +"x")
       print(BDL)
    if option == "remove":
          BDL.remove(input("what would you like to remove"))
    if option == "exit":
          quit()


#main
completed()
    
