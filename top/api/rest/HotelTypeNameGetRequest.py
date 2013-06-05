'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class HotelTypeNameGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.hid = None
		self.name = None

	def getapiname(self):
		return 'taobao.hotel.type.name.get'
