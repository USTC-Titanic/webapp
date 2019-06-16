'use strict';

var myheader = new Vue({
	el: "#myheader",
	data:{
		nickname: '',
	},
	created: function(){
		let cookie = document.cookie;
		let cookie_list = cookie.split(';')
		for(let item of cookie_list){
			if( item.indexOf('nickname=') != -1 ){
				this.nickname = item.split('=')[1];
			}
		}
	},
})
