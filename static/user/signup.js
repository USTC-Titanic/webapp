// MVC, View 和 Control 分开, 逻辑不要全部混在 html 里面
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

var re_username = /^[a-zA-Z0-9]{3,16}$/;
var re_password = /^.{6,16}$/;
var re_email = /^[\S]+@[\S]+.[\S]+$/

// for( var i = 0; i < 4; i++ ){
	// https://stackoverflow.com/questions/195951/how-to-change-an-elements-class-with-javascript
	// document.getElementsByTagName('input')[i].classList.add('form-control');
// }

var app = new Vue({
	el: '#signup',
	data:{
		username: '',
		password: '',
		verify: '',
		email: '',
		error_msg: '',
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
	methods:{
		do_signup: function(){
			// 检查用户名是否合法
			if( re_username.test(this.username) === false ){
				this.error_msg = '用户名不符合规则';
				this.username = '';
				document.getElementsByTagName('input')[0].focus();
			}
			// 检查密码是否合法
			else if( re_password.test(this.password) === false ){
				this.error_msg = '密码不符合规则';
				this.password = '';
				document.getElementsByTagName('input')[1].focus();
			}
			// 检查密码是否相同
			else if( this.password != this.verify ){
				this.error_msg = '两次输入的密码不一致';
				this.verify = '';
				document.getElementsByTagName('input')[2].focus();
			}
			// 检查邮箱
			else if( re_email.test(this.email) === false )
			{
				this.error_msg = '邮箱不符合规则';
				this.email = '';
				document.getElementsByTagName('input')[3].focus();
			}
			else{
				this.error_msg = '请稍等...';
				var self = this;
				var form = {
					username: self.username,
					password: self.password,
					email: self.email,
				};
				var api_post = '/signup'
				axios.post(api_post, form)
				.then(function(resp){
					console.log(resp.data);
					if( resp.data === 'taken' ){
						self.error_msg = '用户名已被使用';
						self.username = '';
					}
					else if( resp.data == 'succ' ){
						self.error_msg = '注册成功';
						self.resp = resp
						window.location.replace('/');
					}
					else if( resp.data == 'errorio' ){
						self.error_msg = '网络繁忙请稍后再试';
					}
					else if( resp.data === 'error' ){
						self.error_msg = '注册信息格式错误';
						self.username = '';
						self.password = '';
						self.verify = '';
						self.email = '';
					}
				})
			}
		}
	}
})
