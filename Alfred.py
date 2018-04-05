from Utils import Utils
from random import randint

class Alfred(object):

	def __init__(self):
		self.util = Utils()

	def addQuestion(self,question):
		self.util.saveQuestion(question)
		return True

	def addStatement(self,statement):
		self.util.saveStatement(statement)
		return True

	def getAnswer(self,phrase):
		if(phrase[-1:] == '?'):
			self.addQuestion(phrase)
			return self.util.getAnswer(phrase)
		else:
			self.addStatement(phrase)
			ran = randint(0,1)
			if(ran==1):
				return self.util.getStatement()
			else:
			 	print("[ALFRED]: "+self.util.getQuestion())
				answer = raw_input("[YOU]: ")
				self.util.saveAnswer(self.util.getQuestion(),answer)
				return self.util.getStatement()
