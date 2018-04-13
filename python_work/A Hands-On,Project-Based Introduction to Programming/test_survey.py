#coding=utf-8
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	#���AnonymousSurvey��Ĳ���
	
	def setUp(self):
		#����һ����������һ��𰸣���ʹ�õĲ��Է���ʹ��
		question = "What is your favorite language?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Chinese','Spanish']
	
	def test_store_single_response(self):
		#���Ե����𰸻ᱻ���Ƶش洢
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
		
	def test_store_three_response(self):
		#���������𰸻ᱻ���Ƶش洢
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
		
		self.assertIn(response,self.my_survey.responses)
		
unittest.main()
