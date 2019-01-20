def launchRA(text):
    if text == "hi" or text == "Hi":
        return ("Hello")
    elif text == "Our Team" or text == "Our team" or text == "our team":
        return "Lahari, Avinash, Sushmita, Tarun"
    elif text == "End" or text == "end":
        return "Thanks for using our product!"
    else:
        return "Command Unknown\nTry : Help"