'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class RefundMessageAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None
		self.image = None
		self.refund_id = None

	def getapiname(self):
		return 'taobao.refund.message.add'

	def getMultipartParas(self):
		return ['image']
