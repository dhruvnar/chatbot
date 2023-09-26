from bardapi import Bard 
import os
import time

os.environ['_BARD_API_KEY'] = "Zgh0iZ56_hgmHMwTfQRfWBlyTS6sXGYStAK7c9nm70SYpjGzvn_9Ndi4_5SO2ZaNA6oiVQ."

chat_bot = True
while chat_bot:
    input_text = input("> ")
    print(Bard().get_answer(input_text)['content'])
