#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext

from user_setting import UserSetting
from utils import send_async
from shared_vars import dispatcher
from internationalization import _, user_locale

@user_locale
def help_handler(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    help_text = _("Ikuti langkah ini ya kontol:\n\n"
      "1. Tambahin bot ini ke grup lo\n"
      "2. Di grup, mulailah permainan baru dengan /new atau bergabung sudah"
      " menjalankan permainan dengan /join\n"
      "3. Setelah setidaknya dua pemain bergabung, mulailah permainan dengan"
      " /start\n"
      "4. Jenis <code>@reyunobot</code> ke dalam kotak obrolan Anda dan tekan "
      "<b>spasi</b>, atau klik <code>melalui @reyunobot</code> teks "
      "di samping pesan. Anda akan melihat kartu Anda (beberapa berwarna abu-abu), "
      "opsi tambahan apa pun seperti menggambar, dan <b>?</b> untuk melihat "
      "keadaan game saat ini. <b>Kartu berwarna abu-abu</b> adalah milik Anda "
      "<b>tidak dapat diputar</b> saat ini. Ketuk opsi untuk mengeksekusi "
      "tindakan yang dipilih.\n"
      "Pemain dapat bergabung dalam game kapan saja. Untuk keluar dari game, "
      "menggunakan /leave. Jika seorang pemain membutuhkan waktu lebih dari 90 detik untuk bermain, "
      "Kamu dapat memakai /skip untuk melewati pemain itu. Menggunakan /notify_me ke "
      "menerima pesan pribadi saat permainan baru dimulai.\n\n"
      "<b>Bahasa</b> dan setelan lainnya: /settings\n"
      "Perintah lain (hanya pembuat game):\n"
      "/close - Tutup lobi\n"
      "/open - Buka lobi\n"
      "/kill - Hentikan permainan\n"
      "/kick - Pilih pemain untuk ditendang "
      "dengan membalasnya\n"
      "/enable_translations - Terjemahkan teks yang relevan ke semua "
      "bahasa yang digunakan dalam permainan\n"
      "/disable_translations - Gunakan bahasa Inggris untuk teks tersebut\n\n"
      "<b>Eksperimental:</b> Mainkan dalam beberapa grup secara bersamaan. "
      "Tekan <code>Game saat ini: ...</code> dan pilih tombol "
      "grup tempat Anda ingin bermain kartu.\n"
      "Jika Anda menikmati bot ini, "
      "<a href=\"https://telegram.me/storebot?start=ReyUnoBot\">"
      "menilai saya</a>, bergabung dengan "
      "<a href=\"https://telegram.me/ReyUpdatesCH\">Updates Channel</a>"
      "<a href=\"https://telegram.me/xyreynld\">Owner Repo</a>.")

    send_async(context.bot, update.message.chat_id, text=help_text,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@user_locale
def modes(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    modes_explanation = _("Rey-UnoBot ini memiliki empat mode permainan: Klasik, Sanik, Liar, dan Teks.\n\n"
      " ✦ Mode Klasik menggunakan dek UNO konvensional dan tidak ada lompatan otomatis.\n"
      " ✦ Mode Sanic menggunakan dek UNO konvensional dan bot secara otomatis melompati pemain jika dia terlalu lama memainkan gilirannya.\n"
      " ✦ Mode Liar menggunakan dek dengan lebih banyak kartu spesial, lebih sedikit variasi angka, dan tidak ada loncatan otomatis.\n"
      " ✦ Mode Teks menggunakan dek UNO konvensional tetapi alih-alih stiker, ia menggunakan teks.\n\n"
      "Untuk mengubah mode permainan, GAME CREATOR harus mengetik bot nickname dan spasi, "
      "sama seperti saat memainkan kartu, dan semua opsi gamemode akan muncul.")
    send_async(context.bot, update.message.chat_id, text=modes_explanation,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@user_locale
def source(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    source_text = _("Bot ini adalah Perangkat Lunak Bebas dan dilisensikan di bawah AGPL. "
      "Owner Repo: \n"
      "https://telegram.me/xyreynld"
      "Source Code: \n"
      "https://github.com/reyn0pe/Rey-UnoBot")
    attributions = _("Atribusi:\n"
      'Draw ikon oleh '
      '<a href="http://www.faithtoken.com/">Faithtoken</a>\n'
      'Pass ikon oleh '
      '<a href="http://delapouite.com/">Delapouite</a>\n'
      "Asli tersedia di http://game-icons.net\n"
      "Ikon diedit oleh ɳick")

    send_async(context.bot, update.message.chat_id, text=source_text + '\n' +
                                                 attributions,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@user_locale
def news(update: Update, context: CallbackContext):
    """Handler for the /news command"""
    send_async(context.bot, update.message.chat_id,
               text=_("Semua berita di sini: https://telegram.me/ReyUpdatesCH"),
               disable_web_page_preview=True)


@user_locale
def stats(update: Update, context: CallbackContext):
    user = update.message.from_user
    us = UserSetting.get(id=user.id)
    if not us or not us.stats:
        send_async(context.bot, update.message.chat_id,
                   text=_("Anda tidak mengaktifkan statistik. Menggunakan /settings di "
                          "obrolan pribadi dengan bot untuk mengaktifkannya."))
    else:
        stats_text = list()

        n = us.games_played
        stats_text.append(
            _("{number} permainan dimainkan",
              "{number} permainan dimainkan",
              n).format(number=n)
        )

        n = us.first_places
        m = round((us.first_places / us.games_played) * 100) if us.games_played else 0
        stats_text.append(
            _("{number} tempat pertama ({percent}%)",
              "{number} tempat pertama ({percent}%)",
              n).format(number=n, percent=m)
        )

        n = us.cards_played
        stats_text.append(
            _("{number} kartu dimainkan",
              "{number} kartu dimainkan",
              n).format(number=n)
        )

        send_async(context.bot, update.message.chat_id,
                   text='\n'.join(stats_text))


def register():
    dispatcher.add_handler(CommandHandler('help', help_handler))
    dispatcher.add_handler(CommandHandler('source', source))
    dispatcher.add_handler(CommandHandler('news', news))
    dispatcher.add_handler(CommandHandler('stats', stats))
    dispatcher.add_handler(CommandHandler('modes', modes))
