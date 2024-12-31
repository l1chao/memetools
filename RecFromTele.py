from telegram.ext import Updater, MessageHandler, filters, CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="你好，欢迎使用我的机器人！")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def main():
    # 请将 'YOUR_TELEGRAM_BOT_TOKEN' 替换为你实际的 Bot Token
    updater = Updater(token=r'7223153864:AAEG6GfM-NtcHgS_9Aj1KxHjoxYN47C-mdI', use_context=True)
    dispatcher = updater.dispatcher

    # 处理 /start 命令
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # 处理文本消息
    echo_handler = MessageHandler(filters.text & (~filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # 开始轮询消息
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()