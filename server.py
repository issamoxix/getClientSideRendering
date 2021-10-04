from fastapi import FastAPI
from requests_html import AsyncHTMLSession
from sele import UseSele

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

def sele_func(url:str):
    useSele = UseSele(url)
    return {"html":useSele.gethtml()}

@app.get('/sele_wait')
def sele_wait(url:str,csss:str):
    useSele = UseSele(url)
    return {"html":useSele.waitEleme(csss)} 
