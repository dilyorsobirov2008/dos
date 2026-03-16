# 🛒 SuperMarket Telegram Mini App

## Nima bor?
- ✅ 300 ta mahsulot (15 kategoriya)
- ✅ Tungi/Kunduzgi rejim
- ✅ Savat (cart) funksiyasi
- ✅ Admin panelga buyurtma yuborish
- ✅ Sevimlilar ro'yxati
- ✅ Buyurtmalar tarixi
- ✅ Qidiruv
- ✅ Telegram Mini App to'liq integratsiya

## Kategoriyalar
💧 Suvlar | 🍞 Non | 🥩 Go'sht | 🥛 Sut mahsulotlari
🥦 Sabzavot | 🍎 Meva | 🧴 Kimyoviy | 🧹 Tozalov
🍬 Qandolat | 🥤 Ichimliklar | 🍦 Muzqaymoq
🌾 Don/Un | 🫙 Yog'lar | 🍚 Krupa

## O'rnatish

### 1. Mini App'ni hosting'ga yuklang
`index.html` faylini quyidagi joylarga yuklash mumkin:
- **GitHub Pages** (bepul): github.com → Settings → Pages
- **Netlify** (bepul): netlify.com
- **Vercel** (bepul): vercel.com

### 2. Bot'ni o'rnating
```bash
pip install python-telegram-bot
```

### 3. `bot.py` faylida WEBAPP_URL'ni o'zgartiring
```python
WEBAPP_URL = "https://sizning-saytingiz.com/index.html"
```

### 4. Bot'ni ishga tushiring
```bash
python bot.py
```

### 5. BotFather'da Mini App'ni sozlang
1. @BotFather'ga yozing
2. `/newapp` buyrug'ini bering
3. URL: sizning hosting URL'ingiz

## Buyurtma qanday keladi?
Foydalanuvchi buyurtma berganda:
- Admin (7351189083) Telegram'ga xabar keladi
- Xabarda: mijoz ismi, ID, mahsulotlar, jami summa

## Sozlamalar
- `BOT_TOKEN` - o'zgartirilgan
- `ADMIN_ID` - o'zgartirilgan (7351189083)
- Mahsulot qo'shish: `index.html` da `allProducts` massivini tahrirlang
