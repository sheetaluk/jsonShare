module.exports = function (grunt) {
  var userConfig = require('./build.config.js');

  var taskConfig = {
    // The clean task ensures the parsed css is removed
    clean: ["css/compiled/"],

    // Compress generated css files
    cssmin: {
      "css/compiled/jsonShare.css": ["css/compiled/jsonShare.css"]
    },

    // Automatically run a task when a file changes
    watch: {
      styles: {
        files: ["css/less/*"],
        tasks: "less"
      }
    },

    // Compile specified less files
    less: {
      compile: {
        options: {
          // These paths are searched for @imports
          paths: ["css/less"]
        },
        files: {
          "css/compiled/jsonShare.css": "css/less/jsonShare.less"
        }
      }
    },

    concat: {
      development: {
        options: {
          separator: ';'
        },
        src: [
          '<%= lib_files.js %>',
          '<%= app_files.js %>'
        ],
        dest: 'js/concatenated/main.js'
      }
    },

    uglify: {
      my_target: {
        files: {
          'js/minified/main.min.js': ['js/concatenated/main.js']
        },
        options: {
          mangle: false
        }
      }
    },

    cacheBust: {
      options: {
        encoding: 'utf8',
        algorithm: 'md5',
        length: 16
      },
      assets: {
        files: [{
          src: ['index.html']
        }]
      }
    },
   
    /**
     * Defines jshint rules.
     */
    jshint: {
      files: ['Gruntfile.js', '<%= app_files.js %>'],
      options: {
        curly: true,
        devel: true,
        eqnull: true,
        evil: true,
        immed: true,
        maxcomplexity: 8,
        newcap: true,
        noarg: true,
        sub: true,
        trailing: true,
        globals: {
          angular: true,
          Highcharts: true,
          Rickshaw: true
        }
      }
    },

    karma: {
      // all other test configs will inherit/override these options
      options: {
        basePath: '.',
        frameworks: [
          'mocha',
          'chai',
          'sinon'
        ],
        browsers: ['PhantomJS'],
        files: [
          'js/minified/main.min.js',
          'js/jsonShare/test/lib/angular/angular-mocks.js',
          'js/jsonShare/test/unit/**/*.js'
        ]
      },
      // continuous integration tests
      continuous: {
        singleRun: true,
        reporters: ['spec']
      },
      // dev tests
      dev: {
        reporters: 'progress',
        background: true
      }
    }
  };

  // Load tasks so we can use them
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-contrib-clean");
  grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-cssmin");
  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-cache-bust');
  grunt.loadNpmTasks('grunt-karma');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  grunt.initConfig(grunt.util._.extend(taskConfig, userConfig));

  grunt.registerTask('test', [
    'jshint'
  ]);

  // The dev task will be used during development
  grunt.registerTask("dev", [
    "concat:development",
    "uglify",
    "cacheBust",
    "clean",
    "less:compile"
  ]);
};