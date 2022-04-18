import openai

class EmailAssistant:
    def __init__(self, key):
        self.key = key

    def email(self, start:str = "Hi, John Doe", len:int = 250, draft:str = "recruiter, give me an referral for internship.", topic:str = 'Request for referral', random_state:float = 0.9 ) -> str:
        openai.api_key = self.key
        return openai.Completion.create(
            engine='text-davinci-002',
            prompt="Write me a professional style email start with '" + start + "' about '" + topic + "' and the email should be based on this draft: \"" + draft + "\"\n",
            temperature = random_state,
            max_tokens= len,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1,
            best_of=2
        ).get("choices")[0]['text'].strip()



