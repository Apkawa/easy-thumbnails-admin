'use strict'
const gulp = require('gulp')
const initTasks = require('gulp-frontend-tools')

var config = {
  project: {
    name: 'easy_thumbnails_admin',
    app_root: '{{ _.project_root }}/frontend/',
    dist_root: '{{ _.project_root }}/{{ _.name }}/static/{{ _.name }}/',
    static_root: '/static/',
  },
  webpack: {
    hot: false,
    extract_css: false,
    commonChunk: false,
    config: {
      resolve: {
        alias: {}
      },
      externals: {
        jquery: 'django.jQuery'
      }
    }

  }
}

initTasks(gulp, config)
  .run()
