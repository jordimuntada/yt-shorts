from pytube import YouTube;
from pytube import Channel;
from pytube import Playlist;
import time;
import http.client;
from http.client import IncompleteRead;

http.client.HTTPConnection._http_vsn = 10;
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0';

def on_complete(stream, filename):
    print()
    print('--- Completed ---')
    print('stream:', stream)
    print('filename:', filename)

def show_length_of_video (element):
    #return YouTube(element).length;
    video = YouTube(element);
    print("data in video");
    print(video);
    raw_input("Press Enter to continue...");
    if video.length < 61:
        ys=video.streams.get_highest_resolution();
        #time.sleep(10);
        try:
            ys.download("/media/jordi/JM/YT_channel/shorts_from_the_beginning/", max_retries=10);
            video.register_on_complete_callback(on_complete);
            print ("Video - ", video.title , " - DESCARREGAT");
        except IncompleteRead:
            pass
    return 1;

#link = input("Enter the link: ");
link = "https://www.youtube.com/c/JordiMuntada/";
playlist_link= "https://www.youtube.com/watch?v=oJViEQSgwno&list=PLhXIAjoLKk9oK9CbH2cQ-ds3uThQstygp"
yt_channel = Channel(link);
yt_playlist = Playlist(playlist_link);
#video_urls
print("es el link: ", link);
print("es el playlist link: ", playlist_link);
print("video author: ", yt_channel.channel_name);
print("last updated in Playlist: ", yt_playlist.last_updated);
#print("number of videos in the playlist: ", yt_playlist.length);
print("number of videos CHANNEL urls: ", len(yt_channel.video_urls));


#reversed_video_urls = [yt_channel.video_urls[::-1] for yt_channel.video_urls in figure];
#result = map(show_length_of_video, yt_channel.video_urls); #yt_channel.video_urls);
#print(list(result));

print("videos PLAYLIST urls: ", yt_playlist.video_urls);

#Title of video
print("Title: ", yt_channel.channel_name);

#Number of views of video
print("Number of views: ", str(yt_channel.views));

#Length of the video
#print("Length of video: ",yt.length,"seconds");

#Description of video
print("About channel: ", yt_channel.about_html);

#Rating
#print("Ratings: ",yt.rating);

#printing all the available streams
#######print(yt.streams);

#ys = yt.streams.get_highest_resolution();
#ys.download("yt_shorts");

print ("FINAL");
