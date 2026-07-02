#a fake news generators

#1-- import the rendom module 
import random
#2--create subject
subjects=[
    "lala ",
    "virat kohali"
    ,"a mumbai cat",
    "nirmala sitaraman",
    "auto rikshaw driver from delhi",
    "prime minister modi"
    "Aalsi Robot",
    "Gullu Software Engineer",
    "chai vala hacker"
]

actions =[
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrations",
    "samosa kha kr ",
    "coding karte huye",
    "reels dekhte huye"
]
palce_or_things=[
    "at red fort",
    "in mumbai local train",
    "at ganga ghat",
    "inside parliament",
    "suring ipl match",
    "india gate",
    "mars per chala gya ",
    "office mein so gaya",
    "code crash kar diya"
]
# 3 starts the headling generators loop
while True:
    s = random.choice(subjects)
    a= random.choice(actions)
    palce = random.choice(palce_or_things)

    headline = f"BREAKING NEWS :{s} {a} {palce}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no) ").strip().lower()
    if user_input=="no":
        break
    #print goodbye message

print("\nthanks for using the fake nes]ws headline generator. have a fun day")