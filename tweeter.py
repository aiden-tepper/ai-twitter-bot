import tweepy, time
import openai, json
import tokens

CONSUMER_KEY = tokens.CONSUMER_KEY
CONSUMER_SECRET = tokens.CONSUMER_SECRET
ACCESS_TOKEN = tokens.ACCESS_TOKEN
ACCESS_SECRET = tokens.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

openai.api_key = tokens.OPENAI_KEY

while True:
    response = openai.Completion.create(
        model="text-curie-001",
        prompt="Come up with a satirical title for an OANN op-ed.",
        temperature=1,
        max_tokens=70,
        top_p=1,
        best_of=4,
        frequency_penalty=1.49,
        presence_penalty=1.51
    )
    tweet = response["choices"][0]["text"]
    print(tweet)
    user_input = input("Tweet? y/n: ")
    if user_input == "y":
        break

api.update_status(tweet)
print("Tweeting!")
