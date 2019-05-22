'use strict';

var myheader = new Vue({
	el: "#myheader",
	data:{
		username: '',
	},
    created: function(){
		let cookie = document.cookie;
		let cookie_list = cookie.split(';')
		for(let item of cookie_list){
			if( item.indexOf('username=') != -1 ){
				this.username = item.split('=')[1];
			}
		}
	},
})