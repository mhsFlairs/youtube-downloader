from pytube import YouTube
from pytube.cli import on_progress

basePath="Videos"

failures=[]

def Download(link,index,totalNumberOfVideos):
    youtubeObject = YouTube(link,on_progress_callback=on_progress)
    youtubeObject = youtubeObject.streams.get_by_resolution("720p")
    try:
        print(f"Downloading: {youtubeObject.title}")
        youtubeObject.download("Videos")
        print(f"Downloaded: {youtubeObject.title} successfully. Downloaded {index+1}/{totalNumberOfVideos} videos")
    except:
        print("An error has occurred. Failed to download the video.")
        failures.append(link)
        return
    print("")

def DownloadVideos():
    urls=[]

    if not os.path.exists("videos.txt"):
        print("videos.txt file not found. Please create a videos.txt file and add the links of the videos you want to download.")
        exit()

    with open("videos.txt", "r") as file:
        for line in file:
            urls.append(line.strip())

    print(f"Total number of videos: {len(urls)}")

    shouldContinue=input("Do you want to continue? (y/n): ")

    if shouldContinue != "y":
        exit()

    for i in range(len(urls)):
        Download(urls[i],i,len(urls))

    if(len(failures)>0):
        print("Failed to download the following videos:")
        for failure in failures:
            print(failure)
    else:
        print("Finished downloading all videos.")    



if __name__ == "__main__":
    DownloadVideos()

