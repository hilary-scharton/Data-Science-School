#An SMS Simulation


class SMSMessage:
    """constructor for class SMSMessage"""
    def __init__(self, hasBeenRead, messageText, fromNumber):
        self.hasBeenRead = hasBeenRead
        self.messageText = messageText
        self.fromNumber = fromNumber
    hasBeenRead = False

    sms_store = []
    number_of_messages = len(sms_store)

    def mark_as_read(self):
        """will change hasBeenRead to True"""
        self.hasBeenRead = True

    def get_message(self):
        """let user select message by index and read message"""
        message_number = input('Read message number: ')
        for i in range(number_of_messages):
            if sms_store.index == message_number:
                return SMSMessage

    def unread_messages(self):
        """let user fetch all messages for which hasBeenRead is false"""
        for i in range(number_of_messages):
            if i.self.hasBeenRead is False:
                return SMSMessage

    add_sms = sms_store.append(SMSMessage)  # add new message to list
    get_count = sms.store.count()           # total number of messages in list, read and unread
    remove_sms = sms_store.pop()            # remove message from list by index number


userChoice = ""

while userChoice != "quit":
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        for item in sms_store:
            if item.self.hasBeenRead is False:
                print(SMSMessage)
    elif userChoice == "send":
        number = input('Enter phone number: ')
        message = input('Enter message text: ')
        sms_store.append(number + message)
    elif userChoice == "quit":
        print "Goodbye"
    else:
        print "Oops - incorrect input"
