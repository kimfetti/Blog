from youtube_transcript_api import YouTubeTranscriptApi

video_ids = ['5-yxXzLX2QY', '9UuFTwUxkLw']

out, _  = YouTubeTranscriptApi.get_transcripts(video_ids)

text_out = {}
for video_id in out:
    text_out[video_id] = ' '.join([x.get('text', '') for x in out[video_id]])


print(text_out)
