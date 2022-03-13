import random

# Verbs/actions
goodWords = ["play", "sing", "laugh", "talk", "eat", "paint", "walk", "build", "draw", "study",
             "read", "learn", "sleep", "work", "code"]
badWords = ["kill", "murder", "punch", "kick", "fight", "mock", "steal", "destroy", "scream",
            "break", "hurt", "abuse", "harm", "insult", "yell"]
allWords = goodWords + badWords


# bot1 - Happy Holly
def holly(a, b = None):
    if b != None:
        return "{} and {} at the same time? Sounds great to me!".format(a+"ing", b+"ing")
    else:
        return "{} sounds awesome! Lets gooo".format(a+"ing")


# bot2 - Grumpy Gina
def gina(a, b = None):
    if b != None:
        return "I don't feel like {}. I don't really want to {} either. Why do you always " \
               "come up with such bad suggestions?".format(a+"ing", b+"ing")
    else:
        return "Ugh, not {}. That's so boring".format(a+"ing")


# bot3 - Crazy Carl
def carl(a, b = None):
    suggestion = random.choice(badWords)
    while (suggestion == a) or (suggestion == b):
        suggestion = random.choice(badWords)

    # Here, I can write more advanced code if a and b is good words.
    if b != None:
        return "{} and {} is okay I guess, but what about {}?".format(a+"ing", b+"ing", suggestion+"ing")
    else:
        return "I guess we could do some {}, but what about {}?".format(a+"ing", suggestion+"ing")


# bot4 - Responsible Ralph
# Here, I can also write more advanced code to respond to Carl
def ralph(a, b = None):
    if b != None:
        return "You are going to far again, Carl. {} or {} sounds safe. Lets do that".format(a+"ing", b+"ing")
    else:
        return "Carl, you need to calm down. At least while {}, we will walk away from it" \
               "without physical harm".format(a+"ing")


# thePresident - the bot who starts the dialog
## Unsure how this will be implemented.
# def president()