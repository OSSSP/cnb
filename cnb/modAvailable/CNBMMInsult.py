#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
CNB Matrix Module
'''

import random
from cnb.cnbMatrixModule import CNBMatrixModule

class CNBMMInsult(CNBMatrixModule):
    """

    """

    name = 'insult'
    usage = ''
    desc = 'Reply some shit when the bot detect an insult'
    enProcessCmd = False
    enProcessPattern = True

    INSULT_MSG = ['fuck you', 'go fuck yourself', 'wtf', 'stfu', 'fuck', 'suck my dick', 'DIAF', 'get lost', 'cry me a river', 'a2m time?', 'stop being a loser']
    INSULT_ANSWER = ["Wrong! You cheating scum!","And you call yourself a h4ck3r ?!","Where did you learn to type?","Are you on drugs?","I don't wish to know that.","My mind is going. I can feel it.","Maybe if you used more than just two fingers...","I've seen penguins that can type better than that.","You speak an infinite deal of nothing","Sure, I've seen people like you before - but I had to pay an admission...","Shouldn't you have a license for being that ugly?","Calling you an idiot would be an insult to all the stupid people.","Listen, are you always this stupid or are you just making a special effort today?","Sure, I'd love to help you out...now, which way did you come in?","People like you are the reason I'm on medication.","Don't piss me off today, I'm running out of swap space","I am not anti-social..I just don't like you","Have you considered suing your brain for non-support?"]

    def __init__(self,log):
        CNBMatrixModule.__init__(self,log)
        
    def __del__(self):
        pass

    def checkPattern(self,oMsg):
        if oMsg.text in self.INSULT_MSG:
            return True
        else:
            return False
                
    def processPattern(self,oMsg):
        return self.INSULT_ANSWER[random.randint(1,len(self.INSULT_ANSWER)-1)]
