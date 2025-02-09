import feedparser
import sys

def fetch_latest_release(rss_url, keyword="release", num_entries=5):
    feed = feedparser.parse(rss_url)

    # Check if feed has entries
    if feed.entries:
        # Get the latest entries (up to num_entries)
        latest_entries = feed.entries[:num_entries]
        
        for i, entry in enumerate(latest_entries, start=1):
            feed_info = entry.title
            print(f"{i}. The latest {keyword} is: {feed_info}")
    else:
        print("No entries found in the feed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rss_reader.py <rss_url> <keyword>")
        sys.exit(1)

    rss_url = sys.argv[1]
    keyword = sys.argv[2]
    fetch_latest_release(rss_url, keyword)