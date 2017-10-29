from flask import Flask,request,render_template,jsonify
import httplib2 as h
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def espa():
    if request.method == 'GET':        
        return render_template('index.html')
    elif request.method == 'POST':
        img_url = request.form['url']
        
        url2post= 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key={YOUR-API-KEY}&version=2016-05-20&url=%s' %img_url

        poster = h.Http()
        response, content = poster.request(url2post,method="POST")
        result = hotdogqualifier(json.loads(content))
        return result


def hotdogqualifier(arg):
    print arg['images'][0]
    print arg['images'][0]['classifiers'][0]
    for item in arg['images'][0]['classifiers'][0]['classes']:
        if item['class'] == 'hotdog' and item['score']>0.5:
            return "HOT DOG"
    
    return "NOT HOT DOG"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
