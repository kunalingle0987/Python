import random

names=["rohit sharma","Narendra Modi","rahul gandhi","salman khan","viky kaushal",
      " kareena kapoor","nana patekar","cat","dog"]

actions=["Dancing on the","flying from","hanging in ","run from",
        "sleep on side","bathing openly","ride on "," fly in water"]

places=["river","gateway","on road","in tup","donky","cycle","delhi"]

while True:
    name=random.choice(names)
    action=random.choice(actions)
    place=random.choice(places)
    print(f"BREAKING..! {name} {action} {place}")
    
    alert=input("Are you wat to continue? (yes?no) ").lower()
    
    if(alert=="no"):yes
    
        break
    