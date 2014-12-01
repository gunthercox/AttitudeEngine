class Attitude(object):

    def __init__(self, text):
        self.text = text

        # Benchmarks (statements that should express specific attitudes)

        # Morality: Is it *right* to say this?

        # Check by context (based on a conversation) or structure (the useage of the words)?

        '''
        stagnating helpless over-whelming    anxious   difficult
        submissive unsure    frustrated    different   ambitious
        tranquil   challenge   neutral      positive   assertive
        relaxed    satisfied     ok        accepting  determined
        comfortable confident  excited        joy          happy
        '''

        self.ATTITUDE_MATRIX = [
            ["stagnating", "helpless", "over-whelming", "anxious",
             "difficult", "ambitious", "assertive", "determined",
             "confident", "excited", "joy", "happy", "comfortable",
             "relaxed", "tranquil", "submissive"],
            ["unsure", "frustrated", "different", "challenge",
             "positive", "satisfied", "ok", "accepting"],
            ["neutral"]
        ]

        self.facets = {}
        self.facets["adaptation"] = 0
        self.facets["approach"] = 0
        self.facets["energy"] = 0
        self.facets["comprehension"] = 0
        self.facets["engagement"] = 0
        self.facets["responsibility"] = 0
        self.facets["outcome"] = 0

    def is_sarcastic(self):
        """
        People use sarcasm incorrectly, because of this we will start by
        eliminating the sentiments that are closest to the origional meaning.
        """
        # TODO
        return False

    def get_sentiment(self):
        """
        Returns the sentiment analysis for a given line of text.
        """

        # If the text is sarcastic, then return a different meaning
        if self.is_sarcastic():
            return not sentiment

        return sentiment
