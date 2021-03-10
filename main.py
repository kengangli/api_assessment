import conferenceApi

#
# main
#

print( "all speakers")
spkrList=conferenceApi.getSpeakers()
for spk in spkrList:
    print(spk["name"])

complete = True
while complete:
    print("please type in speaker name, to list speaker's sessions. Otherwise press enter to quite ")
    speakerName = input()
    if speakerName == '':
        break
    
    sessionTopic_list = conferenceApi.getSpeakerSessions(speakerName)
    for st in sessionTopic_list:
        print(st['title'] + ' timeslot: '+ st['timeslot'])

    print("please type in timeslot to list topics: ")
    tslot = input()

    topic_list = conferenceApi.getSessionTopics(tslot)
    for tl in topic_list:
        print('session: '+tl['sessionName'] + ' topic: ' + tl['topic'])

    speakerName = ''

