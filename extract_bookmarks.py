#!/usr/bin/env python3
"""
Extract tweet text from Twitter bookmark JSON files
Creates clean training data from your bookmarked tweets
"""

import json
import re
from pathlib import Path

def clean_tweet_text(text):
    """Clean tweet text for training"""
    if not text:
        return None

    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'pic\.x\.com/\S+', '', text)

    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove excessive spaces
    text = re.sub(r' {2,}', ' ', text)

    # Remove promotional patterns
    promotional_patterns = [
        r'Like\+.*?Comment.*?Repost',
        r'Follow me for.*?DM',
        r'Link in bio',
        r'Check out my.*?newsletter',
    ]
    for pattern in promotional_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Strip and check length
    text = text.strip()

    # Filter out low-quality tweets
    if len(text) < 50:  # Too short
        return None
    if len(text) > 2000:  # Too long (probably spam)
        return None
    if text.count('🚨') > 2:  # Too many alerts = spam
        return None

    return text

def extract_tweets(json_file):
    """Extract all tweets from a bookmark JSON file"""
    print(f"\n📖 Reading {json_file.name}...")

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        tweets = []
        skipped = 0

        for item in data:
            # Try note_tweet_text first (complete text), fallback to full_text
            text = item.get('note_tweet_text') or item.get('full_text')

            cleaned = clean_tweet_text(text)
            if cleaned:
                tweets.append({
                    'text': cleaned,
                    'author': item.get('screen_name', 'unknown'),
                    'date': item.get('tweeted_at', ''),
                })
            else:
                skipped += 1

        print(f"✅ Extracted {len(tweets)} tweets")
        print(f"⏭️  Skipped {skipped} (too short/promotional/spam)")

        return tweets

    except Exception as e:
        print(f"❌ Error reading {json_file}: {e}")
        return []

def save_training_data(tweets, output_file):
    """Save tweets in training format"""
    print(f"\n💾 Saving to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        for tweet in tweets:
            f.write(tweet['text'])
            f.write('\n\n---\n\n')

    # Calculate stats
    total_words = sum(len(t['text'].split()) for t in tweets)
    total_chars = sum(len(t['text']) for t in tweets)

    print(f"✅ Saved {len(tweets)} tweets")
    print(f"📊 Stats:")
    print(f"   - Total words: {total_words:,}")
    print(f"   - Total chars: {total_chars:,}")
    print(f"   - Avg words/tweet: {total_words // len(tweets)}")

def main():
    print("🐦 Twitter Bookmark → Training Data Extractor")
    print("=" * 50)

    # Input files
    bookmark_files = [
        Path('/Users/ohm./Downloads/bookmark .json'),
        Path('/Users/ohm./Downloads/div bookmark.json'),
    ]

    # Check files exist
    for f in bookmark_files:
        if not f.exists():
            print(f"❌ File not found: {f}")
            return

    # Extract all tweets
    all_tweets = []
    for file in bookmark_files:
        tweets = extract_tweets(file)
        all_tweets.extend(tweets)

    if not all_tweets:
        print("\n❌ No tweets extracted!")
        return

    # Remove duplicates (same text)
    print(f"\n🔍 Removing duplicates...")
    unique_tweets = []
    seen_texts = set()

    for tweet in all_tweets:
        text_lower = tweet['text'].lower()
        if text_lower not in seen_texts:
            unique_tweets.append(tweet)
            seen_texts.add(text_lower)

    duplicates = len(all_tweets) - len(unique_tweets)
    print(f"   Removed {duplicates} duplicates")

    # Sort by date (newest first)
    unique_tweets.sort(key=lambda t: t['date'], reverse=True)

    # Save to training data
    output_dir = Path('/Users/ohm./Desktop/twitter-ai-project/data')
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / 'bookmarks-training.txt'
    save_training_data(unique_tweets, output_file)

    # Also save top authors stats
    from collections import Counter
    authors = Counter(t['author'] for t in unique_tweets)

    print(f"\n👥 Top 10 Authors in Your Bookmarks:")
    for author, count in authors.most_common(10):
        print(f"   @{author}: {count} tweets")

    print(f"\n✅ DONE!")
    print(f"\n📁 Training data saved to:")
    print(f"   {output_file}")
    print(f"\n🚀 Next steps:")
    print(f"   1. Review the data: cat {output_file} | head -100")
    print(f"   2. Copy to autoresearch: cp {output_file} autoresearch-macos/data/train.txt")
    print(f"   3. Run prepare: cd autoresearch-macos && uv run prepare.py")
    print(f"   4. Start training with Claude Code!")

if __name__ == '__main__':
    main()
