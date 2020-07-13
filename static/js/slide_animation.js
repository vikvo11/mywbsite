angular.module('MyApp.controllers', [])

.controller('MainController', function($rootScope, $window, $scope){
 
  
  $rootScope.$on('$stateChangeStart', function(){
    $scope.slide = $scope.slide || 'slide-left'
	console.log('$scope.slide ='+$scope.slide);
  });
  
 
  
})