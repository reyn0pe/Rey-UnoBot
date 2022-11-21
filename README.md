<p align="center">
  <img src="https://telegra.ph/file/ddfd89c5d0775acbb3bdb.jpg">
<h2 align="center">

# Rey-UnoBot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)

Bot Telegram yang memungkinkan Anda memainkan permainan kartu populer UNO melalui kueri sebaris. Bot saat ini berjalan sebagai [@ReyUnoBot](http://telegram.me/reyunobot).

Untuk menjalankan bot sendiri, Anda memerlukan: 
- Python (tested with 3.4+)
- The [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) module
- [Pony ORM](https://ponyorm.com/)

## Mempersiapkan
- Dapatkan token bot dari [@BotFather](http://telegram.me/BotFather) dan ubah konfigurasi di `config.json`.
- Konversikan semua file bahasa dari `.po` file ke `.mo` dengan mengeksekusi skrip bash `compile.sh` terletak di `locales` map.
  Pilihan lain adalah: `find . -maxdepth 2 -type d -name 'LC_MESSAGES' -exec bash -c 'msgfmt {}/unobot.po -o {}/unobot.mo' \;`.
- Menggunakan `/setinline` dan `/setinlinefeedback` dengan BotFather untuk bot Anda.
- Menggunakan `/setcommands` dan kirimkan daftar perintah di commandlist.txt
- Install requirements (menggunakan sebuah `virtualenv` direkomendasikan): `pip install -r requirements.txt`

Anda dapat mengubah beberapa parameter gameplay seperti waktu giliran, jumlah minimum pemain, dan mode game default `config.json`.
Mode permainan saat ini tersedia: klasik, cepat, dan liar. Periksa detailnya dengan `/modes` command.

Kemudian jalankan bot dengan `python3 bot.py`.

Dokumentasi kode sangat minim tetapi ada.
