import bs4

def yahoo(html):
    soup = bs4.BeautifulSoup(html)
    potential_ids = ['mediaarticlebody',
                     'mediablogbody',
                     'mediacontentstory']
    content = None
    for id in potential_ids:        
        content = soup.find(id = id)
        if content != None and len(content) > 0:
            break

    return content
