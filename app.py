from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# مصادر الأخبار القانونية
FEEDS = {
    "أخبار الأمم المتحدة": "https://news.un.org/feed/subscribe/ar/news/all/rss.xml"
}

@app.route('/')
def home():
    articles = []
    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]: # سحب أحدث 5 مواضيع
                articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'source': source
                })
        except:
            pass
            
    # هنا نطلب من بايثون عرض ملف التصميم وتمرير الأخبار إليه
    return render_template('index.html', articles=articles)

