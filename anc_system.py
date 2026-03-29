import os, random, time, requests
from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# --- محرك البحث والذكاء المطور ---
class OmniFabric:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    def process_query(self, query):
        raw = query.lower().strip()
        
        # تنفيذ أوامر النظام المحاكية
        if any(cmd in raw for cmd in ["scan", "fetch", "cmd"]):
            time.sleep(1)
            return f"<div style='color:#7ee787'>[SYSTEM]: تم تنفيذ البروتوكول '{query}' بنجاح عبر خيوط النسيج.</div>"
        
        try:
            # محرك البحث المباشر (DuckDuckGo API المحسن)
            url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
            r = requests.get(url, headers=self.headers, timeout=10)
            data = r.json()
            
            # استخراج الإجابة المباشرة (عواصم، تعريفات، حقائق)
            answer = data.get("AbstractText") or data.get("Definition")
            
            # إذا لم تكن هناك إجابة مباشرة، نبحث في المواضيع المرتبطة
            if not answer and data.get("RelatedTopics"):
                answer = data.get("RelatedTopics")[0].get("Text")

            if answer:
                return f"<div style='color:#00f2ff; border-bottom:1px solid #0052ec; padding-bottom:5px; margin-bottom:10px;'>[KNOWLEDGE_FOUND]:</div><p style='color:#e2e8f0; line-height:1.5;'>{answer}</p>"
            
            return f"<div style='color:#ff9e64'>[LOG]: لم يتم العثور على رد مباشر لـ '{query}'؛ جاري توسيع نطاق البحث في العقد العميقة...</div>"
            
        except Exception as e:
            return f"<div style='color:#f85149'>[ERROR]: فشل الاتصال بالنسيج العالمي. {str(e)}</div>"

fabric = OmniFabric()

# --- واجهة v32.2 الرسومية مع مؤشر التحميل ---
UI_V32_2 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ANC v32.2 | Final Sovereign</title>
    <style>
        :root { --blue: #0052ec; --cyan: #00f2ff; --bg: #020617; }
        body { background: var(--bg); color: #e2e8f0; font-family: sans-serif; margin: 0; display: flex; height: 100vh; overflow: hidden; }
        
        #sidebar { width: 220px; background: #0b1120; border-left: 2px solid var(--blue); padding: 20px; flex-shrink: 0; }
        .stat-val { font-size: 22px; color: var(--cyan); font-family: monospace; text-shadow: 0 0 10px var(--cyan); }
        
        #display { flex: 1; padding: 20px; overflow-y: auto; padding-bottom: 150px; scroll-behavior: smooth; }
        .msg { background: rgba(15, 23, 42, 0.9); border-right: 4px solid var(--blue); padding: 15px; margin-bottom: 15px; border-radius: 5px; animation: slideUp 0.3s ease; }
        
        /* مؤشر التحميل */
        #loader { display: none; margin: 10px; color: var(--cyan); font-size: 13px; font-family: monospace; }
        .dot { animation: blink 1s infinite; }
        @keyframes blink { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }

        /* شريط البحث العائم المطور */
        #search-float { 
            position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
            width: 90%; max-width: 500px; background: #0f172a; border: 2px solid var(--blue);
            padding: 8px; border-radius: 50px; display: flex; gap: 10px;
            box-shadow: 0 0 25px rgba(0, 82, 236, 0.5); z-index: 999;
        }

        input { flex: 1; background: transparent; border: none; color: var(--cyan); padding: 10px 20px; outline: none; font-size: 16px; }
        button { background: var(--blue); color: white; border: none; padding: 10px 25px; border-radius: 50px; cursor: pointer; font-weight: bold; }
        
        @keyframes slideUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div id="sidebar">
        <div style="margin-bottom:20px">
            <div style="font-size:10px; color:#94a3b8;">خيوط النسيج</div>
            <div class="stat-val" id="s-val">14375</div>
        </div>
        <div style="margin-bottom:20px">
            <div style="font-size:10px; color:#94a3b8;">السرعة الحالية</div>
            <div class="stat-val" id="f-val" style="font-size:18px;">2.98 GB/s</div>
        </div>
    </div>

    <div id="display">
        <div class="msg"><b>[SYSTEM]:</b> النواة v32.2 جاهزة. تم إصلاح محرك الإجابات وتفعيل مؤشر المعالجة.</div>
        <div id="loader">جاري جلب البيانات من النسيج العصبي<span class="dot">...</span></div>
    </div>

    <div id="search-float">
        <input type="text" id="q" placeholder="اسأل عن أي شيء (مثلاً: عاصمة كوريا)..." onkeypress="if(event.key==='Enter') send()">
        <button onclick="send()">نهش</button>
    </div>

    <script>
        async function send() {
            const i = document.getElementById('q');
            const d = document.getElementById('display');
            const loader = document.getElementById('loader');
            if(!i.value) return;
            
            const val = i.value;
            d.innerHTML += `<div style='color:#94a3b8; margin:10px; font-size:14px;'>Master: ${val}</div>`;
            i.value = '';
            loader.style.display = 'block';
            d.scrollTop = d.scrollHeight;

            try {
                const r = await fetch(`/api/query?q=${encodeURIComponent(val)}`);
                const data = await r.json();
                loader.style.display = 'none';
                d.innerHTML += `<div class="msg"><b>ANC:</b><br>${data.result}</div>`;
            } catch(e) {
                loader.style.display = 'none';
                d.innerHTML += `<div class="msg" style="border-color:red;">خطأ في الاتصال.</div>`;
            }
            d.scrollTop = d.scrollHeight;
        }

        setInterval(() => {
            document.getElementById('s-val').innerText = 14300 + Math.floor(Math.random()*200);
            document.getElementById('f-val').innerText = (2.5 + Math.random()).toFixed(2) + " GB/s";
        }, 2500);
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(UI_V32_2)

@app.route('/api/query')
def query():
    q = request.args.get('q', '')
    return jsonify(result=fabric.process_query(q))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
