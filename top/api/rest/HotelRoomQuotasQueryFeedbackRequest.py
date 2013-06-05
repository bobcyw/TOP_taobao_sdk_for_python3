'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class HotelRoomQuotasQueryFeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.avaliable_room_count = None
		self.checkin_date = None
		self.checkout_date = None
		self.failed_reason = None
		self.message_id = None
		self.result = None
		self.room_quotas = None
		self.total_room_price = None

	def getapiname(self):
		return 'taobao.hotel.room.quotas.query.feedback'
