import json
import os.path
from random import randint

class Utils(object):
	
	def __init__(self):
		if(os.path.isfile("brain.json")):
			print("[INFO]: Brain exists.")
			self.data = json.load(open("brain.json"))
		else:
			print("[INFO]: Brain does not exist.")
			self.buildBrain(True)
			self.data = json.load(open("brain.json"))
	

	def saveQuestion(self,question):
		brain = self.data["questions"]
		brain[question] = brain[question]["count"] +1 if question in brain else {"count":1,"answers":{}}
		with open('brain.json', 'w') as outfile:
			json.dump(self.data, outfile)

	def saveAnswer(self,question,answer):
		brain = self.data["questions"]
		brain[question]["answers"][answer] = brain[question]["answers"][answer] +1 if answer in brain[question]["answers"] else 1
		with open('brain.json', 'w') as outfile:
			json.dump(self.data, outfile)

	def saveStatement(self,statement):
		brain = self.data["statements"]
		brain[statement] = brain[statement] +1 if statement in brain else 1
		with open('brain.json', 'w') as outfile:
			json.dump(self.data, outfile)


	def buildBrain(self,check):
		if(check):
			f = open("brain.json",'a')
			f.write("{\"statements\":{},\"questions\":{},\"interests\":{},\"dislikes\":{}}")
			f.close()
			return True
		return False

	def getStatement(self):
		i = randint(0,len(self.data["statements"])-1) if len(self.data["statements"])-1 >0 else 0
		return list(self.data["statements"])[i]

	def getQuestion(self):
		i = randint(0,len(self.data["questions"])-1) if len(self.data["questions"])-1 >0 else 0
		return list(self.data["questions"])[i]

	def getAnswer(self,question):
		if(question in self.data["questions"]):
			if(len(self.data["questions"][question]["answers"]) > 0):
				i = randint(0,len(self.data["questions"][question]["answers"])-1) if len(self.data["questions"][question]["answers"])-1 >0 else 0
				answer = list(self.data["questions"][question]["answers"])[i]
			else:
				i = randint(0,len(self.data["statements"])-1) if len(self.data["statements"])-1 > 0 else 0
				answer = list(self.data["statements"])[i]
		else:
			i = randint(0,len(self.data["statements"])-1) if len(self.data["statements"])-1 > 0 else 0
			answer = list(self.data["statements"])[i]
		return answer





