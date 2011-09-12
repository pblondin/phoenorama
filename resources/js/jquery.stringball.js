/*

	StringBall ver2.1 for jQuery(gt Ver 1.3.2) 
	Developped  by Coichiro Aso
	Copyright Codesign.verse 2009　http://codesign.verse.jp/
	Licensed under the MIT license:http://www.opensource.org/licenses/mit-license.php/
*/

(function($){

	$.fn.stringball=function(options){

		var defaults={	
			camd:1000,
			radi:250,
			speed:40,
			framerate:30
		};

	var options = $.extend(defaults, options);

	var target=$(this);
	var elem=$("li" ,target);
	var scrz=500;
	var radi=options.radi;
	var camd=options.camd;
	var speed=options.speed;
	var frn=Math.floor(1000/options.framerate);
	var elemLength=elem.length;
	
	var xs=[];
	var ys=[];
	var zs=[];
	var fw=[];
	var fh=[];
	
/*	
	var axang=0;
	var accx=0;
	var accy=0;
	var rotec=0;
	var rotes=0;
*/	
	var ac=0;
	var as=0;
	var roteang=0;
	var looptimer=0;

	var itxpos = target.offset().left;
	var itw = target.width();
	var itypos=target.offset().top;
	var ith=target.height();

		function setini(){
			var anga=0;
			var angb=0;
			for(i=0;i<elemLength;i++){
			anga= Math.acos((2 * (i + 1) - 1) / elem.length - 1);
			angb= Math.sqrt(elem.length * Math.PI) * anga;
			fw[i]=$(elem[i]).width()/2;
			fh[i]=$(elem[i]).height()/2;
			xs[i]=radi*Math.cos(angb)*Math.sin(anga);
			ys[i]=radi*Math.cos(anga);
			zs[i]=radi*Math.sin(angb)*Math.sin(anga);
			
			/*
			elem[i].xpos=radi*Math.cos(angb)*Math.sin(anga);
			elem[i].zpos=radi*Math.cos(anga);
			elem[i].ypos=radi*Math.sin(angb)*Math.sin(anga);
			*/
			}
		}

		function setpos(){

			var rotec=Math.cos(roteang);
			var rotes=Math.sin(roteang);

			
			for(i=0;i<elemLength;i++){
				
				var xpos=xs[i]*(ac*ac*(1-rotec)+rotec)+ys[i]*(ac*as*(1-rotec))-zs[i]*(as*rotes);
				var ypos=xs[i]*(ac*as*(1-rotec))+ys[i]*(as*as*(1-rotec)+rotec)+zs[i]*(ac*rotes);
				var zpos=xs[i]*as*rotes-ys[i]*ac*rotes+zs[i]*rotec;
				
				xs[i]=xpos;
				ys[i]=ypos;
				zs[i]=zpos;
				
				var scale=scrz/(camd-zpos);

				var myx=xpos*scale+(itw>>1)-fw[i] | 0;
				var myy=ypos*scale+(ith>>1)-fh[i] | 0;
				var myscale=scale*100 | 0 ;
				
				elem[i].style.left=myx+"px";
				elem[i].style.top=myy+"px";
				elem[i].style.fontSize=myscale+"%";
				elem[i].style.opacity=scale;
	
			}
			return false;
		}
		
		setini();
		setpos();
		
		target.hover(
		function(){

			clearInterval(looptimer);
			looptimer=setInterval(setpos,frn);
		},
		function(){
			clearInterval(looptimer);
		});
		
		target.mousemove(function(e){
				
			var accx = (e.pageX-itxpos-(itw>>1))/itw;
			var accy = (e.pageY-itypos-(ith>>1))/ith;			
			roteang=(Math.max(Math.abs(accx),Math.abs(accy)))/100*speed;			
			var axang=Math.PI/2+Math.atan2(accy,accx);			
			ac=Math.cos(axang);
			as=Math.sin(axang);
			
		});

	}
})(jQuery);

