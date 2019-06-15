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

var main = new Vue({
	el: "#myprofile",
	data:{
		username: '',
		old_password: '',
		password: '',
		verify: '',
		error_msg: '',
	},
	created: function(){
		let cookie = document.cookie;
		let cookie_list = cookie.split(';');
		for( let item of cookie_list ){
			if( item.indexOf('username') != -1 ){
				this.username = item.split('=')[1];
				break;
			}
		}
	},
	methods: {
		doSubmit: function(){
			if( re_password.test(this.old_password) === false ){
				this.error_msg = '旧密码不符合规则';
				this.old_password = '';
				document.getElementsByTagName('input')[1].focus();
			}
			else if( re_password.test(this.password) === false ){
				this.error_msg = '新密码不符合规则';
				this.password = '';
				document.getElementsByTagName('input')[2].focus();
			}
			else if( this.password != this.verify ){
				this.error_msg = '两次输入的密码不一致';
				this.verify = '';
				document.getElementsByTagName('input')[3].focus();
			}
			else{
				this.error_msg = '请稍等...';
				let form = {
					username: this.username,
					old_password: this.old_password,
					password: this.password,
				};
				let api = '/profile?q=json';
				let self = this;
				axios.put(api, form)
					.then(function(resp){
						if( resp.data === 'ok' ){
							self.error_msg = '修改成功';
							window.location.replace('/');
						}
						else{
							self.error_msg = '密码错误';
						}
					});
			}
		}
	},
})