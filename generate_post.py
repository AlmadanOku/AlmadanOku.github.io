import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Girişimcilik ve yapay zeka hakkında bilgilendirici, özgün, SEO uyumlu bir blog yazısı yaz."

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Sen profesyonel bir blog yazarı ve içerik uzmanısın."},
        {"role": "user", "content": prompt}
    ]
)

blog_content = response['choices'][0]['message']['content']

# Dosya adı
today = datetime.today().strftime('%Y-%m-%d')
filename = f"_posts/{today}-ai-blog.md"

os.makedirs("_posts", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\ntitle: Otomatik AI Blog\ndate: {today}\n---\n\n")
    f.write(blog_content)