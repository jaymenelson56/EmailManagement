subscribers = set()
unsubscribers = set()

def add_email(email, set_name):
    set_name.add(email)
    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"Email '{email}' removed from {'subscribers' if set_name == subscribers else 'unsubscribers'}.")
    else:
        print(f"'{email}' was not found in {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

def display_emails(set_name):
    set_label = 'subscribers' if set_name == subscribers else 'unsubscribers'
    print(f"{set_label}:")
    if set_name:
        for email in set_name:
            print(email)
    else:
        print(f"No emails in {'subscribers' if set_name == subscribers else 'unsubscribers'}")

def find_active_subscribers():
    active_subscribers = subscribers - unsubscribers
    return active_subscribers



add_email("Luigi@mushroom.com", subscribers)
add_email("Mario@mushroom.com", subscribers)
add_email("Peach@mushroom.com", subscribers)
add_email("Toad@mushroom.com", subscribers)
add_email("Yoshi@mushroom.com", subscribers)

add_email("Mario@mushroom.com", unsubscribers)
add_email("Toad@mushroom.com", unsubscribers)

remove_email("Mario@mushroom.com", unsubscribers) 
remove_email("Wario@mushroom.com", unsubscribers)    

display_emails(subscribers)
display_emails(unsubscribers)

print("Active Subscribers:")
active_subs = find_active_subscribers()
for email in active_subs:
    print(email)