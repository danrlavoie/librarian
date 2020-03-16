class SearchResults:
	BEGIN_BLOCK = {
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": (
				"These were the results of my search:",
			),
		},
	}
	DIVIDER_BLOCK = {"type": "divider"}

	def __init__(self, channel):
		self.channel = channel
		self.username = "librarian"
		self.icon_emoji = ":books:"
		self.timestamp = ""

	def get_message_payload(self):
		return {
			"ts": self.timestamp,
			"channel": self.channel,
			"username": self.username,
			"icon_emoji": self.icon_emoji,
			"blocks": [
				BEGIN_BLOCK,
				DIVIDER_BLOCK,
				*self._get_search_results(),
			]
		}
	def _get_search_results(self):
		return {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": (
					"Dan: Hello World",
				),
			}
		}