import requests

def get(self, appid, steamid, class_id):
    allowed = ['570', '205790']
    query = "GetEquippedPlayerItems/v1/?steamid={}&class_id={}&key={}&format={}"
    query = query.format(steamid, class_id, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    if str(appid) not in allowed:
        print "Unfortunately this method is non-existent for this game"
        return False

    r = requests.get(self.method.format(appid) + query)
    return r.content
