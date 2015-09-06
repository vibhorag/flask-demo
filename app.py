from flask import Flask, render_template, request, redirect
from stockplotter import getstockdata,generateplot
import traceback

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
  print "This is main()"
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():

  print "Arrived in index()"
  print "request.method: ", request.method
  #Check the request
  if request.method=='GET':
    print "This is get GET"
    return render_template('layout.html',bokeh_script="",bokeh_div="",note="")


  else:
    print "This is POST"
    #check the post

    try:
        # Request for API-call
        data = getstockdata(request.form['stock'])
    except:
        note = "Oh no.May be i'am not in Database.?"
        return render_template('layout.html',bokeh_script="",bokeh_div="",note=note)

    # Bokeh Plot
    desired_columns = request.form.getlist('features')
    script,div,note = generateplot(data,desired_columns,request.form['stock'])

    # Render
    return render_template('layout.html',bokeh_script=script,bokeh_div=div,note=note)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=33507,debug=True)
