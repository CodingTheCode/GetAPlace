app.controller('ResourceController', function($scope, Local, LocalEspecifico) {
  var locais = Local.query(function() {
    console.log(locais);
  });
  $scope.espacos = locais;
  
  $scope.atualizaId = function(id){
    $scope.espaco = $scope.espacos[id];
  };
});

app.controller('ReviewsLocalController', function($scope, ReviewsLocal){
  $scope.id=1;
  var reviews = ReviewsLocal.query({ id: $scope.id }, function() {
    //console.log(reviews);
  });
  $scope.reviews = reviews;
});

app.controller('BuscaTagsController', function($scope, BuscaTags){
  //$scope.nome='mesa de bilhar';
  //$scope.endereco='_';
  // $scope.bairro='_';
  // $scope.cidade='_';
  // $scope.estado='_';
  // $scope.pais='_';
    $scope.tag='_';


  $scope.pesquisarTags = function() {
    var reviews = BuscaTags.query({ id: $scope.id ,nome: $scope.nome, endereco: $scope.endereco, bairro: $scope.bairro, cidade: $scope.bairro, estado: $scope.estado, pais: $scope.pais, tags: $scope.tag }, function() {
      //nome, endereco, bairro, cidade, estado, pais, tag(separado por virgulas)
      //console.log(reviews);
    });
      $scope.espaco = reviews;
  };
});

app.controller('AdicionaReviewController', function($scope, AdicionaReview){
  var reviews = ReviewsLocal.query({local: $scope.local, autor: $scope.idAutor,  titulo: $scope.titulo, texto: $scope.texto, avaliacao: $scope.avaliacao}, function() {
    //console.log(reviews
  });
  $scope.reviews = reviews;
});
