import bot_functions 
import pyautogui 
import time 
import os
import random
import json_loader 
from datetime import datetime, timedelta

def delete_url_from_file(target_url):

    """
    Deletes a specific URL from a text file and removes duplicate URLs.

    Args:
        file_path (str): Path to the text file containing URLs.
        target_url (str): The URL to be removed.

    Returns:
        None
    """

    file_path = json_loader.read_variable("instagram_profiles_file")

    try:


        # Read all URLs from the file
        with open(file_path, 'r') as file:
            urls = file.readlines()

        # Remove the target URL
        urls = [url.strip() for url in urls if url.strip() != target_url]

        # Remove duplicate URLs
        unique_urls = list(set(urls))

        # Write the cleaned URLs back to the file
        with open(file_path, 'w') as file:
            for url in unique_urls:
                file.write(url + '\n')

        print(f"URL '{target_url}' removed and duplicates cleaned from {file_path}.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please provide a valid file path.")

def get_random_filename(folder_path):
    try:
        # Get a list of all files in the specified folder
        files = os.listdir(folder_path)

        # Filter out directories (if any)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Choose a random filename from the list
        if files:
            random_filename = random.choice(files)
            return random_filename
        else:
            return "No files found in the folder."

    except FileNotFoundError:
        return "Folder not found. Please provide a valid folder path."


def get_recent_download_filename():
    """
    Checks the Downloads folder for files downloaded in the last 1 minute.
    
    Returns:
        str: Filename if a file was downloaded in the last minute, otherwise None
    """
    try:
        # Get the Downloads folder path
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        if not os.path.exists(downloads_path):
            print("Downloads folder not found.")
            return None
        
        # Get current time and 1 minute ago
        current_time = datetime.now()
        one_minute_ago = current_time - timedelta(minutes=5) #file within last 5 minutes ... 
        
        # Get all files in Downloads folder
        files = os.listdir(downloads_path)
        
        # Check each file's modification time
        for filename in files:
            file_path = os.path.join(downloads_path, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
                
            # Get file modification time
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Check if file was modified in the last minute
            if file_mod_time >= one_minute_ago:
                print(f"Recent download found: {filename}")
                return filename
        
        print("No recent downloads found in the last minute.")
        return None
        
    except Exception as e:
        print(f"Error checking downloads: {e}")
        return None

def select_file_from_fileOpener(destination_folder_path): 

    """
    This function is used to select the files from the file opener ... 
    """
    
    media_filename = get_recent_download_filename()
    bot_functions.please_wait('./Screenshots/FileOpener/file_1.png')

    image_axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/FileOpener/file_1.png')
    pyautogui.click(image_axes[0]-40,image_axes[1]+4,clicks=1)
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace') 
    time.sleep(1)

    pyautogui.write(destination_folder_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)


    # Step 3 Enter FileName 
    image_axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/FileOpener/filebox.png')
    pyautogui.click(image_axes[0]+50,image_axes[1]+5,clicks=1)
    time.sleep(1)

    pyautogui.write(media_filename)
    time.sleep(2) 
    pyautogui.press('down') 

    pyautogui.press('enter')
    time.sleep(1)

    # delete_file_from_downloads(media_filename)
    return media_filename

def create_hashtags_list(file_path):
    # Read hashtags from the text file (assuming one hashtag per line)
    with open(file_path, "r") as file:
        all_hashtags = [line.strip() for line in file]

    # Predefined list of additional hashtags
    additional_hashtags = [
        '#fyp', '#foryou', '#trending', '#tiktok', '#usa', '#uk', '#germany', '#trump','#motivation',
    ]

    # Randomly select hashtags from the file
    num_random_hashtags = min(len(all_hashtags), 5)  # You can adjust the number
    random_selected_hashtags = random.sample(all_hashtags, num_random_hashtags)

    # Combine the two lists
    final_hashtags = random_selected_hashtags + additional_hashtags
    return final_hashtags


def get_random_comment(file_path):

    # file_path = r"D:\Software Dev Workplace\Affiliate Marketing Bot Project\text-data\comments.txt"

    try:
        # Read all lines from the file into a list
        with open(file_path, "r", encoding='utf-8') as file:
            comments_list = file.readlines()

        # Remove any leading/trailing whitespace from each comment
        comments_list = [comment.strip() for comment in comments_list]

        # Choose a random comment from the list
        if comments_list:
            random_comment = random.choice(comments_list)
            return random_comment
        else:
            return "No comments found in the file."

    except FileNotFoundError:
        return "The file 'comments.txt' does not exist."

def get_random_sentence_from_dataset(file_path):

    """
    this function is for to access the random piece of data from a dataset.txt file ...
    """
    try:
        # Read all lines from the file into a list
        with open(file_path, "r",encoding='utf-8') as file:
            comments_list = file.readlines()

        # Remove any leading/trailing whitespace from each comment
        comments_list = [comment.strip() for comment in comments_list]

        # Choose a random comment from the list
        if comments_list:
            random_comment = random.choice(comments_list)
            return random_comment
        else:
            return "No comments found in the file."

    except FileNotFoundError:
        return "The file does not exist."


def delete_file(folder_path, filename):

    """
    Deletes a file permanently from the specified folder.

    Args:
        folder_path (str): Path to the folder containing the file.
        filename (str): Name of the file to be deleted.

    Returns:
        bool: True if the file was successfully deleted, False otherwise.
    """
    try:
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
        print(f"File '{filename}' deleted successfully.")
        return True
    except FileNotFoundError:
        print(f"File '{filename}' not found in the specified folder.")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
        return False

def compose_message():

    """
    This function is used to compose the message ... it reads the message from the file . 
    """

    health_care_description = json_loader.read_variable("health_care_description_file")

    sentence = get_random_sentence_from_dataset(health_care_description)

    string = f"** DENTAL CARE TIP OF THE DAY ** \n \n{sentence}\n \nIf you want healthy Teeths & Gums Use Pro-Dentim (LINK IN BIO) "

    return string

def delete_file_from_downloads(filename):
    """
    Deletes a specified file from the Downloads folder.
    
    Args:
        filename (str): The name of the file to delete (including extension).
        
    Returns:
        bool: True if the file was successfully deleted, False otherwise.
    """
    # Get the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_path, filename)
    
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"Error: File '{filename}' does not exist in Downloads folder.")
            return False
        
        # Attempt to delete the file
        os.remove(file_path)
        
        # Verify the file was deleted
        if not os.path.exists(file_path):
            print(f"Success: File '{filename}' was deleted from Downloads folder.")
            return True
        else:
            print(f"Error: Failed to delete '{filename}' for unknown reason.")
            return False
            
    except PermissionError:
        print(f"Error: Permission denied when trying to delete '{filename}'.")
        return False
    except OSError as e:
        print(f"Error: Failed to delete '{filename}'. {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error when deleting '{filename}': {str(e)}")
        return False

# delete_file_from_downloads("SnapInsta.to_AQOK7SC6F7moA0U1XZGUQR3ooSvhugnsUceE-RRgdVrKGL7P3fmAgALVIM-lelk_tXojQw8KrhJ83PtBDqD2Sdiub0BhlehGCaYcCBc.mp4")