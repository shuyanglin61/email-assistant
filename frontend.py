from re import S
import streamlit as sl
from backend import EmailAssistant

class FrontEnd:
    def main(self):
        sl.title("Email Assistant via GPT-3")
        sl.markdown("*by Shuyang Lin*")
        k = sl.form(key = 'key', clear_on_submit= True)
        key = k.text_input("Input your OpenAI API key here:")
        but = k.form_submit_button(label = "Submit")

        if 'ready' in sl.session_state.keys() and sl.session_state['ready']:
            k.markdown('*API key received. The app will not check the validity.*')
            backend = EmailAssistant(key)
            with sl.form(key = "form", clear_on_submit=False):
                c1, c2 = sl.columns(2)
                with c1:
                    topic = sl.text_input("Input the topic of the email here:")
                    sl.markdown('*Example: Referral request*')
                with c2:
                    start = sl.text_input("Input the greeting and receiver here:")
                    sl.markdown('*Example: Hi, John Doe*')

                draft = sl.text_input("Input the plain language here:").strip()
                sl.markdown('''
                *Example:*

                *Recruiter, give me an referral for internship.*
                ''')
                with c1:
                    slider1 = sl.slider("Select the maximum length of words:", min_value=75, max_value=250, value=125)
                with c2:
                    slider2 = sl.slider("Select the random state.", min_value=0.0, max_value=1.0, value=0.5)
                button = sl.form_submit_button(label = "Generate")
                if 'generate' in sl.session_state.keys() and sl.session_state['generate']:
                    with sl.spinner("Generating the email..."):
                        output = backend.email(start = start, len = slider1, draft = draft, topic = topic, random_state=slider2)
                    sl.markdown("## Email Output")
                    sl.write(output)
                    sl.markdown("[Send via Google]({})".format("https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + self.format_email(output)))
                else:
                    if button:
                        sl.session_state['generate'] = True
                        sl.experimental_rerun()
        else:
            sl.warning('A personal API key issued by OpenAI is essential for this app. Please see more information at https://beta.openai.com/account/api-keys')
            if but:
                sl.session_state['ready']=True
                sl.experimental_rerun()

        sl.markdown("""
        &nbsp;

        &nbsp;

        &nbsp;

        &nbsp;

        &nbsp;

        &nbsp;

        &nbsp;

        *About*

        *People on the Autism spectrum can tend to write and speak bluntly, 
        which can be an impediment to the smooth comminication with neurotypical colleagues in a work environment. 
        We'll explore using Transformers to create a style-transfer model which takes a draft e-mail, 
        and rewrites it in a professional style.*

        *Main Target*

        *Transfer plain language to draft a professional e-mail*

        *Announcement*

        *This app is only used for DS-5899-01 Transformers Special Course. It's a must to follow all rules made by OpenAI.*
        
        """)
    def format_email(self, output):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        string = list(output)
        for i, c in enumerate(string):
            if c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n' :
                string[i] = '+'
        return ''.join(string)

test = FrontEnd()
test.main()