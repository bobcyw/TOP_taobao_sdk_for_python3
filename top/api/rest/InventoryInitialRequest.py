'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class InventoryInitialRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.items = None
		self.store_code = None

	def getapiname(self):
		return 'taobao.inventory.initial'
