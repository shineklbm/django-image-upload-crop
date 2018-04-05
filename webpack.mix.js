let mix = require('laravel-mix');

mix.copy('node_modules/jquery-cropper/dist/jquery-cropper.min.js', 'assets/js/jquery-cropper.min.js')
    .copy('node_modules/cropperjs/dist/cropper.min.js', 'assets/js/cropper.min.js')
    .copy('node_modules/cropperjs/dist/cropper.min.css', 'assets/css/cropper.min.css');