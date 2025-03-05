from workflow.utility import *
from YTChannelConfig import *
from MongoConfiguration import *

channel_details_list = get_channel_details(channel_id_dict)
video_id_lst= get_videos_list('UUKTWY-rVwUqCxrVmPOlJyjA')
videos_details = get_video_details(video_id_lst)
popular_comments_lst = get_popular_comments('3lM89xFmwFU')


ytscrapping_db = client.YoutubeScrapping
print('database configuration successful!')


ytscrapping_db.channel_details.insert_many(channel_details_list)


# database cleaned up
# ytscrapping_db.channel_details.drop()
# print('database cleaned up successfully')



