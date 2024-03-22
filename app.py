from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from predict import predict_custom  # Import the predictor function
from ultralytics.yolo.utils import DEFAULT_CONFIG, ROOT

import shutil
import os
import glob

from ruamel.yaml import YAML

app = Flask(__name__, static_folder='static')

# Configure Flask to store uploaded files in the 'uploads' folder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif', 'mp4'}

STATIC_FOLDER = os.path.join('static')

# Function to check if a filename has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, browser may also submit an empty part without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # If the file is allowed and is an image or video
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        
            yaml=YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)
            CUSTOM_CONFIG = yaml.load(DEFAULT_CONFIG)
            CUSTOM_CONFIG['model'] = 'best.pt'
            CUSTOM_CONFIG['source'] = str(file_path)

            with open(ROOT / "yolo/configs/custom_config.yaml", 'wb') as f:
                yaml.dump(CUSTOM_CONFIG, f)

            # Run YOLOv8 prediction with 'best.pt' model
            output_results = predict_custom()

            if not isinstance(output_results, list):
                output_results = [output_results]

            #output_results = [output_results]
            print("Output result is :", output_results)
            # Check if the output_results list is not empty
            if output_results:
                output_path = os.path.join(output_results[-1], os.path.basename(str(file_path)))
                #src_dir = output_path
                print("Output path is :", output_path)
                #dst_dir = 'static'
                #print("dst_dir :", dst_dir)
                shutil.copy(output_path, STATIC_FOLDER)

                full_filename = os.path.join(STATIC_FOLDER, os.path.basename(str(file_path)))
                file_name = os.path.basename(full_filename)
                print(file_name)
                # Pass the output results to the template for rendering
                #return render_template('index.html', file_path=file_path, output_results=new_path)
                return render_template("index.html", user_image=file_name)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
