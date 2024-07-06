# -*- coding: utf-8 -*-

#chatgpt API, youtube API
#openai.api_key = :)
#youtube.api_key = :)

from openai import OpenAI
from googleapiclient.discovery import build

client = OpenAI(
    api_key= :)
)

#talk with user for 3 times (total 6 sentences)
i = 2
messages = []
messages.append({"role": "system", "content": "You are a teaching assistant."})
messages.append({"role": "system", "content": "You have to define single category of today's lecture in Korean."})
messages.append({"role": "system", "content": "Talk with students to get hint about what they learned today."})
messages.append({"role": "system", "content": "Use Korean."})

bot_question = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)
bot_contentf = bot_question.choices[0].message.content.strip()
messages.append({"role" : "assistant", "content" : f"{bot_contentf}"})
print(f"Bot : {bot_contentf}")

while i > 0:
  user_content = input("user: ")
  messages.append({"role" : "user", "content" : f"{user_content}"})

  bot_says = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)
  bot_content = bot_says.choices[0].message.content.strip()
  messages.append({"role" : "assistant", "content" : f"{bot_content}"})
  print(f"Bot : {bot_content}")

  i = i-1

messages.append({"role": "system", "content": "from previous messages, define single topic."})
bot_thinks_topic = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)
bot_topic = bot_thinks_topic.choices[0].message.content.strip()
messages.append({"role" : "assistant", "content" : f"{bot_topic}"})

#input: user inputs the topic.
#topic = input("user: ")
topic = bot_topic

api_key_youtube = :)

youtube = build('youtube','v3',developerKey=api_key_youtube)

request2 = youtube.search().list(
  q = f"{topic}",
  part = "snippet",
  maxResults = 1,
  regionCode = "KR"
)

response = request2.execute()

for item in response['items']:
    vid_id = item['id']['videoId']
    yt_link = f'https://youtu.be/{vid_id}'

print("Bot: 추천 영상을 보내드릴게요!: ", yt_link)