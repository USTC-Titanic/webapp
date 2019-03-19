'use strict';

var re_username = /^[a-zA-Z0-9]{3,16}$/;
var re_password = /^.{6,16}$/;

var app = new Vue({
	el: "#signin",
	data:{
		username: '',
		password: '',
		error_msg: '',
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
					if(  resp.data === 'sigin error' ){
						self.error_msg = '用户名或密码错误';
					}
					else{
						self.error_msg = '登录成功';
						window.location.replace('/');
					}
				})
			}
		},
	}
})