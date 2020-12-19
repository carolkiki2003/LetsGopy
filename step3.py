# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader(download_pictures=True,download_video_thumbnails=False,download_videos=False,download_geotags=False,download_comments=False,save_metadata=False)
bot.login("jingyachen1229", "zxcvb0808")
# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'python_scripts')

def tops_posts_from_hashtag(hashtag_name: str, max_count: int):
    # Load the hashtag object into a variable
    hashtag = instaloader.Hashtag.from_name(bot.context, hashtag_name)
    # Get top posts in a generator
    posts = hashtag.get_top_posts()
    for index in range(1, max_count + 1):
        try:
            # Download the post
            bot.download_post(next(posts), target=f'{hashtag_name}_{index}')
        except:
            break # If there are any errors, we break out of the loop

            
print( tops_posts_from_hashtag(input(),5))