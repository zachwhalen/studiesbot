# Every @studiesbot tweet follows one of the following ridiculously simple templates:
# [Noun] Studies
# [Adjective Noun] Studies
# Post [Noun] Studies
# Dark [Noun] Studies

# Get your packages
import random, tweepy, wordfilter
from wordnik import *

# Set up Wordnik. Use your own API Key
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'YOURAPIKEY'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordsApi.WordsApi(client)

# Set up Twitter access. Use your own API keys
auth = tweepy.OAuthHandler('consumer_key', 'consumer_token')
auth.set_access_token('key', 'secret')
api = tweepy.API(auth) 

# Grab a random noun from Wordnik
noun = wordApi.getRandomWord(includePartOfSpeech='noun',minCorpusCount=15000,hasDictionaryDef='true',minDictionaryCount=20)
lowerNoun = noun.word
noun = noun.word.capitalize()

# Grab a random adjective from Wordnik
adjective = wordApi.getRandomWord(includePartOfSpeech='adjective',minCorpusCount=15000,hasDictionaryDef='true',minDictionaryCount=20)
lowerAdjective = adjective.word
adjective = adjective.word.capitalize()

# Make a bunch of possibilities. Technically, this is a very inefficient way to get the final output, but whatevs
subjects = ["Dark " + noun, "Post-" + noun, adjective + " " + noun, noun, "Critical " + noun, "New " + noun, "Trans" + lowerNoun, "Critical " + adjective, "Comparative " + noun, "Early " + noun, "Early " + adjective + " " + noun, "Ethno" + lowerNoun, "Medieval " + noun, "Human " + noun, noun + " Policy", "Global " + noun, "Digital " + noun, "Para" + lowerAdjective, "Contemporary " + adjective + " " + noun]

# Pick a random item from the array above. Again, very inefficient. 
subject = random.choice(subjects)

# Add "Studies" to the newly picked subject.
studies = subject + " Studies"

# If the subject matches one of the blacklisted words, exit it.
# You could just make it choose again, but I wanted to terminate the bot as punishment.
if wordfilter.is_blacklisted(studies) == 1:
    print "BAD: " + studies
    raise SystemExit

# Display output on the console
print studies

# Send to Twitter
api.update_status(status=studies)
