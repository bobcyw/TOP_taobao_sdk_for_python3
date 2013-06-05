'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class ItemPropimgUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.image = None
		self.num_iid = None
		self.position = None
		self.properties = None

	def getapiname(self):
		return 'taobao.item.propimg.upload'

	def getMultipartParas(self):
		return ['image']
