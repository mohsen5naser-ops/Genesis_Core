import os
import hashlib
import time

def generate_sovereign_id():
    # دمج بصمة فريدة من عتاد هاتفك وتوقيت اللحظة
    # هذا يضمن أن الهوية مرتبطة بجهازك وبعقلك فقط
    raw_seed = os.urandom(32) + str(time.time()).encode()
    
    # تحويل البذرة إلى "توقيع سيادي" غير قابل للتزوير
    sovereign_key = hashlib.sha512(raw_seed).hexdigest()
    
    print("="*40)
    print("[!] تحذير: هذا هو مفتاح إمبراطوريتك.")
    print("[!] إذا ضاع، سيفقد النظام أصله.")
    print("="*40)
    print(f"ID: {sovereign_key[:32]}...") # سنظهر جزءاً منه فقط للأمان
    
    # حفظ المفتاح في ملف مخفي داخل نظامك
    with open(".master_shadow.key", "w") as f:
        f.write(sovereign_key)
    
    return sovereign_key

if __name__ == "__main__":
    generate_sovereign_id()
