# django-image-upload-crop
A widget for image upload with features like preview, zoom, crop functionality

## Installation

1. Clone repository
2. Create a file called local.py under imgcrop/settings/ directory
3. Add your local database details to imgcrop/settings/local.py
5. Activate your environment (if you are using miniconda just type "source activate YOUR_ENVIRONMENT_NAME")
6. Then run "python manage.py migrate" from project root
7. Run "python manage.py runserver".
8. Open your browser type "http://127.0.0.1:8000" (This may be different on your machine)


### Frontend

I am using webpack and laravel-mix for asset management, please feel free to play with the webpack.mix.js file and composer.js file for frontend changes. Please make sure that you run "npm install" and "npm run dev" to make the changes work.

Please feel free to contact me on shine@richkenmedia.com for any queries you may have.

