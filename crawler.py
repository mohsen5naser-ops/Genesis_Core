import requests
from bs4 import BeautifulSoup
import sys
import os

def fetch_real_data(query):
    # محرك بحث مستقل (يستخدم DuckDuckGo لتجنب الحظر والحفاظ على السيادة)
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # استخراج النتائج الحقيقية (العناوين والملخصات)
        results = soup.find_all('a', class_='result__a', limit=3)
        
        if not results:
            return "لم يتم العثور على بيانات جديدة في الشبكة حالياً."

        knowledge_block = ""
        for res in results:
            knowledge_block += f"| المصدر: {res.get_text()} | الرابط: {res['href']}\n"
        
        # تخزين في الأرشيف الأبدي
        with open("universal_knowledge.db", "a", encoding="utf-8") as db:
            db.write(f"\n[QUERY: {query}]\n{knowledge_block}")
            
        return knowledge_block
    except Exception as e:
        return f"خطأ في الاتصال بالشبكة: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(fetch_real_data(query))
