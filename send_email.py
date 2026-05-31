import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def build_html(news_list):
    html = "<h2>📰 今日TOP新闻</h2><ul>"
    for idx, news in enumerate(news_list, 1):
        html += (
            f"<li><strong>{idx}.</strong> "
            f"<a href='{news['link']}' target='_blank'>{news['title']}</a></li>"
        )
    html += "</ul>"
    return html

def send_email(news_list):
    sender = os.environ["MAIL_USERNAME"]
    passwd = os.environ["MAIL_PASSWORD"]
    receiver = os.environ["MAIL_USERNAME"]

    subject = "📢 每日TOP新闻"
    html_body = build_html(news_list)

    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server.login(sender, passwd)
        server.sendmail(sender, receiver, msg.as_string())
    print("✅ 邮件发送成功")

if __name__ == "__main__":
    from crawl_news import get_top_news
    news = get_top_news()
    send_email(news)
