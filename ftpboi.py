from flask import Flask, request, redirect, url_for, session, render_template
import os

app = Flask(__name__)
app.secret_key = 'randomstring'

upload_folder = os.path.join(os.getcwd(),'uploads')
app.config['UPLOAD_FOLDER'] = upload_folder
print(str(upload_folder))

download_folder = os.path.join(os.getcwd(),'randomfiles')
app.config['DOWNLOAD_FOLDER'] = download_folder
print(str(download_folder))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file'] # getting the file from the request
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename)) # saving the file to the upload folder
    return 'upload successful' 

@app.route('/upload-successfull')
def uploaded_file():
    return 'File uploaded successfully'

@app.route('/view-uploads', methods=['GET','POST'])
def ftp_code():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            file_list = os.listdir(upload_folder)
            return render_template('view-uploads.html',file_list=file_list)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return render_template('view-uploads.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

if  __name__ == '__main__':
    app.run(port=5000,debug=True)
    print("Starting python flask server on port 5000")
