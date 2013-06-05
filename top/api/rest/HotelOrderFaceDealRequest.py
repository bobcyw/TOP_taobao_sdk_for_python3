'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class HotelOrderFaceDealRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.oper_type = None
		self.reason_text = None
		self.reason_type = None

	def getapiname(self):
		return 'taobao.hotel.order.face.deal'
