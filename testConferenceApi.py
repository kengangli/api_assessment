import unittest
import conferenceApi

class TestConferenceAPI(unittest.TestCase):
	def test_speakers(self):
		speakers = conferenceApi.getSpeakers()
		speakersCount = len(speakers)
		self.assertEqual(speakersCount,99)

	def test_sessions(self):
		skrs = conferenceApi.getSpeakers()
		sessions =  conferenceApi.getSpeakerSessions('Scott Guthrie')
		sessionsCount = len(sessions)
		self.assertEqual(sessionsCount, 4)

	def test_topics(self):
		speakers = conferenceApi.getSpeakers()
		sessions = conferenceApi.getSpeakerSessions('Scott Guthrie')
		topics = conferenceApi.getSessionTopics('04 December 2013 13:40 - 14:40')
		topicsCount = len(topics)
		self.assertEqual(topicsCount, 2)

if __name__ == '__main__':
	unittest.main()
    
