#Name: Aurelio Siordia
#Date: 07/04/23

#8-9 Messages
messages=['Hi everyone', 'Have a nice day', 'Where are you from?', 'Nice to meet you']
def show_messages(messages):
    """Display messages"""
    for message in messages:
        print(message)

show_messages(messages)
print()

# 8-10 Sending Messages
sent_messages=[]
def send_messages(messages, sent_messages):
    """Move messages to sent_messages"""
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    

send_messages(messages, sent_messages)
print(messages)
print(f'{sent_messages}\n')    


# 8-11 Archived Messages
messages=['Hi everyone', 'Have a nice day', 'Where are you from?', 'Nice to meet you']
sent_messages=[]
send_messages(messages[:], sent_messages)
print(messages)
print(f'{sent_messages}\n') 

