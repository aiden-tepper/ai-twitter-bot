import tweepy, time
import openai, json

CONSUMER_KEY = 'LdqSOsAUKYT10OtNmNNiqxmbi'
CONSUMER_SECRET = 'vZ1EG4kZkRMHMLR0p4nQf54EPDr41P2LNLQXLAmS2nW2lEWNR1'
ACCESS_TOKEN = '2360233446-hRskwevgp1SDuJ62MWYDOas3TRX50PGApRPJJoC'
ACCESS_SECRET = 'kJ9GQ3IuzwxSut5SHqbSPRxemp8GEWo3vkAaRRHSFBtwR'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

openai.api_key = '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'

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
