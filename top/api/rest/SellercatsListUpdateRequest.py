'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class SellercatsListUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.name = None
		self.pict_url = None
		self.sort_order = None

	def getapiname(self):
		return 'taobao.sellercats.list.update'
