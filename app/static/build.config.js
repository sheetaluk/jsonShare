module.exports = {
  /**
   * This is a collection of file patterns that refer to our app code.
   * These file paths are used in the configuration of build tasks.
   */
  app_files: {
    js: ['js/jsonShare/**/*.js', '!js/jsonShare/test/**/*.js']
  },

  /**
   * This is a collection of third party libraries.
   */
  lib_files: {
    js: [
      'js/lib/angular/angular.js',
      'js/lib/angular/angular-resource.js',
      'js/lib/angular/angular-route.js'
    ]
  }
};