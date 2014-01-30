(function() {
  var module = angular.module('JsonShare', ['ngRoute', 'JsonShare.controllers', 'JsonShare.services']);

  module.config(['$routeProvider', function($routeProvider) {
    'use strict';
    /*
    $routeProvider.when('/Json/:jsonId', {
      templateUrl: '/static/views/jsons/json.html',
        controller: 'JsonsController'
      }).when('/Json', {
      templateUrl: '/static/views/jsons/json.html',
        controller: 'JsonsController'
      }).otherwise({
        redirectTo: '/Json'
      });
    */
    }]);

    angular.module('JsonShare.controllers', ['JsonShare.services']);
    angular.module('JsonShare.services', []);
}());