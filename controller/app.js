var app = angular.module('myApp',['ngResource']).factory('Local', function ($resource) {
    return $resource('http://getaplace.herokuapp.com/api/lugares/');
}).factory('LocalEspecifico', function ($resource) {
  return $resource('http://getaplace.herokuapp.com/api/lugares/:id');
}).factory('ReviewsLocal', function ($resource){
  return $resource('https://getaplace.herokuapp.com/api/lugares/reviews/:id');
})
;