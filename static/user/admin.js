'use strict';

var re_username = /^[a-zA-Z0-9]{3,16}$/;
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
			nickname: '',
			email: '',
		},
		error_msg: '',
		curPage: 1,
		index: 1,
		maxPage: 1,
	},
	created: function(){
		this.doRetrieve();
	},
	methods:{
		doCreate: function(){
			
		},
		doRetrieve: function(){
			let self = this;
			axios.get(api)
				.then( function(resp){
					self.userlist = resp.data;
					self.maxLength = self.userlist.length;
					self.maxPage = parseInt(self.maxLength / 5) + 1;
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
			let user = this.userlist[this.index];
			let self = this;
			axios.put(api, self.user)
				.then( function(resp) {
					console.log(resp.data);
					if( resp.data != 'ok' ){
						self.error_msg = '操作失败';
					}
					else{
						user.nickname = self.user.nickname;
						user.email = self.user.email;
					}
				});
		},
		doDelete: function(){
			let self = this;
			axios.delete(api + '&username=' + self.user.username)
				.then( function(resp) {
					console.log(resp.data);
					if( resp.data != 'ok' ){
						self.error_msg = '操作失败';
					}
					else{
						self.userlist.splice(self.index, 1);
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