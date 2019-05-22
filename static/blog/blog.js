'use strict';

var myheader = new Vue({
	el: '#myheader',
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
	}
});

var app = new Vue({
	el: '#blog',
	data: {
		pathname: '',
		totalPage: 2,
		post_list: [],
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
		this.pathname = document.location.pathname;
		this.get_post_list();
	},
	methods: {
		get_post_list: function(){
			let self = this;
			let APIjson = `${self.pathname}?q=json`;
			axios.get(APIjson)
				.then(function(resp){
					self.post_list = resp.data;
				});
		}
	}
})
