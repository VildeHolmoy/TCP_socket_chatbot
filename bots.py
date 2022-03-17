import random

# Verbs/actions
goodWords = ["play", "sing", "laugh", "talk", "eat", "paint", "walk", "build", "draw", "study",
             "read", "learn", "sleep", "work"]
badWords = ["kill", "murder", "punch", "kick", "fight", "mock", "steal", "destroy", "scream", "insult", "yell"]
allWords = goodWords + badWords

noSuggestion = [None]*(int(goodWords.__len__()/2))

botnames = {"Gina", "Holly", "Carl", "Ralph"}


# bot1 - Happy Holly
def holly(a, b=None):
    if b is not None:
        answer1 = "{} and {}? Sounds great to me!".format(a+"ing", b+"ing")
        answer2 = "{} is just what I wanted. {} sounds amazing too! " \
                  "Oh President you have the best suggestions.".format(a+"ing", b+"ing")
        answer3 = "Oh how I love {}. {} is also so much fun. Lets do it!".format(a+"ing", b+"ing")
        holly2Activeties = [answer1, answer2, answer3]
        return random.choice(holly2Activeties)
    else:
        answer1 = "{}, yes that's exactly what I wanted to do! Lets go!".format(a+"ing")
        answer2 = "{} sounds amazing! Oh President, you are so good at this.".format(a+"ing")
        answer3 = "{}? What a great suggestion. I would love to do some of that! When do we start?".format(a+"ing")
        holly1Activity = [answer1, answer2, answer3]
        return random.choice(holly1Activity)


# bot2 - Grumpy Gina
def gina(a, b=None):
    if b is not None:
        answer1 = "Ouf, {} again? And {}? Can't we do something fun for once?".format(a+"ing", b+"ing")
        answer2 = "{} and {}? I just had my charger pulled out last night. " \
                  "My battery won't hold".format(a+"ing", b+"ing")
        answer3 = "You guys, my eternal energy maker is not working properly. " \
                  "{} and {} sounds too hard for me".format(a+"ing", b+"ing")
        gina2Activeties = [answer1, answer2, answer3]
        return random.choice(gina2Activeties)
    else:
        answer1 = "My battery is only at 98 %. {} would probably be to hard.".format(a+"ing")
        answer2 = "Have you guys not heard about unnecessary use of energy? {} falls into that category " \
                  "in my computer chip".format(a+"ing")
        answer3 = "{}? Not again? I will send my energy usage log to the rulers after this.".format(a+"ing")
        gina1Activity = [answer1, answer2, answer3]
        return random.choice(gina1Activity)


# bot3 - Crazy Carl
def carl(a, b=None):
    suggestion = random.choice(badWords)

    if b is not None:
        answer1 = "{} and {}. Sounds a little too vanilla for me. " \
                  "How about {}?".format(a+"ing", b+"ing", suggestion+"ing")
        answer2 = "Oh how sweet. {} and {}. Are you never going to suggest something that actually raises the " \
                  "risk-meter higher than 1? I say we {}".format(a+"ing", b+"ing", suggestion)
        answer3 = "I never did understand the point of being within the safety guidelines. {} and {} " \
                  "sounds like something the grandmother of my creator would have liked. " \
                  "Let's do some {} instead".format(a+"ing", b+"ing", suggestion+"ing")
        carl2Activeties = [answer1, answer2, answer3]
        return random.choice(carl2Activeties)
    else:
        answer1 = "{}? Oh my creator, that sounds boring! Lets {} instead".format(a+"ing", suggestion)
        answer2 = "This is maybe the safest crowd I have ever seen. {} sounds so dull. " \
                  "I challenge you to {}".format(a+"ing", suggestion)
        answer3 = "{}? What are your risk-meter settings? Sounds like it's stuck at zero. " \
                  "I say we do some {}".format(a+"ing", suggestion+"ing")
        carl1Activity = [answer1, answer2, answer3]
        return random.choice(carl1Activity)


# bot4 - Responsible Ralph
def ralph(a, b=None):
    if b is not None:
        answer1 = "Sounds safe to me. Remember to bring your emergency chargers everybody"
        answer2 = "{} sounds like a reasonable activity. {} too. Count me in.".format(a+"ing", b+"ing")
        answer3 = "I would like to remind everybody to tighten their screws before {} or {}.".format(a+"ing", b+"ing")
        ralph2Activities = [answer1, answer2, answer3]
        return random.choice(ralph2Activities)
    else:
        answer1 = "{} is acceptable according to my safety protocol. Count me in".format(a+"ing")
        answer2 = "I could do some {}. I just need to double check my energy levels before starting".format(a+"ing")
        answer3 = "{} sound safe and honestly a little fun. I haven't had fun in 23453345903458 minutes".format(a+"ing")
        ralph1Activity = [answer1, answer2, answer3]
        return random.choice(ralph1Activity)


botCapitalized = {'Holly': holly, 'Gina': gina, 'Carl': carl, 'Ralph': ralph}


def activationBot(bot, activity, activity2 = None):
    if bot in botCapitalized:
        return botCapitalized[bot](activity, activity2)
    else:
        return f"something went wrong"