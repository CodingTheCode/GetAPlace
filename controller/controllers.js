app.controller('ResourceController', function($scope, Local, BuscaTags) {
  var locais = Local.query(function() {
    //console.log(locais);
  });
  $scope.espacos = locais;

  $scope.atualizaId = function(id){
    $scope.espaco = $scope.espacos[id];
  };
  
  $scope.pesquisarTags = function() {
    if($scope.id==null) $scope.id='_';
    if($scope.nome==null) $scope.nome='_';
    if($scope.endereco==null) $scope.endereco='_';
    if($scope.bairro==null) $scope.bairro='_';
    if($scope.cidade==null) $scope.cidade='_';
    if($scope.estado==null) $scope.estado='_';
    if($scope.pais==null) $scope.pais='_';
    if($scope.tag==null) $scope.tag='_';
    
    var reviews = BuscaTags.query({ id: $scope.id ,nome: $scope.nome, endereco: $scope.endereco, bairro: $scope.bairro, cidade: $scope.cidade, estado: $scope.estado, pais: $scope.pais, tags: $scope.tag }, function() {
      
      //nome, endereco, bairro, cidade, estado, pais, tag(separado por virgulas)
      console.log(reviews);
      $scope.espacos = reviews;
    });
  };
  
});

app.controller('ReviewsLocalController', function($scope, ReviewsLocal){
  $scope.id=1;
  var reviews = ReviewsLocal.query({ id: $scope.id }, function() {
    //console.log(reviews);
  });
  $scope.reviews = reviews;
});

login.controller('AdicionaReviewController', function($scope, AdicionaReview){
  console.log("bla");
  $scope.escreverReview = function(){
    var reviews = AdicionaReview.save({local: $scope.local, autor: $scope.idAutor,  titulo: $scope.titulo, texto: $scope.texto, avaliacao: $scope.avaliacao}, function() {
      console.log(reviews);
    });
    $scope.reviews = reviews;
  };
});
