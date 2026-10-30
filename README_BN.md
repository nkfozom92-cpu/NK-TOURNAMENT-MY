# NK E-SPORTS — Render Deployment

## ফাইল
- `user.html` — ইউজার ওয়েবসাইট
- `admin.html` — অ্যাডমিন প্যানেল
- `app.py` — Python Flask সার্ভার
- `requirements.txt` — Python প্যাকেজ
- `render.yaml` — Render deploy configuration

## GitHub-এ আপলোড
এই ZIP Extract করে সব ফাইল একই repository-র root folder-এ upload করুন। `user.html` এবং `admin.html`-কে অন্য folder-এ রাখবেন না।

## Render-এ Deploy
1. Render.com-এ login করুন।
2. **New + → Web Service** নির্বাচন করুন।
3. GitHub repository connect করুন।
4. Runtime: **Python** (render.yaml থাকলে সেটি auto-detect হতে পারে)।
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`
7. Deploy চাপুন।

## Website URL
- User website: `https://YOUR-SERVICE.onrender.com/`
- Admin panel: `https://YOUR-SERVICE.onrender.com/admin`
- Health check: `https://YOUR-SERVICE.onrender.com/health`

## গুরুত্বপূর্ণ Firebase নিরাপত্তা
দুই HTML ফাইলেই একই Firebase project config আছে: `nk-tournament-cff5d`। Firebase Authentication, Realtime Database এবং Security Rules Firebase Console-এ সঠিকভাবে configure করতে হবে। শুধু Python/Render server চালু হলেই Firebase Rules নিরাপদ হয়ে যায় না।

`admin.html`-এ PIN `1448` ব্রাউজারের JavaScript-এর মধ্যে রাখা আছে। এটি production-grade admin authentication নয়—যে কেউ source code দেখে PIN বের করতে পারে। Public website চালুর আগে Firebase Authentication ও server-side/custom-claim based admin authorization ব্যবহার করুন এবং Database Rules দিয়ে admin-only write access নিশ্চিত করুন। PIN পরিবর্তন করলেও এই সীমাবদ্ধতা দূর হবে না।

Render deploy সফল হওয়া মানেই Firebase login/database operation যাচাই হয়েছে—এমন নয়। Deploy-এর পরে user login, registration, match, wallet এবং admin action আলাদাভাবে পরীক্ষা করুন।
