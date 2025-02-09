import feedparser
import requests
import sys
import os

def fetch_latest_release(rss_url, keyword="release", num_entries=5):
    feed = feedparser.parse(rss_url)

    # Check if feed has entries
    if feed.entries:
        # Get the latest entries (up to num_entries)
        latest_entries = feed.entries[:num_entries]
        
        # Accumulate feed information
        feed_infos = []
        for i, entry in enumerate(latest_entries, start=1):
            feed_info = entry.title
            feed_infos.append(f"{i}. {feed_info}")
        
        # Create the message
        message = f"The latest {keyword}s are:\n" + "\n".join(feed_infos)
        print(message)
        
        # Send the message to Discord
        send_to_discord(message)
    else:
        print("No entries found in the feed.")

def send_to_discord(message):
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    if not webhook_url:
        print("Discord webhook URL not found in environment variables.")
        return
    
    payload = {
        "content": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204 or response.status_code == 200:
        print("Message sent successfully to Discord! Woohoo!")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rss_reader.py <rss_url> <keyword>")
        sys.exit(1)

    rss_url = sys.argv[1]
    keyword = sys.argv[2]
    fetch_latest_release(rss_url, keyword)