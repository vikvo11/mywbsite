var uiView = angular.module('uiView',['ui.router'])

.config(['$urlRouterProvider','$stateProvider',function($urlRouterProvider,$stateProvider)
 {
		
		$urlRouterProvider.otherwise('/');
		//$urlRouterProvider.when('/main','/123');
		var glasses={
			url:'/',
				views: {
						'glasses': {
						templateUrl: 'static/template/_u_glasses.html',
						
						controller:'myController',
								  }
						,'content': {
						templateUrl: 'static/template/_u_bottles.html',
						controller: 'myController'
									}/**/
						},
				//templateUrl: 'static/page1.html',
				//controller:'myController1',
				controllerAs:'home Ctrl'
		}
		
		var IdGlasses={
		url:'/glass/{glassesId}',
			views: {
						'glasses': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_slick_1.html',
						controller:'myGlass',
								  }
						/*,'content': {
						templateUrl: 'static/template/_u_bottles.html',
						controller: 'myGlass'
									}*/
			},
			//controller:'SlickController',
			//controller:'myController',
			controllerAs:'home Ctrl'
		}
		
		var slick={
		url:'/glasses',
			views: {
						'glasses': {
						templateUrl: 'static/template/_u_slick_1.html'
						,controller:'SlickController',
								  },
			},
			controller:'myController',
			controllerAs:'home Ctrl'
		}
			
		var students={
			url:'/students',templateUrl: 'static/page2.html',controller:'homeController',controllerAs:'home Ctrl',		resolve:{
				studentlist: function($http){
					return $http.get('/testget')
						.then(function (response) {
							return response.data;
						})
				}
			}
		}
		
		$stateProvider.state("home",glasses);
		$stateProvider.state("IdGlasses",IdGlasses)
		$stateProvider.state("home-glasses",slick)
		//.state("home-glasses",{url:'/glasses',templateUrl: 'static/page2.html',controller:'homeController',controllerAs:'home Ctrl'})
		.state("students",students);
		
		//.state("studentDetails",{url:'/students/:id',templateUrl: 'static/page2.html',controller:'homeController',controllerAs:'home Ctrl'});
		//$routeProvider.when('/page1',{templateUrl: 'static/page1.html'});
		//$routeProvider.when('/page2',{templateUrl: 'static/page2.html'});
		//$routeProvider.otherwise('/',{redirectTo:'/home'});	
		
		//$locationProvider.html5Mode({enabled: true,requireBase:false})
	}])
	

	;
	
	

		

		
uiView.controller('myController', function($scope, $http){
    $http({
    method: 'get', 
    url: '/main_view_g'
}).then(function (response) {
    console.log(response, 'res');
    data = response.data;
	$scope.glasses = response.data;
	$scope.glassID = response.data;
},function (error){
   console.log(error, 'can not get data.');
})
});

uiView.controller('myGlass', function($scope, $http,$stateParams){
    $http({
    method: 'get', 
    url: '/glass/'+$stateParams.glassesId
}).then(function (response) {
    console.log(response, 'GlassID');
    data = response.data;
	$scope.glassID = response.data;
},function (error){
   console.log(error, 'can not get data.');
})
});  	


uiView.controller('glasses', function($scope){ 
$scope.glass = [{
		id: '1001',
        name: 'Nokia Lumia 630',
        year: 2014,
        price: 200,
        company: {
            name: 'Nokia',
            country: 'Финляндия'
        }
    }]
}); 

//
//.controller('studentsController',function (studentslist,$state,$location){
//	var vm = this;
//	vm.studentSearch=function(){
//		if(vm.name)
//			$location.url('/studentsSearch/'+vm.name)
//		else
//			$location.url('/studentsSearch')
//	}
//	vm.reloadData = function() {
//		$state.reload();
//	}
//	vm.students = studentslist;
//}
//	)


// $stateParams Service
// If you had a url on your state of: url: '/users/:id/details/{type}/{repeat:[0-9]+}?from&to'

// Then you navigated your browser to: '/users/123/details//0'

// Your $stateParams object would be { id:'123', type:'', repeat:'0' }

// Then you navigated your browser to: '/users/123/details/default/0?from=there&to=here'

// Your $stateParams object would be { id:'123', type:'default', repeat:'0', from:'there', to:'here' }

uiView.controller('SlickController', function ($scope, $timeout) {
    //====================================
    // Slick 1
    //====================================
    $scope.number1 = [1, 2, 3, 4, 5, 6, 7, 8];
    $scope.slickConfig1Loaded = true;
    $scope.updateNumber1 = function () {
      $scope.slickConfig1Loaded = false;
      $scope.number1[2] = '123';
      $scope.number1.push(Math.floor((Math.random() * 10) + 100));
      $timeout(function () {
        $scope.slickConfig1Loaded = true;
      }, 5);
    };
    $scope.slickCurrentIndex = 0;
    $scope.slickConfig = {
      dots: true,
      autoplay: true,
      initialSlide: 3,
      infinite: true,
      autoplaySpeed: 1000,
      method: {},
      event: {
        beforeChange: function (event, slick, currentSlide, nextSlide) {
          console.log('before change', Math.floor((Math.random() * 10) + 100));
        },
        afterChange: function (event, slick, currentSlide, nextSlide) {
          $scope.slickCurrentIndex = currentSlide;
        },
        breakpoint: function (event, slick, breakpoint) {
          console.log('breakpoint');
        },
        destroy: function (event, slick) {
          console.log('destroy');
        },
        edge: function (event, slick, direction) {
          console.log('edge');
        },
        reInit: function (event, slick) {
          console.log('re-init');
        },
        init: function (event, slick) {
          console.log('init');
        },
        setPosition: function (evnet, slick) {
          console.log('setPosition');
        },
        swipe: function (event, slick, direction) {
          console.log('swipe');
        }
      }
    };

    //====================================
    // Slick 2
    //====================================
    $scope.number2 = [{label: 1, otherLabel: 1}, {label: 2, otherLabel: 2}, {label: 3, otherLabel: 3}, {
      label: 4,
      otherLabel: 4
    }, {label: 5, otherLabel: 5}, {label: 6, otherLabel: 6}, {label: 7, otherLabel: 7}, {label: 8, otherLabel: 8}];
    $scope.slickConfig2Loaded = true;
    $scope.updateNumber2 = function () {
      $scope.slickConfig2Loaded = false;
      $scope.number2[2] = 'ggg';
      $scope.number2.push(Math.floor((Math.random() * 10) + 100));
      $timeout(function () {
        $scope.slickConfig2Loaded = true;
      });
    };

    $scope.slickConfig2 = {
      autoplay: true,
      infinite: true,
      autoplaySpeed: 1000,
      slidesToShow: 3,
      slidesToScroll: 3,
      method: {}
    };

    //====================================
    // Slick 3
    //====================================
    $scope.number3 = [{label: 1}, {label: 2}, {label: 3}, {label: 4}, {label: 5}, {label: 6}, {label: 7}, {label: 8}];
    $scope.slickConfig3Loaded = true;
    $scope.slickConfig3 = {
      method: {},
      dots: true,
      infinite: false,
      speed: 300,
      slidesToShow: 4,
      slidesToScroll: 4,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    };

    //====================================
    // Slick 4
    //====================================
    $scope.number4 = [{label: 225}, {label: 125}, {label: 200}, {label: 175}, {label: 150}, {label: 180}, {label: 300}, {label: 400}];
    $scope.slickConfig4Loaded = true;
    $scope.updateNumber4 = function () {
      $scope.slickConfig4Loaded = false;
      $scope.number4[2].label = 123;
      $scope.number4.push({label: Math.floor((Math.random() * 10) + 100)});
      $timeout(function () {
        $scope.slickConfig4Loaded = true;
      });
    };
    $scope.slickConfig4 = {
      method: {},
      dots: true,
      infinite: true,
      speed: 300,
      slidesToShow: 1,
      centerMode: true,
      variableWidth: true
    };


  });