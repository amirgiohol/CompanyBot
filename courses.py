# data.py

courses = {
    "Python": [
        {"id": 1, "name": "Python مبتدی", "price": 50, "description": "شروع یادگیری Python از صفر"},
        {"id": 2, "name": "Python متوسط", "price": 70, "description": "ساخت پروژه‌های عملی با Python"},
        {"id": 3, "name": "Python پیشرفته", "price": 100, "description": "پروژه‌های حرفه‌ای و Data Science"},
        {"id": 4, "name": "Django", "price": 90, "description": "ساخت وب‌اپلیکیشن با فریمورک Django"},
        {"id": 5, "name": "Flask", "price": 85, "description": "ساخت وب‌اپلیکیشن سبک با Flask"}
    ],
    "JavaScript": [
        {"id": 6, "name": "Frontend با JS", "price": 60, "description": "HTML, CSS, DOM و پروژه عملی"},
        {"id": 7, "name": "Node.js Backend", "price": 80, "description": "ساخت سرور و API با Node.js"},
        {"id": 8, "name": "React.js", "price": 90, "description": "ساخت رابط کاربری مدرن با React"},
        {"id": 9, "name": "Vue.js", "price": 85, "description": "ساخت رابط کاربری با Vue.js"},
        {"id": 10, "name": "Angular", "price": 95, "description": "فریمورک حرفه‌ای Frontend با Angular"}
    ],
    "Java": [
        {"id": 11, "name": "Java Core", "price": 55, "description": "مبانی Java و OOP"},
        {"id": 12, "name": "Spring Framework", "price": 90, "description": "وب‌اپلیکیشن حرفه‌ای با Spring"},
        {"id": 13, "name": "Java Advanced", "price": 100, "description": "Java پیشرفته و طراحی معماری نرم‌افزار"}
    ],
    "C#": [
        {"id": 14, "name": "C# Desktop", "price": 60, "description": "ساخت اپلیکیشن ویندوزی"},
        {"id": 15, "name": "ASP.NET Core", "price": 85, "description": "ساخت وب‌اپلیکیشن حرفه‌ای با ASP.NET Core"},
        {"id": 16, "name": "Unity Game Dev", "price": 95, "description": "ساخت بازی با Unity و C#"}
    ],
    "Mobile": [
        {"id": 17, "name": "Android", "price": 70, "description": "ساخت اپلیکیشن اندروید"},
        {"id": 18, "name": "iOS (Swift)", "price": 90, "description": "ساخت اپلیکیشن iOS با Swift"},
        {"id": 19, "name": "Flutter", "price": 100, "description": "ساخت اپلیکیشن چند سکویی با Flutter"},
        {"id": 20, "name": "React Native", "price": 95, "description": "ساخت اپلیکیشن موبایل Cross-platform"}
    ],
    "Web Development": [
        {"id": 21, "name": "HTML و CSS", "price": 40, "description": "ساخت صفحات وب ساده"},
        {"id": 22, "name": "Bootstrap", "price": 50, "description": "ساخت وب‌سایت ریسپانسیو با Bootstrap"},
        {"id": 23, "name": "Tailwind CSS", "price": 55, "description": "ساخت وب‌اپلیکیشن مدرن با Tailwind"}
    ],
    "Data Science & AI": [
        {"id": 24, "name": "Pandas & Numpy", "price": 60, "description": "تحلیل داده با Pandas و Numpy"},
        {"id": 25, "name": "Machine Learning", "price": 100, "description": "آموزش یادگیری ماشین و الگوریتم‌ها"},
        {"id": 26, "name": "Deep Learning", "price": 120, "description": "شبکه‌های عصبی و یادگیری عمیق با Python"},
        {"id": 27, "name": "Data Visualization", "price": 70, "description": "نمایش داده‌ها با Matplotlib و Seaborn"}
    ],
    "DevOps & Cloud": [
        {"id": 28, "name": "Docker", "price": 80, "description": "مدیریت کانتینرها و محیط توسعه"},
        {"id": 29, "name": "Kubernetes", "price": 120, "description": "استقرار برنامه‌های کانتینری در مقیاس بزرگ"},
        {"id": 30, "name": "AWS", "price": 130, "description": "خدمات ابری و استقرار پروژه‌ها روی AWS"},
        {"id": 31, "name": "CI/CD", "price": 90, "description": "یکپارچه‌سازی و تحویل مداوم پروژه‌ها"}
    ]
}

admins = {
    123456789: "ادمین اصلی"
}
