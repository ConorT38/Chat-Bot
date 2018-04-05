import json
import sys
import os
from Alfred import Alfred

class ChatBot(object):

	def __init__(self):
		self.alfred = Alfred()

	def listen(self,phrase):
		answer = self.alfred.getAnswer(phrase)
		return self.say(answer)

	def say(self,answer):
		print("[ALFRED]: "+answer)

chatbot = ChatBot()
while(True):
	phrase = raw_input("[YOU]: ")
	chatbot.listen(phrase)
