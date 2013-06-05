'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class PictureCategoryUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.category_name = None
		self.parent_id = None

	def getapiname(self):
		return 'taobao.picture.category.update'
