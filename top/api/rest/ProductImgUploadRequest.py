'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class ProductImgUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.image = None
		self.is_major = None
		self.position = None
		self.product_id = None

	def getapiname(self):
		return 'taobao.product.img.upload'

	def getMultipartParas(self):
		return ['image']
