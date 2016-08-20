var app = angular.module('myApp',['ngResource']).factory('Local', function ($resource) {
    return $resource('http://getaplace.herokuapp.com/api/lugares/');
}).factory('LocalEspecifico', function ($resource) {
  return $resource('http://getaplace.herokuapp.com/api/lugares/:id');
}).factory('ReviewsLocal', function ($resource){
  return $resource('https://getaplace.herokuapp.com/api/lugares/reviews/:id');
}).factory('BuscaTags', function ($resource){
  return $resource('https://getaplace.herokuapp.com/api/lugares/busca/nome/:nome/endereco/:endereco/bairro/:bairro/cidade/:cidade/estado/:estado/pais/:pais/tags/:tags/');
}).factory('AdicionaReview', function ($resource){
  return $resource('https://getaplace.herokpais/api/locacao/reviews');
})
;
