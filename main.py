from cloner import Cloner
from utils.colors import COLORS

from time import sleep

def main():
    #define global variables
    globals()["tmp"] = 0
    globals()["Domain"] = Cloner.Domain()

        
    #in case the user opts to check possible usernames from first and last name
    if Cloner.mode() == "COMPOSE USERNAME":
        #loop through each list of usernames and map each element with check function
        [list(map(check,usernames)) for usernames in Cloner.username_composer()]
        sleep(5)
        cloner.driver.quit()

    #in case the user opts to directly check if username is available
    else:
        username = Cloner.get_username()
        check(username)
        sleep(5)
        cloner.driver.quit()
        

def check(username):
    #initialize global variables
    global tmp;
    global cloner;
    global Domain;

    
    #instantiate Cloner object if global cloner instance doesn't exist 
    if 'cloner' not in globals():
        cloner= Cloner()

    
    
    # if there is 5 consecutive available emails break the map iteration and move to other usernames list
    if tmp == 5:
        raise StopIteration
    
    #in case username is unavailable
    if (username_status := getattr(cloner,f'check_{Domain}')(username)) is False:
        print(f"{COLORS[Domain]}{Domain.upper()}   :",end="    ")
        print(f"{COLORS['failure']}{username}@{Domain}.com")
        print(COLORS['reset'],end="")
        #set tmp to 0
        tmp = 0
   
    #in case username is available but there is no facebook account linked to the email
    elif username_status is True and (facebook_status := cloner.check_facebook(f"{username}@yahoo.com")) is False:
        print(f"\n{COLORS[Domain]}{Domain.upper()}   :",end="    ")
        print(f"{COLORS['success']}{username}@{Domain}.com")
        print(f"{COLORS['facebook']}FACEBOOK:",end="    ")
        print(f"{COLORS['failure']}{username}@{Domain}.com",end="\n")
        print(COLORS["reset"])

        tmp += 1
    
    #in case username is available and there is facebook account linked to the email
    elif username_status is True and facebook_status is True:
        print(f"\n{COLORS[Domain]}{Domain.upper()}   :",end="    ")
        print(f"{COLORS['success']}{username}@{Domain}.com")
        print(f"{COLORS['facebook']}FACEBOOK:",end="    ")
        print(f"{COLORS['failure']}{username}@{Domain}.com",end="\n\n")
        print(COLORS["reset"])

        tmp += 1

    
if __name__ == "__main__":
    main()