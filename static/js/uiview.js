var uiView = angular.module('uiView',['ui.router','slickCarousel','ngAnimate'])

.config(['$urlRouterProvider','$stateProvider',function($urlRouterProvider,$stateProvider)
 {
		 $stateProvider
      .state('tab1',
      {
        url : "/tab1",
		views: {	/*,'offer_cart': {
						//templateUrl: 'static/template/_u_offer.html',
						templateUrl: 'static/template/_u_offer_v2.html',
						controller: 'myController'
									}*/
						
						'product': {
						templateUrl: 'static/template/_u_product_locks.html'
						//,controller:'SlickController',
								  }		
						/**/
						,'gravs': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_gravs_1.html',
						controller:'myGravs',
								  }
						,'examples': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_examples_1.html',
						controller:'myExamp',
								  }
			}
        
      })
      .state('tab2',
      {
        url : "/tab2",
		views: {	/*,'offer_cart': {
						//templateUrl: 'static/template/_u_offer.html',
						templateUrl: 'static/template/_u_offer_v2.html',
						controller: 'myController'
									}*/
						
						'product': {
						templateUrl: 'static/template/_u_product_glasses.html'
						//,controller:'SlickController',
								  }		
						/**/
						,'gravs': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_gravs_1.html',
						controller:'myGravs',
								  }
						,'examples': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_examples_1.html',
						controller:'myExamp',
								  }
			}
        
      });
      
		$urlRouterProvider.otherwise('/');
		//$urlRouterProvider.when('main','/main123').otherwise('/12');
		var homepage={
			url:'/',
				views: {
						/*'glasses': {
						templateUrl: 'static/template/_u_glasses.html',
						
						controller:'myController',
								  }
						,'content': {
						templateUrl: 'static/template/_u_bottles.html',
						controller: 'myController'
									},
						'offer': {
						templateUrl: 'static/template/_u_offer.html',
						//templateUrl: 'static/template/_u_offer_v1.html',
						controller: 'myController'
									},*/
						'offer_cart': {
						//templateUrl: 'static/template/_u_offer.html',
						templateUrl: 'static/template/_u_offer_v2.html',
						//controller: 'SlideAnimation'
									},
						'product': {
						templateUrl: 'static/template/_u_product_glasses.html'
						//,controller:'SlickController',
								  },
						'gravs': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_gravs_1.html',
						controller:'myGravs',/**/
								  }
						,'examples': {
						//templateUrl: 'static/template/_u_grav.html',
						templateUrl: 'static/template/_u_examples_1.html',
						controller:'myExamp',/**/
								  }
						},
				//templateUrl: 'static/page1.html',
				//controller:'SlickController'
				//controllerAs:'home Ctrl',
			/*	
			url:'/glasses?/',
				views: {
						
						'offer_cart': {
						//templateUrl: 'static/template/_u_offer.html',
						templateUrl: 'static/template/_u_offer_v2.html',
						controller: 'myController'
									}
						
						},
				controllerAs:'home Ctrl'*/
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
		$stateProvider.state("home",homepage);
		//$stateProvider.state("offer_cart",offer_cart);
		//$stateProvider.state("home_glasses",home_glasses);
		//$stateProvider.state("home_locks",home_locks);
		//$stateProvider.state("IdGlasses",IdGlasses)
		$stateProvider.state("home-glasses",slick)
		//$stateProvider.state("home",slick)
		//.state("home-glasses",{url:'/glasses',templateUrl: 'static/page2.html',controller:'homeController',controllerAs:'home Ctrl'})
		.state("students",students);
		
		//.state("studentDetails",{url:'/students/:id',templateUrl: 'static/page2.html',controller:'homeController',controllerAs:'home Ctrl'});
		//$routeProvider.when('/page1',{templateUrl: 'static/page1.html'});
		//$routeProvider.when('/page2',{templateUrl: 'static/page2.html'});
		//$routeProvider.otherwise('/',{redirectTo:'/home'});	
		
		//$locationProvider.html5Mode({enabled: true,requireBase:false})
		
		
		document.addEventListener('mousewheel', null, { passive: true });
		//$urlRouterProvider.otherwise('/');
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

//

//
//$scope.gravs_count1=[0,1,2,3,4,5]
$scope.gravs_count=Array(6)  //Колличество шаблонов гравировки в type_index_shablon - используется в _u_gravs_1.html(контролер -myController)




function  workLoad() {

  $.ajaxSetup({ cache: true });

  $('.thumb-container label').click(function() {
    var $this = $(this),
        newTitle = $this.find('strong').text(),
        spinner = '<div class="loader">Loading...</div>',
        url = $this.find('.thumb-unit').data('url');

    $('.project-load').html(spinner).load(url);
    $('.project-title').text(newTitle);
  });

}



  
  
});

uiView.controller('myGravs', function($scope, $http){
   

$http({
    method: 'get', 
    url: '/main_view_gravs'
}).then(function (response) {
    console.log(response, 'main_view_gravs -res');
    data = response.data;
	$scope.gravs = response.data;
	//$scope.gravs_count=Array(response.data.length);
},function (error){
   console.log(error, 'main_view_gravs -can not get data.');
})



//$scope.gravs_count1=[0,1,2,3,4,5]
$scope.gravs_count=Array(6)  //Колличество шаблонов гравировки в type_index_shablon - используется в _u_gravs_1.html(контролер -myController)



});

uiView.controller('myExamp', function($scope, $http){
   
$http({
    method: 'post', 
    url: '/main_view_examples'
}).then(function (response) {
    console.log(response, 'main_view_examples -res');
    data = response.data;
	$scope.examples = response.data;
	//$scope.gravs_count=Array(response.data.length);
},function (error){
   console.log(error, 'main_view_examples -can not get data.');
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

uiView.controller('SlideAnimation', function($rootScope, $window, $scope){
 
  /**/
  $rootScope.$on('$stateChangeStart', function(){
    $scope.slide = $scope.slide || 'slide-left'
	console.log('$scope.slide ='+$scope.slide);
	
  });
  
 
  
});

uiView.controller('SlickController', function ($scope, $timeout,$window,$rootScope) {
    
	$(function(){
		

  
/*
	$('body').on('click', '#close-popup,#magnify,#overlay,#overlay_offer', function(event) {
	event.preventDefault();

    $('#overlay, #overlay_offer, #magnify, #magnify_offer').fadeOut('fast', function() {
      $('#close-popup, #magnify, #overlay').remove();
	  });	  
  });
 */ 
 /* 
   $rootScope.$on('$stateChangeStart', function(){
    $scope.slide = $scope.slide || 'slide-left'
  });*/
  
	// Всплывающие окна
 $('body').on('click', '#close-popup,#magnify,#overlay,#a-popover-close', function(event) {
	event.preventDefault();
    $('#overlay,#magnify').fadeOut('fast', function() {
      $('#close-popup, #magnify').remove();
	  //$('.a-color-price').remove();
	    
	  });
	
	if (typeof statOfferView === 'undefined' || !statOfferView){document.body.style.overflow = '';}
	  //if (!statOfferView) {document.body.style.overflow = '';console.log('statOfferView!!!='+statOfferView);}
	//document.body.style.overflow = '';
	//$scope.statview=true
	
  });
  
 $('body').on('click', '#overlay_offer,#a-popover-close', function(event) {
	event.preventDefault();
    $('#overlay_offer,#magnify_offer').fadeOut('fast', function() {
	$('#offer_id').remove();	
	//$('.a-color-price').remove();
	//console.log('GravID='+GravID);
	//$scope.id='';
	 //$('#offer_button').fadeIn('fast');
			 //$('#cart_button').fadeOut('fast');
			 //GravID='';
	  //$scope.id='';
	document.body.style.overflow = '';	 
	statOfferView=false;
	console.log('statOfferView='+statOfferView)	;
	  });	  
  });
  //*******
});


//Validate form
    //$scope.fname = 'M.kumar';
	//$scope.name = '10021';
     //$scope.lname1 = 'Rai';
     //$scope.address = 'xxx xxx xxx';
    //$scope.email = 'xxx@gmail.com';

		
	$scope.setCurrentPos = function($event) {
			$scope.currentPosY = $event.offsetY;
			$scope.currentPosX = $event.offsetX;

};

	
//Всплывающие изображение
		$scope.ctrlClickHandler = function(obj){
			
			console.log($scope.currentPos)	;
			console.log($scope.currentPosY)	;
			console.log(obj.offsetY - $scope.currentPosY)
			console.log($scope.currentPosY-obj.offsetY)
			console.log(obj.offsetY)	;
			
		if ((obj.offsetY == $scope.currentPosY || (obj.offsetY - $scope.currentPosY)<20) && obj.offsetX == $scope.currentPosX ) {
	
			var element = $(obj.currentTarget).attr("src")
    $('body').append('<div id="overlay"></div><div id="magnify"><img src="'+element+'"><div id="close-popup"><i></i></div></div>');
	
	console.log($('#magnify').outerWidth());
	$('#magnify').css({
	    left: ($(document).width() - $('#magnify').outerWidth())/2,
		//left: window.pageXOffset +($(document).width() - $('#magnify').outerWidth())/2,
	     //top: ($(document).height() - $('#magnify').outerHeight())/2 
            //top: ($(window).height() - $('#magnify').outerHeight())/2 +$(window).height()/15
		  //top: window.scrollY + 50
		  top: window.pageYOffset + 50
		  
	  });
    
	  
    $('#overlay, #magnify').fadeIn('fast');
	document.body.style.overflow = 'hidden';
	} else {}
		};	
		/*Проверка элемента в корзине*/
		
		/*Получения ID*/
		$scope.inOfferID = function(a){
					//return  ngCart.getItemById(GravID);
				  //console.log('$scope.id='+$scope.id);
					
						//$scope.attrs.id=GravID;
					//console.log($scope.attrs.id); //GravID получается в ctrlClickHandlerOffer
					/*Если данные валидны-*/
					console.log('a='+a);
					if (!a) {
					$scope.id=GravID;
					console.log('TESTTT='+GravID);
					//$scope.id=GravID;
					$scope.name=GlassID;
					$scope.price=PriceID;
					$scope.text=TextID;
					
					/**/
					//$scope.text1='Proverka!';
					$scope.offer_names=document.getElementById("offer_names").value;
					$scope.offer_date=document.getElementById("offer_date").value;
					//document.getElementById("ac-atc-price-value").value=PriceID;
					
					//$scope.name=a;
					//$scope.id=a;
					//$('#offer_button').fadeOut('fast');
					$('#cart_button').fadeIn('fast');
					$('#offer_sub_button').fadeOut('fast');
					}
					//console.log(ngCart.getItemById(GravID));
					//console.log('inCart='+ngCart.getItemById(attrs.id));
					if (a=='price') {
						if (typeof PriceID === 'undefined') {return '';} else {return PriceID;}
					} 
					if (a=='id') {
						if (typeof GravID === 'undefined') {return '';} else {return GravID;}
					}
					if (a=='img') {
						if (typeof ImgID === 'undefined') {return '';} else {return '/static/'+ImgID;}
					}
					if (a=='imgg') {
						if (typeof Img_gID === 'undefined') {return '';} else {return '/static/'+Img_gID;}
					}
					if (a=='imgr') {
						if (typeof Img_rID === 'undefined') {return '';} else {return '/static/'+Img_rID;}
					}
					//if (a=='price') {return PriceID;} else {return GravID;}
                    
						
                };
		/*Проверка что элемент уже добавлен*/
		$scope.OfferValid = function(a){

					if (typeof GravID === 'undefined') {
					console.log('GravID=undefined') } else {console.log('GravID='+GravID);}

					// OfferID создается в ctrlClickHandlerOffer; получает значение в (ngCart.js)addItem; обнуляется в (ngCart.js)removeItemById. 
					if(typeof GravID === 'undefined') {return(false)} else{return(a==OfferID);}	
						
                };
//Всплывающие окно заказа
		$scope.ctrlClickHandlerOffer = function(obj,id,name,price,text,img,imgg,imgr){
			//console.log($scope.name);

//console.log($scope.name);			
			console.log(obj.offsetY)	;
	if (1 == 1) {
			console.log(id)
			var element = $(obj.currentTarget).attr("src")
			 //GravID = $(obj.currentTarget).attr("id")
			 GravID = id
			 GlassID =name
			 PriceID=price
			 TextID=text
			 OfferID=''
			 ImgID=img
			 Img_gID=imgg
			 Img_rID=imgr
			 statOfferView=true
			 console.log('statOfferView='+statOfferView)	
			 console.log('GravID ='+GravID)
			 $('#offer_sub_button').fadeIn('fast');
			 //$('#offer_button').fadeOut('fast');
			 //$('#cart_button').fadeOut('fast');
			 //GlassID = $(obj.currentTarget).attr("name")
			//GlassID = id
			 
    //$('body').append('<div id="overlay"></div><div id="magnify_offer" style="background-color: white;"><img src="http://127.0.0.1:5000/static/source/glasses/G06_big_1.png"><form ng-controller="SlickController" name="myForm" novalidate><p>First Name:<br><input type="text" name="fname" placeholder="Виктор + Елена" ng-model="fname" required><span style="color:red" ng-show="myForm.fname.$dirty && myForm.fname.$invalid"><span ng-show="myForm.fname.$error.required">First name is required!!!.</span></span></p><p>Last Name :<br><input type="text" name="lname" ng-model="lname" required><span style="color:red" ng-show="myForm.lname.$dirty && myForm.lname.$invalid"><span ng-show="myForm.lname.$error.required">Last name is required.</span></span></p><p>Address :<br><input type="text" name="address" ng-model="address" required><span style="color:red" ng-show="myForm.address.$dirty && myForm.address.$invalid"><span ng-show="myForm.address.$error.required">Username is required.</span></span></p><p>Email:<br><input type="email" name="email" ng-model="email" required><span style="color:red" ng-show="myForm.email.$dirty && myForm.email.$invalid"><span ng-show="myForm.email.$error.required">Email is required.</span><span ng-show="myForm.email.$error.email">Invalid email address.</span></span></p><p><input type="submit" ng-disabled="myForm.fname.$dirty && myForm.fname.$invalid || myForm.lname.$dirty && myForm.lname.$invalid || myForm.address.$dirty && myForm.address.$invalid || myForm.email.$dirty && myForm.email.$invalid"></p></form>	<div id="close-popup"><i></i></div></div>');
	
	 //$('body').append('<div id="overlay"></div><div id="magnify_offer"><div ui-view="examples"></div><div id="close-popup"><i></i></div></div>');
	 $('#magnify_offer').append('<div id="offer_id">GravID='+GravID+'<p>GlassID='+GlassID+'<p>PriceID='+PriceID+'</div>');
	  //$('.a-font_price').append('Price:'+PriceID+'</div>');
	 //$('.a-span7').append('<span id="ac-atc-price-value" class="a-color-price">'+PriceID+'₽</span>');
	 
	 //document.getElementsByTagName('ngcart-addtocart')[0]['id']=GravID;
	 
	
   $('#magnify_offer').css({
	    left: ($(document).width() - $('#magnify_offer').outerWidth())/2,
		//left: window.pageXOffset +($(document).width() - $('#magnify').outerWidth())/2,
	     //top: ($(document).height() - $('#magnify').outerHeight())/2 
            //top: ($(window).height() - $('#magnify').outerHeight())/2 +$(window).height()/15
		  //top: window.scrollY + 50
		  top: window.pageYOffset + 50
		  
	  });
	  
	  
    $('#overlay_offer, #magnify_offer').fadeIn('fast');
	//$('#cart_button').fadeOut('fast');
	document.body.style.overflow = 'hidden';
				 
	} else {}
	
		};	
		

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
	  /*lazyLoad: 'progressive',
	  lazyLoaded: 'image',*/
      infinite: true,
      autoplaySpeed: 3300,
      slidesToShow: 3,
      slidesToScroll: 3,
      method: {},
	  centerMode: true,
	  centerPadding: '50px',
	  variableWidth: true,
			rtl: false,
	  responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true,
			centerPadding: '40px',
			variableWidth: true
          }
        },
	/*	{
          breakpoint: 900,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true,
			centerPadding: '40px',
			variableWidth: false
          }
        },*/
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
			variableWidth: true,
			centerMode: true,
			centerPadding: '0px'
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
			centerMode: true,
	  centerPadding: '0px',
	  variableWidth: true
          }
        }
      ]
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