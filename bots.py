import random

# Activities
goodWords = ["play", "sing", "laugh", "talk", "eat", "paint", "walk", "build", "draw", "study",
             "read", "learn", "sleep", "work", "stretch", "wonder", "relax", "cook", "teach", "research",
             "discover", "roll", ]
badWords = ["kill", "murder", "punch", "kick", "fight", "mock", "steal", "destroy", "scream", "insult", "yell",
            "crash", "creep", "throw", "drink", "party"]
allWords = goodWords + badWords

noSuggestion = [None]*(int(goodWords.__len__()/3))                              # Activity2 needs to be None sometimes

botnames = {"Gina", "Holly", "Carl", "Ralph"}                                   # List of botnames


# bot1 - Happy Holly
def holly(a, b=None):
    if b is not None:                                                           # If activity2 is suggested by the President
        answer1 = "Good suggestions mr. President. {} and {} sounds " \
                  "great to me!".format(a.capitalize()+"ing", b+"ing")
        answer2 = "Yes! {} is just what I wanted. {} sounds amazing too. " \
                  "Oh mr.President you have the best " \
                  "suggestions.".format(a.capitalize()+"ing", b.capitalize()+"ing")
        answer3 = "Oh how I love {}. {} is also so much fun. " \
                  "Lets do it!".format(a+"ing", b.capitalize()+"ing")
        holly2Activeties = [answer1, answer2, answer3]
        return random.choice(holly2Activeties)
    else:                                                                       # If activity2 is not suggested by the President
        answer1 = "Yay, {}! That's exactly what I wanted to do! " \
                  "Lets go!".format(a+"ing")
        answer2 = "Oh President, you are so good at this. " \
                  "{} sounds amazing!".format(a.capitalize()+"ing")
        answer3 = "What a great suggestion. " \
                  "I would love to do some {}! " \
                  "When do we start?".format(a+"ing")
        holly1Activity = [answer1, answer2, answer3]
        return random.choice(holly1Activity)


# bot2 - Grumpy Gina
def gina(a, b=None):
    if b is not None:                                                            # If activity2 is suggested by the President
        answer1 = "Ouf, {} again? And {}? Can't we do " \
                  "something fun for once?".format(a+"ing", b+"ing")
        answer2 = "{} and {}? I just had my charger pulled out last night. " \
                  "My battery won't hold.".format(a.capitalize()+"ing", b+"ing")
        answer3 = "You guys, my eternal energy maker is not working properly. " \
                  "{} and {} sounds too hard for me.".format(a.capitalize()+"ing", b+"ing")
        gina2Activeties = [answer1, answer2, answer3]
        return random.choice(gina2Activeties)
    else:                                                                       # If activity2 is not suggested by the President
        answer1 = "My battery is only at 98 %. {} would " \
                  "probably be to hard.".format(a.capitalize()+"ing")
        answer2 = "Have you guys not heard about unnecessary use of " \
                  "energy? {} falls into that category " \
                  "in my computer chip.".format(a.capitalize()+"ing")
        answer3 = "{}? Not again? I will send my energy usage log " \
                  "to the rulers after this.".format(a.capitalize()+"ing")
        gina1Activity = [answer1, answer2, answer3]
        return random.choice(gina1Activity)


# bot3 - Crazy Carl
def carl(a, b=None):
    suggestion = random.choice(badWords)                                        # Carl only uses bad words

    if b is not None:                                                           # If activity2 is suggested by the President
        answer1 = "No, not {} and {}. That sounds a little too vanilla for me. " \
                  "How about {}?".format(a+"ing", b+"ing", suggestion+"ing")
        answer2 = "Oh how sugary sweet. {} and {}. Are you never going to " \
                  "suggest something that actually raises the " \
                  "risk-meter higher than 1? \n" \
                  "I say we {}.".format(a.capitalize()+"ing", b+"ing", suggestion)
        answer3 = "I never did understand the point of being " \
                  "within the safety guidelines. \n" \
                  "{} and {} sounds like something the grandmother of " \
                  "my creator would have liked. " \
                  "Let's do some {} instead".format(a.capitalize()+"ing", b+"ing", suggestion+"ing")
        carl2Activeties = [answer1, answer2, answer3]
        return random.choice(carl2Activeties)
    else:                                                                       # If activity2 is not suggested by the President
        answer1 = "What? Are you serious? {}? Oh my creator, that sounds boring! " \
                  "Lets do some {} instead.".format(a.capitalize()+"ing", suggestion+"ing")
        answer2 = "This is maybe the safest crowd I have ever seen. " \
                  "{} sounds so dull. " \
                  "I challenge you to {}.".format(a.capitalize()+"ing", suggestion)
        answer3 = "What are your risk-meter settings? {}? " \
                  "Sounds like it's stuck at zero. " \
                  "I say we do some {}.".format(a.capitalize()+"ing", suggestion+"ing")
        carl1Activity = [answer1, answer2, answer3]
        return random.choice(carl1Activity)


# bot4 - Responsible Ralph
def ralph(a, b=None):
    if b is not None:                                                           # If activity2 is suggested by the President
        answer1 = "Sounds safe to me. Remember to bring your " \
                  "emergency chargers everybody."
        answer2 = "I think {} sounds like a reasonable activity. {} too. " \
                  "Count me in.".format(a+"ing", b.capitalize()+"ing")
        answer3 = "I would like to remind everybody to tighten their " \
                  "screws before {} or {}.".format(a+"ing", b+"ing")
        ralph2Activities = [answer1, answer2, answer3]
        return random.choice(ralph2Activities)
    else:                                                                       # If activity2 is not suggested by the President
        answer1 = "{} is acceptable according to my safety protocol. " \
                  "Count me in".format(a.capitalize()+"ing")
        answer2 = "I could do some {}. I just need to double check my energy " \
                  "levels before starting.".format(a+"ing")
        answer3 = "That sounds so safe and honestly a little fun. I haven't " \
                  "had fun in 23453345903458 minutes." \
                  ""
        ralph1Activity = [answer1, answer2, answer3]
        return random.choice(ralph1Activity)


botFunctions = {'Holly': holly, 'Gina': gina, 'Carl': carl, 'Ralph': ralph}     # Connects botnames with their functions


# Receives prompt from clients, responds with the bot matching the username of the client
def activationBot(bot, activity, activity2=None):
    if bot in botFunctions:                                                     # if client is matching function
        return botFunctions[bot](activity, activity2)                           # Run function with the right name
    else:
        return f"something went wrong".encode('utf-8')
