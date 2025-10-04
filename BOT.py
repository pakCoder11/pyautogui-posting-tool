from playwright.sync_api import sync_playwright, expect
import time
import pyautogui 
import re
import bot_functions 
import random
import os
from datetime import datetime, timedelta 
import video_downloader
from bs4 import BeautifulSoup

import file_functions

def remove_string_from_file(file_path, target_string):
    try:
        # Read the entire content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove the target string (if it exists) from the list of lines
        updated_lines = [line for line in lines if target_string not in line]

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"Removed occurrences of '{target_string}' from {file_path}.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        


def read_urls_from_file(file_path):
    """
    Returns:
        list: List of strings read from the file.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            # Remove newline characters from each line
            cleaned_lines = [line.strip() for line in lines]
            return cleaned_lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []



def delete_video_link(target_url):
    """
    Deletes a specific Instagram reel URL from instagram_video_links.txt.
    
    Args:
        target_url (str): The Instagram reel URL to be removed.
        
    Returns:
        bool: True if the URL was found and deleted, False if not found or error occurred.
    """
    file_path = "instagram_video_links.txt"
    
    # Basic URL validation
    if not target_url.startswith("https://www.instagram.com/") or "/reel/" not in target_url:
        print(f"Invalid Instagram reel URL: {target_url}")
        return False
        
    try:
        # Read all URLs from the file
        with open(file_path, 'r') as file:
            urls = file.readlines()
            
        # Clean URLs and check if target exists
        cleaned_urls = [url.strip() for url in urls]
        if target_url not in cleaned_urls:
            print(f"URL not found: {target_url}")
            return False
            
        # Remove the target URL while preserving order
        updated_urls = [url for url in urls if url.strip() != target_url]
        
        # Write the updated URLs back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_urls)
            
        print(f"Successfully deleted URL: {target_url}")
        return True
        
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the URL: {e}")
        return False


def break_cursor(): 

    axes = bot_functions.Locate_PNGImageOnScreen("./Screenshots/redirect.png") 
    print(f"The axes is {axes}")
    pyautogui.click(axes[0]+5,axes[1]+50,clicks=1)
    time.sleep(5)  


def download_video(): 

    video_links = read_urls_from_file('instagram_video_links.txt') 
    random_video_link = random.choice(video_links)
    # bot_functions.redirect_url(generate_video_redirect_url(random_video_link))
    bot_functions.redirect_url("https://snapinsta.to/en")
    time.sleep(3) 
    break_cursor()
    bot_functions.ClickImageOnScreen("./Screenshots/enter_url.png",1) 
    time.sleep(3) 
    pyautogui.write(random_video_link)
    time.sleep(4) 
    pyautogui.press('enter') 

    bot_functions.please_wait("./Screenshots/close.png")
    time.sleep(1)

    break_cursor()

    bot_functions.press_down_keys(5)

    bot_functions.ClickImageOnScreen("./Screenshots/download.png",3) 
    time.sleep(3) 
    
    # delete_video_link(random_video_link)

def auto_start_google_chrome(): 

    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write("chrome")
    time.sleep(3)
    pyautogui.press('enter') 
    time.sleep(4)



def upload_to_X(): 


    bot_functions.redirect_url("https://www.x.com/home") 

    time.sleep(3)

    bot_functions.please_wait("./Screenshots/big_post.png")
    time.sleep(4)

    bot_functions.ClickImageOnScreen("./Screenshots/big_post.png",1) 
    time.sleep(3) 

    bot_functions.ClickImageOnScreen("./Screenshots/media_x.png",1) 
    time.sleep(3)

    download_filename = file_functions.select_file_from_fileOpener(destination_folder_path="This PC/Downloads")
    time.sleep(20)
    bot_functions.ClickImageOnScreen("./Screenshots/small_post.png",1)
    time.sleep(45)
    file_functions.delete_file_from_downloads(download_filename)


def post_comment_on_X(): 

    """
    This function is used to post a comment on a X post
    """

    X_profiles = ["https://x.com/elonmusk","https://x.com/realDonaldTrump","https://x.com/TuckerCarlson","https://x.com/nvidia","https://x.com/Tesla"]

    bot_functions.redirect_url(random.choice(X_profiles))
    time.sleep(8) 
    bot_functions.press_down_keys(30)


    while(True): 

        if bot_functions.LocateImageOnScreen("./Screenshots/comment_btn.png") == True: 

            bot_functions.ClickImageOnScreen("./Screenshots/comment_btn.png",1) 
            time.sleep(3)
            if bot_functions.LocateImageOnScreen("./Screenshots/draft.png") == True:  
                pyautogui.write(file_functions.get_random_comment("./text-data/comments.txt"))

                time.sleep(2)
                bot_functions.ClickImageOnScreen("./Screenshots/post_reply.png",1) 
                time.sleep(3)
                break
        
        time.sleep(2)
        bot_functions.press_down_keys(10)

    time.sleep(15)

def upload_to_linkedin(): 

    """
    This function is used to upload the video on a LinkedIn
    """

    bot_functions.redirect_url("https://www.linkedin.com/feed/")
    time.sleep(3) 

    bot_functions.ClickImageOnScreen("./Screenshots/start_post.png",1) 
    time.sleep(3) 

    bot_functions.ClickImageOnScreen("./Screenshots/media.png",1) 
    time.sleep(3) 

    download_filename = file_functions.select_file_from_fileOpener(destination_folder_path="This PC/Downloads")

    bot_functions.ClickImageOnScreen("./Screenshots/next.png",1) 
    time.sleep(3) 

    bot_functions.ClickImageOnScreen("./Screenshots/post.png",1) 
    time.sleep(45)

def post_comment_on_linkedin():  

    linkedin_profiles = ["https://www.linkedin.com/in/linasbeliunas/recent-activity/all/","https://www.linkedin.com/in/neilkpatel/recent-activity/all/","https://www.linkedin.com/in/williamhgates/recent-activity/all/","https://www.linkedin.com/in/satyanadella/recent-activity/all/"]

    bot_functions.redirect_url(random.choice(linkedin_profiles))
    time.sleep(8) 

    bot_functions.scroll_down_until_image_found("./Screenshots/LinkedIn/comment.png") 
    time.sleep(3)
    
    bot_functions.ClickImageOnScreen("./Screenshots/LinkedIn/like.png",1)
    time.sleep(2) 

    bot_functions.ClickImageOnScreen("./Screenshots/LinkedIn/comment.png",1)
    time.sleep(3) 

    pyautogui.write(file_functions.get_random_comment("./text-data/comments.txt"))
    time.sleep(2)
    bot_functions.ClickImageOnScreen("./Screenshots/LinkedIn/blue_comment.png",1)

    time.sleep(10)

def upload_quote_to_asani(): 

    """
    This function is used to upload the data on Asani.pk
    """

    bot_functions.redirect_url("https://asani.pk/")
    time.sleep(1)

    bot_functions.please_wait("./Screenshots/Asani_pk/awaz.png") 
    time.sleep(1)

    bot_functions.ClickImageOnScreen("./Screenshots/Asani_pk/awaz.png",1) 
    time.sleep(3) 

    pyautogui.write(file_functions.get_random_comment("./text-data/comments.txt"))
    time.sleep(2)
    bot_functions.ClickImageOnScreen("./Screenshots/Asani_pk/awaz_btn_text.png",1) 
    time.sleep(10) 

# -------------------------------------------------------------------

# def extract_tweet_text(tweet_url):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         page.goto(tweet_url)
#         time.sleep(4)

#         soup = BeautifulSoup(page.content(), 'html.parser')
#         tweet_div = soup.find('div', attrs={'data-testid': 'tweetText'})
#         tweet_text = tweet_div.get_text(strip=True) if tweet_div else None

#     return tweet_text

def upload_video_to_fanvue(video_text): 

    """
    This function is used to upload the video on Fanvue
    """

    # video_text = video_downloader.download_videos_from_x()
    # print("Function start")

    bot_functions.redirect_url("https://www.fanvue.com/create") 
    time.sleep(7)

    bot_functions.ClickImageOnScreen("./Screenshots/Fanvue/subscriber.png",1)  
    time.sleep(3)
    bot_functions.press_down_keys(1)
    time.sleep(1) 

    pyautogui.press('enter')
    time.sleep(2)

    bot_functions.ClickImageOnScreen("./Screenshots/Fanvue/upload.png",1)  
    time.sleep(5) 

    media_filename = file_functions.select_file_from_fileOpener(destination_folder_path="This PC/Downloads")
    time.sleep(2)

    bot_functions.ClickImageOnScreen("./Screenshots/Fanvue/caption.png",1)  
    time.sleep(2)
    pyautogui.write(video_text)
    time.sleep(45)
    bot_functions.ClickImageOnScreen("./Screenshots/Fanvue/create.png",1)  
    time.sleep(4) 
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    return video_text


def upload_post_to_instagram(string): 

    # media_path = './Screenshots/Instagram/'
    instagram_media_folder_path = r"This PC\Downloads" 

    """
    This function is used to post the content on instagram 
    """

    bot_functions.redirect_url("https://www.instagram.com/")
    time.sleep(3)

    bot_functions.please_wait('./Screenshots/Instagram/create.png')
    time.sleep(1)
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/create.png',1)
    time.sleep(1)

    if bot_functions.please_wait_for_n_seconds("./Screenshots/Instagram/post.png",3): 

        bot_functions.ClickImageOnScreen("./Screenshots/Instagram/post.png",1)
        time.sleep(1)

    bot_functions.please_wait('./Screenshots/Instagram/select_from_pc.png')
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/select_from_pc.png',1)
    time.sleep(1)

    media_filename = file_functions.select_file_from_fileOpener(instagram_media_folder_path)
    time.sleep(1)

    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/next.png',1)
    time.sleep(2)
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/next.png',1)
    time.sleep(2)

    
    axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/Instagram/smiley.png')
    pyautogui.click(axes[0],axes[1]-100,clicks=1)

    time.sleep(1)

    # string = generate_insta_post_description()

    pyautogui.write(string)
    time.sleep(2)
    pyautogui.press('space')
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/share.png',1)
    time.sleep(2)

    status_ = bot_functions.please_wait_for_n_seconds("./Screenshots/Instagram/post_shared_status.PNG",100)

    if status_ == True:

        file_functions.delete_file(instagram_media_folder_path,media_filename)
        pyautogui.press('esc')
        time.sleep(1)
    
    file_functions.delete_file_from_downloads(media_filename) 
    print("File deleted from downloads folder")

if __name__ == "__main__":

    """
    This is a facebook page scraping tool , it's a module a part of a big mega gui based application ... 
    """

    auto_start_google_chrome()
    time.sleep(3) 
    video_downloader.download_video_from_snapinsta() 

    time.sleep(3)
    upload_to_linkedin()
    post_comment_on_linkedin()
    upload_to_X()
    post_comment_on_X()

    upload_quote_to_asani()
    video_text = video_downloader.download_videos_from_x()
    video_text = upload_video_to_fanvue(video_text) 
    upload_post_to_instagram(video_text)

    time.sleep(3) #ending sleep time
    pyautogui.hotkey('ctrl', 'w') #close the browser ... 



