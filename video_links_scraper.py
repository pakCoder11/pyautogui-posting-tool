import source_code_downloader 
import time 
import bot_functions
import pyautogui 
from bs4 import BeautifulSoup
import re


def extract_pins_links(source_code):
    """
    Extracts Instagram post and reel links from the given HTML source code.

    Args:
        source_code (str): The HTML source code to parse.

    Returns:
        list: A list of properly formatted Instagram post and reel URLs.
    """
    soup = BeautifulSoup(source_code, 'html.parser')
    pins_links = []

    # Find all anchor tags (a) with href attributes

    for link in soup.find_all('a', href=True):


        href = link['href']
        if '/reel/' in href:
            if not href.startswith('https://www.instagram.com/'):
                href = f'https://www.instagram.com{href}'


            # video_id = extract_tiktok_video_id(href)
            pins_links.append(href)
        
        else: 
            pass

    return pins_links


def save_source_code_to_file(source_code, filename):
    """
    Saves the provided source code to a text file.

    Args:
        source_code (str): The source code or text content to save.
        filename (str): The name of the output file.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            file.write(source_code)
        print(f"Source code saved to {filename} successfully!")
    except Exception as e:
        print(f"Error saving source code to {filename}: {e}")


def write_links_to_file(links, filename):
    """
    Writes a list of links to a text file, one link per line.

    Args:
        links (list): List of links (strings).
        filename (str): Name of the output text file.

    Returns:
        None
    """

    try:

        with open(filename, 'a+') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Links written to {filename} successfully!")


    except (TypeError, AttributeError, IndexError) as e:
        print(f"Error writing to {filename}: {e}")


def break_cursor():

    axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/cross.png')
    pyautogui.click(axes[0]-50,axes[1],clicks=1)
    time.sleep(1)


def extract_tiktok_video_id(url):
    """
    Extracts the TikTok video ID from a given URL.

    Args:
        url (str): TikTok video URL.

    Returns:
        str: TikTok video ID.
    """
    # Regular expression pattern to match the video ID
    pattern = r"https://www\.tiktok\.com/@[^/]+/video/(\d+)"
    
    # Search for the pattern in the URL
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
    

if __name__ == "__main__":


    limit = 50
    counter = 0

    print("Bot starts/_")
    time.sleep(7)
    source_code_downloader.open_close_inspect_element_window()

    while(True):

        source_code = source_code_downloader.copy_code_using_inspect_element()
        time.sleep(1)

        urls = extract_pins_links(source_code)

        write_links_to_file(urls,'instagram_video_links.txt')

        counter == 1 

        if counter == 1:

            break 
        
        break_cursor()

        bot_functions.press_down_keys(50) 
        time.sleep(3)
    
    source_code_downloader.open_close_inspect_element_window()

