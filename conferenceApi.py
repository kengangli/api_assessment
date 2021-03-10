import requests
import json

#
# Global Variables
#
speakers = []
speakerSessions = []
sessionTopics = []
#
# Get 
#
def getResource(url):
	headers={'Content-Type':'application/json','Ocp-Apim-Subscription-Key':'67f50e1f75e84a78856eb15d8ec10a48','Api-version':'v1'}
	response=requests.get(url,headers=headers)
	resp_status=response.status_code
	res_arr=json.loads(response.text)
	return res_arr
	
def getSpeakers():
	url = "https://conferenceapi.azurewebsites.net:443/speakers"
	res_arr=getResource(url)
	items = res_arr['collection']['items']
	speakers.clear()
	for item in items:
        	speaker = {'name':None,'url_sessions':None}
        	speaker['name']=item['data'][0]['value']
        	speaker['url_sessions']=item['links'][0]['href']
        	speakers.append(speaker)
	
	return speakers

def getSpeakerSessions(name):
    for spkr in speakers:
        if spkr['name'] == name:
            url_sessions=spkr['url_sessions']

    sessions=getResource(url_sessions)['collection']['items']
    speakerSessions.clear()
    
    for sess in sessions:
        session = {'title':None,'timeslot':None,'url_topics':None}
        session['title']=sess['data'][0]['value']
        session['timeslot']=sess['data'][1]['value']
        session['url_topics']=sess['links'][1]['href']
        speakerSessions.append(session)
    
    return speakerSessions

def getSessionTopics(timeslot):
    for spss in speakerSessions:
        if spss['timeslot'] == timeslot:
            url_topics = spss['url_topics']
            sessName = spss['title']
        
    topics=getResource(url_topics)['collection']['items']
    sessionTopics.clear()

    for tp in topics:
        topic = {'sessionName':None,'topic':None}
        topic['sessionName'] = sessName
        topic['topic'] = tp['data'][0]['value']
        sessionTopics.append(topic)
    
    return sessionTopics


