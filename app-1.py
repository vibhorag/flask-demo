from flask import Flask, render_template, request, redirect
from basic_stock_visual import getstockdata,plot_generate
import traceback

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
  print "Hello main()"
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():

  print "Hello index()"
  print "Show request.method: ", request.method
  # Show the initial question sheet
  if request.method=='GET':
      print "Arrived in GET"
      return render_template('pagelayout.html',bokeh_script="",bokeh_div="",note="")

  # Form was filled out, time to draw the plot
  else:
    print "Arrived in POST",request.method
    
    try:
        data = getstockdata(request.form['stock'])
    except:
        note = "ERROR getting stock data! Faulty ticker symbol?"#+traceback.format_exc()
        return render_template('pagelayout.html',bokeh_script="",bokeh_div="",note=note)
    

    check_columns = request.form.getlist('features')
    script,div,note = generateplot(data,desired_columns,request.form['stock'])
    
    
    # Generate bokeh plot
    check_columns = request.form.getlist('features')
    script,div,note = plot_generate(data,check_columns,request.form['stock'])

    # Render
    return render_template('pagelayout.html',bokeh_script=script,bokeh_div=div,note=note)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=33507,debug=True)