'use strict';

var app = new Vue({
	el: '#blog',
	data: {
		pathname: '',
		totalPage: 2,
		post_list: []
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.get_post_ist();
	},
	methods: {
		get_post_ist: function(){
			var self = this;
			var APIjson = `${self.pathname}?q=json`;
			axios.get(APIjson)
				.then(function(resp){
					self.post_list = resp.data;
				});
		}
	}
})
