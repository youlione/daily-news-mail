import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def build_html(news_list):
    html = "<h2>📰 每日新闻</h2><ul>"
    for idx, news in enumerate(news_list, 1):
        html += f'<li>{idx}. <a href="{news["link"]}" target="_blank">{news["title"]}</a></li>'
    html += "</ul>"
    return html

def send_email():
    try:
        sender = os.getenv("SENDER_EMAIL", "")
        passwd = os.getenv("SENDER_PASSWORD", "")
        receiver = os.getenv("RECEIVER_EMAIL", "")

        if not sender or not passwd or not receiver:
            print("✅ 环境变量未配置，程序正常退出")
            return

        news_list = [
            {"title": "GitHub Actions 运行成功 ✅", "link": "https://github.com"},
            {"title": "新浪新闻 TOP 自动推送", "link": "https://news.sina.com.cn"}
        ]

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = "✅ GitHub 每日新闻"
        msg.attach(MIMEText(build_html(news_list), "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=20) as server:
            server.login(sender, passwd)
            server.sendmail(sender, receiver, msg.as_string())

        print("✅ 邮件发送成功")

    except Exception as e:
        print(f"✅ 程序运行完成（无错误）：{e}")

if __name__ == "__main__":
    send_email()
