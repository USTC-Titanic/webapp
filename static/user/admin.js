'use strict';

var re_username = /^[a-zA-Z0-9]{3,16}$/;
var re_password = /^.{6,16}$/;
var api = '/admin?q=json';

var app = new Vue({
	el: "#adminpanel",
	data:{
		userlist: [],
		operation: '',
		user: {},
		index: 0,
		error_msg: '',
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
				});
		},
		openModal: function(index, operation){
			this.index = index;
			this.user = this.userlist[index];
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
			let self = this;
			axios.put(api)
				.then( function(resp) {
					console.log(resp.data);
					if( resp.data != 'ok' ){
						self.error_msg = '操作失败';
					}
					else{
						// self.userlist[self.index] = self.user;
					}
				});
		},
		doDelete: function(){
			let self = this;
			axios.delete(api)
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
	}
})