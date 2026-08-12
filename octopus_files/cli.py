from pathlib import Path
import argparse


def main():
    counter=0 # عداد الملفات

# لإضافة وصف لصفحة help 
    parser = argparse.ArgumentParser(
            description="Octopus Files Tool"
        )

# لإضافة اعدادات و أوامر للأداة تشتغل على الترمينال
    parser.add_argument(
        "folder", # الأمر
        nargs="?", # تعني أن الأمر سيكون اختياري
        default=str(Path.home() / "Downloads"), # في حالة كان الأمر اختياريا سيتم اختيار مجلد التنزيلات بشكل افتراضي
        help="File counter" # وصف لوظيفة الأمر 
        )
# لرؤية الإصدار
    parser.add_argument(
        "--version", # الأمر
        action="version", # يعطي الإصدار 
        version="octopus-files 0.1.0" # يطبع إسم الاصدار
        )

    args = parser.parse_args() # قراءة أوامر المستخدم


    folder = Path(args.folder) # تحديد المسار 
    for item in folder.iterdir(): # المرور على كل عناصر الموجودة بالمجلد
        if item.is_file(): # شرط لتحقق من أن العنصر عبارة عن ملف
            counter+=1 # حساب عدد ملفات

    print(f"Files : {counter} file") # طباعة عدد ملفات

if __name__ == "__main__":
    main()
