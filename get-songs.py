import sys
import spotipy
from subprocess import call
import spotipy.util as util
from dotenv import load_dotenv
load_dotenv()

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    while results:
        for item in results['items']:
            track = item['track']
            call(['ytmdl', track['name'] + ' - ' + track['artists'][0]['name']])
        results = sp.next(results)
else:
    print("Can't get token for", username)