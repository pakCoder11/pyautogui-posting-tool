
from playwright.sync_api import sync_playwright, expect
import time
import pyautogui 
import re
import bot_functions 
import random
import os
from datetime import datetime, timedelta
import file_functions
from bs4 import BeautifulSoup


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

def break_cursor(): 

    axes = bot_functions.Locate_PNGImageOnScreen("./Screenshots/redirect.png") 
    pyautogui.click(axes[0]+5,axes[1]+50,clicks=1)
    time.sleep(5) 

def extract_tweet_text(tweet_url): 

    tweet_text = "This is a great Post ... Enjoy more and Follow Me ... Thanks"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(tweet_url)
        time.sleep(4)

        soup = BeautifulSoup(page.content(), 'html.parser')
        tweet_div = soup.find('div', attrs={'data-testid': 'tweetText'})
        tweet_text = tweet_div.get_text(strip=True) if tweet_div else None

    return tweet_text

def download_video_from_snapinsta(): 

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

    break_cursor() 
    time.sleep(30) 

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    
    remove_string_from_file('instagram_video_links.txt', random_video_link)


def download_videos_from_x(): 

    random_video_link = random.choice(read_urls_from_file('video_urls.txt'))

    bot_functions.redirect_url("https://x-downloader.com/")
    time.sleep(2) 
    break_cursor()

    bot_functions.ClickImageOnScreen("./Screenshots/X_Downloader/enter_url.png",1) 
    time.sleep(2) 

    pyautogui.write(random_video_link) 
    time.sleep(1) 
    pyautogui.press('enter') 

    time.sleep(7)
    
    bot_functions.ClickImageOnScreen("./Screenshots/X_Downloader/download.png",1)
    # bot_functions.wait_and_click_after_time("./Screenshots/X_Downloader/download.png") 
    time.sleep(2)

    pyautogui.press('esc') 
    pyautogui.press('esc')
    time.sleep(1)
    break_cursor()
    time.sleep(20) 

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    remove_string_from_file('video_urls.txt', random_video_link)
    tweet_text = extract_tweet_text(random_video_link)
    return tweet_text

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


# tweet_text = extract_tweet_text("https://x.com/x_viral_vibes/status/1963743347916607869")
# print(tweet_text)
# download_videos_from_x()