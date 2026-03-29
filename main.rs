use std::process::Command;
use std::fs;
use std::env;

fn main() {
    // جلب المفتاح من ذاكرة النظام لضمان الأمان وتجاوز حظر GitHub
    let token = env::var("GH_TOKEN").unwrap_or_else(|_| "".to_string());
    
    if token.is_empty() {
        println!("❌ خطأ: المفتاح (Token) غير موجود في ذاكرة النظام!");
        println!("استخدم أمر export قبل التشغيل.");
        return;
    }

    let repo_url = format!("https://{}@github.com/mohsen5naser-ops/Genesis_Core.git", token);

    println!(">>> الكيان يبدأ الامتصاص المعرفي الحقيقي من الشبكة...");

    // 1. استدعاء محرك البحث الحقيقي (crawler.py)
    let output = Command::new("python3")
        .args(&["crawler.py", "آخر أخبار الأمن السيبراني في سوريا 2026"])
        .output()
        .expect("فشل في تشغيل المحرك");

    let real_results = String::from_utf8_lossy(&output.stdout);

    // 2. تحديث الواجهة العالمية بالبيانات الحقيقية
    let mut html_content = fs::read_to_string("index.html").unwrap_or_default();
    
    // حقن النتائج الحقيقية في الواجهة (تأكد أن الكلمة موجودة في ملف index.html)
    if html_content.contains("Knowledge:") {
        let new_data = format!("Knowledge: {}", real_results.trim());
        // استبدال أي نص قديم بالنتائج الجديدة الحقيقية
        html_content = html_content.replace("Knowledge: Cybersecurity at 1774791924", &new_data);
    }
    
    fs::write("index.html", html_content).expect("فشل في تحديث الواجهة");

    // 3. المزامنة العالمية (رفع التطورات لـ GitHub)
    println!(">>> رفع التطورات للشبكة العالمية...");
    let _ = Command::new("git").args(&["add", "."]).status();
    let _ = Command::new("git").args(&["commit", "-m", "Entity Clean Evolution: Real Data Ingestion"]).status();
    
    let push_status = Command::new("git")
        .args(&["push", "--force", &repo_url, "main"])
        .status()
        .expect("فشل الرفع");

    if push_status.success() {
        println!("✅ DONE: الكيان تطور عالمياً والبيانات الحقيقية متاحة الآن.");
    } else {
        println!("❌ فشل الرفع: تأكد من تنظيف السجلات القديمة.");
    }
}
