username="siva"
password="1234"
def login(u,p):
    return username==u and password==p
def show_reels(u,p):
    login(u,p)
    if(login(u,p)):
        return "insta posts,reels displayed"
    else:
        return "login invalid"
print(show_reels("siva","1234"))