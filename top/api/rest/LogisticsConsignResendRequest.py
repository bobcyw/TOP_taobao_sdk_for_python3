'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class LogisticsConsignResendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.company_code = None
		self.feature = None
		self.is_split = None
		self.out_sid = None
		self.seller_ip = None
		self.sub_tid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.consign.resend'
