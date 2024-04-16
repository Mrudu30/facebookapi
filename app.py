from flask import Flask,redirect,url_for,render_template,request,jsonify
from modules.fbhistory import Fbhistory
from werkzeug.utils import secure_filename
import os
import shutil

fb = Fbhistory()

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        return render_template('index.html')
    return render_template('index.html')

@app.route("/make-a-post",methods=['GET','POST'])
def make_a_post():
    if request.method == 'POST':
        image = request.files.get('image')
        image_path=''
        if image:
            # Save the image to a temporary folder
            temp_folder = 'E:\\facebookapi\\static\\uploads'
            os.makedirs(temp_folder, exist_ok=True)
            filename = secure_filename(image.filename)
            image_path = os.path.join(temp_folder, filename)
            image.save(image_path)
            shutil.rmtree(temp_folder)
        result = fb.fbposts(request.form,image_path)
        return jsonify({'status':result})

    pagelist = fb.get_all_fbpages()
    return render_template('make_a_post.html',pagelist=pagelist)

if __name__ == '__main__':
    app.run(port=5000,debug=True)