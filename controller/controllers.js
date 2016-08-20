app.controller('ResourceController', function($scope, Local) {
  var locais = Local.query(function() {
    //console.log(locais);
  });
  $scope.espacos = locais;
});

app.controller('LocalUnicoController',function($scope, LocalEspecifico) {
  $scope.id=1;
  var entry = LocalEspecifico.get({ id: $scope.id }, function() {
    //console.log(entry);
  });
  $scope.espaco = entry;
});

app.controller('ReviewsLocalController', function($scope, ReviewsLocal){
  $scope.id=1;
  var reviews = ReviewsLocal.query({ id: $scope.id }, function() {
    console.log(reviews);
  });
  $scope.espaco = reviews;
});
