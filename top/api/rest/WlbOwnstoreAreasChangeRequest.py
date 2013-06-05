'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class WlbOwnstoreAreasChangeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area_codes = None
		self.service_code = None
		self.type = None

	def getapiname(self):
		return 'taobao.wlb.ownstore.areas.change'
