import os
from base64 import b64encode
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('open_ai_key')




def open_ai(t):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=t,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ai_text = response.get('choices')[0].get('text').strip()
    return ai_text
    
def reads_file(adds):
    with open(adds,'r+') as file:
        return file.read().strip().split('\n')



def wp_paragraph(text):
    codes =f' <!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes

def wp_h2(text):
    codes = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return codes

def wp_images(url,name):
    codes =f'<!-- wp:image {{"align":"center","id":733,"sizeSlug":"large","linkDestination":"none"}} --><figure class="wp-block-image aligncenter size-large"><img src="{url}" alt="{name}" class="wp-image-733"/><figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    return codes


def wp_h3(text):
    codes = f'<!-- wp:heading --><h3>{text}</h3><!-- /wp:heading -->'
    return codes
    
    
def generate_content(*args):
    codes = ''
    for arg in args:
        codes +=arg
    return codes

def headers(user):
    passwords = os.getenv('wp_passwords')
    credentials = f'{user}:{passwords}'
    token = b64encode(credentials.encode())
    header = {'authorization': f'Basic {token.decode("utf-8")}'}
    return header



