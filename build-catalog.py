import urllib.request,re,json,pathlib
s=urllib.request.urlopen('https://html.spec.whatwg.org/multipage/indices.html').read().decode()
pathlib.Path('/tmp/html-index.html').write_text(s)
def table(id):
 p=s.index('id='+id); p=s.index('<table',p); return s[p:s.index('</table>',p)]
def clean(x):return re.sub(r'\s+',' ',re.sub('<[^>]+>','',x)).strip()
def rows(t):
 out=[]
 for r in re.split(r'<tr[^>]*>',t)[1:]:
  cells=re.split(r'<t[hd][^>]*>',r)[1:]
  if len(cells)>1:out.append(cells)
 return out
els=[]
for c in rows(table('elements-3')):
 ns=[clean(x) for x in re.findall(r'<code[^>]*>(.*?)</code>',c[0],re.S)]
 for n in ns:
  if n in ('svg','math'):continue
  url=re.search(r'<a[^>]*href=([^ >]+)',c[0]); url=url[1].strip('\"') if url else ''
  if not url:continue
  attrs=[clean(x) for x in re.findall(r'<code[^>]*>(.*?)</code>',c[5],re.S)]
  els.append(dict(name=n,description=clean(c[1]),parents=clean(c[3]),children=clean(c[4]),attributes=attrs,url='https://html.spec.whatwg.org/multipage/'+url))
attrs={}
for c in rows(table('attributes-3')):
 ns=[clean(x) for x in re.findall(r'<code[^>]*>(.*?)</code>',c[0],re.S)]
 for n in ns:
  url=re.search(r'<a[^>]*href=([^ >]+)',c[0]);url=url[1].strip('\"') if url else 'indices.html#attributes-3'
  a=attrs.setdefault(n,dict(name=n,description=clean(c[2]),values=clean(c[3]),elements=[],url='https://html.spec.whatwg.org/multipage/'+url))
  a['elements']+= [clean(x) for x in re.findall(r'<code[^>]*>(.*?)</code>',c[1],re.S)]
  if 'HTML elements' in clean(c[1]):a['global']=True
p=s.index('id=attributes-3'); p=s.index('</table>',p); t=s[s.index('<table',p):s.index('</table>',s.index('<table',p))]
events=[]
for c in rows(t):
 ns=[clean(x) for x in re.findall(r'<code[^>]*>(.*?)</code>',c[0],re.S)]
 for n in ns:events.append(dict(name=n,description=clean(c[2]),event=True,elements=['body'] if 'body' in clean(c[1]) else [],values='JavaScript event handler',url='https://html.spec.whatwg.org/multipage/webappapis.html#handler-'+n,**{'global':'body' not in clean(c[1])}))
for a in attrs.values():a['elements']=sorted(set(a['elements']))
print(len(els),len(attrs),len(events));print(els[:1]);print(list(attrs.values())[:2])
(pathlib.Path(__file__).parent/'dist/catalog.json').write_text(json.dumps(dict(elements=els,attributes=list(attrs.values())+events,date='2026-10-04'),indent=2))
