from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#import pandas as pd

def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=r'D:\\chromedriver.exe')
    return driver

def get_videos(driver):
    driver.get("https://www.youtube.com/feed/trending")
    VIDEO_REDERER='ytd-video-renderer'
    video= driver.find_elements(By.TAG_NAME,VIDEO_REDERER)
    return video
    
def parse_videos(video):
    title= video.find_element(By.ID, 'video-title').text
    title_url=video.find_element(By.ID, 'video-title').get_attribute('href')
    thumbnail= video.find_element(By.TAG_NAME, 'img').get_attribute('src')
    channel_name= video.find_element(By.CLASS_NAME,'ytd-channel-name').text
    description= video.find_element(By.TAG_NAME,'yt-formatted-string').text
    views= video.find_element(By.CLASS_NAME,'style-scope ytd-video-meta-block').text
    return {
    'title': title,
    'title_url': title_url,
    'thumbnail': thumbnail,
    'channel_name': channel_name,
    'Description': description,
    'Views': views
    }

if __name__=="__main__":
    driver=get_driver()
    videos= get_videos(driver)
    print(f'found {len(videos)} videos')
    print('Top 10 Videos from Trending Page')
    video_data= [parse_videos(video) for video in videos[:10]]
    Create DataFrame and save file in Dataframe
    videos_df= pd.DataFrame(video_data, index=None)
    print(videos_df)
    videos_df.to_csv('Top_10.csv', index=None)



    
    
    

    
