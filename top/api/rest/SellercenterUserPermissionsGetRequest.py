'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class SellercenterUserPermissionsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None

	def getapiname(self):
		return 'taobao.sellercenter.user.permissions.get'
