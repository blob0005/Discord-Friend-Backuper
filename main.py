error = False
try:
    import os
    os.system("title " + "Discord Friend Backuper")
except:
    pass
try:
    import discum, discord, requests
except:
    error = True
if error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install discord")
        os.system("pip install discum")
        os.system("pip install requests")
        print("Error May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Fix")
        input("")
        exit()
invite_code = "weYYXeUSNm"
while True:
    tokens = input("Enter Token: ")
    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        print("Invalid Token")
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            break
        if "403" in str(r):
            print("Locked Token")
def adder():
    try:
        file = open("friends_save.txt")
        frend = file.readlines()
        file.close()
        list = []
        dine = 0
        for frind in frend:
            dine = int(dine) + 1
            if "\n" in frind:
                list.append(frind[:-1])
            else:
                list.append(frind)
            print(f"[{str(dine)}] Loaded User, {str(frind)}")
    except:
        print("Could Not Find The Save File")
        input("")
        exit()
    print("Press Enter To Start Adding")
    input("")
    try:
        bot = discum.Client(token=tokens)
        for usa in list:
            bot.requestFriend(str(usa))
        bot.gateway.run()
    except:
        print("Unkown Error")
    print("Done")
    input("")
    exit()
def scraper():
    print("Friend Scraper, Press Enter To Start")
    input("")
    userr = discord.Client()
    @userr.event
    async def on_connect():
        done = 0
        for user in userr.user.friends:
            done = int(done) + 1
            id = user.id
            file = open("friends_save.txt", "a")
            file.write(str(id)+"\n")
            file.close()
            print(f"[{str(done)}] Scraped " + str(id))
        print("Done")
        input("")
        exit()
    userr.run(tokens, bot=False)
while True:
    tools = input("""
1. Friend Scraper
2. Friend Adder
3. How Use
> """)
    if tools == "1" or tools == "2" or tools == "3":
        break
    else:
        print("Enter A Valid Choice")
if tools == "1":
    scraper()
if tools == "2":
    adder()
if tools == "3":
    print("""
1. Scrape Friends (1)
(It Will Save All Ids In A Txt File Make Sure To Save That Somwhere
2. Now You Probably Gotten Banned So Enter The New Token When You Run This Program Then Start The Adder (2)
(Make Sure To Put The Txt File That You Got Earlier In The Same Folder
3. Now If You Started 2 It Should Start To Add All Your Friends, If It Stopped Its Done""")
    input("")