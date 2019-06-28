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

var re_password = /^.{6,16}$/;
var api = '/admin?q=json';

var app = new Vue({
	el: "#adminpanel",
	data:{
		userlist: [],
		maxLength: 0,
		operation: '',
		user: {
			uid: 0,
			username: '',
			password: '',
			nickname: '',
			email: '',
		},
		error_msg: '',
		curPage: 1,
		index: 1,
		maxPage: 1,
		keyword: '',
		tmpUserlist: [],
	},
	created: function(){
		this.doRetrieve();
	},
	watch:{
		keyword: function(){
			let self = this;
			let keyword = this.keyword;
			let arr = this.tmpUserlist.filter( function(user){
				return user.username.includes(keyword) === true || user.nickname.includes(keyword) === true || user.email.includes(keyword) === true;
			})
			let len = arr.length;
			this.maxLength = len;
			this.maxPage = parseInt(len / 5) + 1;
			this.userlist = arr;
		}
	},
	methods:{
		doSearch: function(){
			this.userlist = [];
			for( let i = 0; i < this.maxLength; i++ ){
				let user = this.tmpUserlist[i];
				if( user.username.includes(this.keyword) ){
					this.userlist.push(this.tmpUserlist[i]);
				}
			}
			this.maxLength = this.userlist.length;
			this.maxPage = parseInt(this.maxLength) + 1;
		},
		doCancel: function(){
			this.keyword = '';
			this.userlist = this.tmpUserlist;
			this.maxLength = this.userlist.length;
			this.maxPage = parseInt(this.maxLength / 5) + 1;
		},
		doCreate: function(){
			
		},
		doRetrieve: function(){
			let self = this;
			axios.get(api)
				.then( function(resp){
					self.userlist = resp.data;
					self.tmpUserlist = resp.data;
					self.maxLength = self.userlist.length;
					self.maxPage = parseInt((self.maxLength + 4) / 5);
				});
		},
		openModal: function(index, operation){
			let user = this.userlist[index];
			this.index = index;
			this.user.username = user.username;
			this.user.nickname = user.nickname;
			this.user.email = user.email;
			this.operation = operation;
		},
		doRequest: function(){
			if( this.operation === '修改' ){
				this.doUpdate();
			}
			else if( this.operation === '删除' ){
				this.doDelete();
			}
		},
		doUpdate: function(){
			if( this.user.password != '' && re_password.test(this.user.password) === false ){
				this.error_msg = '密码不符合规则';
			}
			else{
				this.userlist[this.index].nickname = this.user.nickname;
				this.userlist[this.index].email = this.user.email;
				let self = this;
				axios.put(api, self.user)
					.then( function(resp) {
						console.log(resp.data);
						if( resp.data != 'ok' ){
							self.error_msg = '操作失败';
						}
					});
			}
		},
		doDelete: function(){
			this.userlist.splice(this.index, 1);
			this.maxLength--;
			let self = this;
			axios.delete(api + '&username=' + self.user.username)
				.then( function(resp) {
					console.log(resp.data);
					if( resp.data != 'ok' ){
						self.error_msg = '操作失败';
					}
				});
		},
		getIndexlist: function(){
			let indexlist = [];
			let begin = (this.curPage - 1) * 5;
			for( let offet = 0; offet < 5; offet++ ){
				let index = begin + offet;
				if( index >= this.maxLength ){
					break;
				}
				indexlist.push(index);
			}
			return indexlist;
		},
		addPage: function(){
			if( this.curPage < this.maxPage ){
				this.curPage++;
			}
		},
		decPage: function(){
			if( this.curPage > 1 ){
				this.curPage--;
			}
		}
	}
})