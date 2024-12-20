from flask import Flask
app1=Flask(__name__)

@app1.route("/hello1")

def hello():
    output='''<body bgcolor=red> <h1> Hello World </h1> </body>'''
    return output
def helloworld1():
    output='''<body bgcolor=red>
<h1 > This Is My 1st Flask Programme Is Executed Successfully<h1>
</body>'''
    return output
def helloworld2():
    output='''<body bgcolor=yellow >
<h1 bgcolor=green> This Is My 1st Flask Programming<h1>
</body>'''
    return output


app1.add_url_rule('/hello2',"helloworld2",helloworld2)
app1.run()






