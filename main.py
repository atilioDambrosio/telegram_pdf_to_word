# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
from pdf2docx import Converter
import os

bot = telebot.TeleBot("TOKEN")
@bot.message_handler(commands=["help", "start"])

def _send(message):
    bot.reply_to(message, "Ready para convertir")

@bot.message_handler(content_types=['document'])
def handle_docs_audio(message):
    bot.reply_to(message, "Recibido")
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    docx_file = "test.docx"
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    cv = Converter(new_file)
    cv.convert(docx_file)
    cv.close()
    bot.send_document(chat_id=message.chat.id, document=open('test.docx', 'rb'))
    bot.reply_to(message, "Documento convertido a word")
    os.remove("test.docx")
    os.remove(file_name)

bot.polling()

