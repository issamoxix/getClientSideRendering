from fastapi import FastAPI
from requests_html import AsyncHTMLSession
from sele import gethtml

app = FastAPI()


@app.get('/')

async def func(url:str):
    try:
        asession = AsyncHTMLSession()
        r = await asession.get(url)
        await r.html.arender(sleep=1)
    except:
        return 0
        pass

    return {"html":r.text}

@app.get('/sele')

def fk(url:str):
    return {"html":gethtml(url)}

