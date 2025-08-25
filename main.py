from flask import Flask, render_template, request, file
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'txt', 'jpg', 'gif', 'pdf'}

@app.route('/upload')
def upload():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET','POST'])
def uploader_file():
  if request.method =='POST':
    if file not in request.files:
      return render_template('index.html', msg ='No such file exists :)')
    if file.filename =='':
      return render_template('index.html', msg="No file selected :]")
    if file and allowed_file(file.filename):
      file.save(file.filename)
      return render_template('index.html', msg="File uploaded successfully :}")
    else:
      return render_template('index.html', msg="Isn't supported, upload only png, jpg, pdf, gif or txt. :(")


@app.route('/') 
def index():
    return render_template('index.html')
app.run(host='0.0.0.0', port=8000)
    

      
