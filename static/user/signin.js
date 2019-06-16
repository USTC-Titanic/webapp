'use strict';

var myheader = new Vue({
	el: '#myheader',
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
	}
});

var re_username = /^[a-zA-Z0-9]{3,16}$/;
var re_password = /^.{6,16}$/;

var app = new Vue({
	el: "#signin",
	data:{
		username: '',
		password: '',
		error_msg: '',
	},
	created: function(){
		let cookie = document.cookie;
		let cookie_list = cookie.split(';');
		for(let item of cookie_list){
			if( item.indexOf('username=') != -1 ){
				this.username = item.split('=')[1];
				break;
			}
		}
	},
	methods:{
		do_signin: function() {
			if( re_username.test(this.username) === false ){
				this.error_msg = '用户名不符合规则';
				this.username = '';
				document.getElementsByTagName('input')[0].focus();
			}
			else if( re_password.test(this.password) === false ){
				this.error_msg = '密码不符合规则';
				this.password = '';
				document.getElementsByTagName('input')[1].focus();
			}
			else{
				this.error_msg = '请稍等...';
				var self=this;
				var form= {
					username: self.username,
					password: self.password,
				}
				var api_post = '/signin';
				axios.post(api_post, form)
				.then( function(resp){
					if( resp.data === 'succ' ){
						self.error_msg = '登录成功';
						window.location.replace('/');
					}
					else if( resp.data === 'error' ){
						self.error_msg = '用户名或密码错误';
					}
					else{
						self.error_msg = '请重试';
					}
				})
			}
		},
	}
})