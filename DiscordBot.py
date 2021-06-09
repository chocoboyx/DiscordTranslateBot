# インストールした discord.py を読み込む
import discord
import googletrans
from pprint import pprint
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODUxNjQ1MzU4NzMwOTAzNTcz.YL7SjA.eitU5BjQKOfMwCuwUMTMl12TSMY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    if client.user in message.mentions: # 話しかけられたかの判定
        translator = googletrans.Translator()
        robotName = client.user.name
        if translator.detect(message.content) == 'zh-tw':
            return
            
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        remessage = translator.translate(content, dest='zh-tw').text
        await message.reply(remessage) # 返信する非同期関数を実行

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)