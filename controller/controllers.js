app.controller('ResourceController', function($scope, Local) {
    var locais = Local.query(function() {
    console.log(locais);
  });
});
