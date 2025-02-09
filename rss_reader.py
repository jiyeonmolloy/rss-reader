import feedparser
import sys

def fetch_latest_release(rss_url):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Check if feed has entries
    if feed.entries:
        # Get the latest release (first entry)
        latest_entry = feed.entries[0]
        
        # Extract the title (which usually includes the version)
        latest_version_info = latest_entry.title
        
        print(f"The latest release is: {latest_version_info}")
    else:
        print("No entries found in the feed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rss_reader.py <rss_url>")
        sys.exit(1)

    rss_url = sys.argv[1]
    fetch_latest_release(rss_url)