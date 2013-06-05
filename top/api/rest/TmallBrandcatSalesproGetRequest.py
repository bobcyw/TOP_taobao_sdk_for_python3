'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class TmallBrandcatSalesproGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.brand_id = None
		self.cat_id = None

	def getapiname(self):
		return 'tmall.brandcat.salespro.get'
