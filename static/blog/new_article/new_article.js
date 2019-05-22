'use strict';

var app = new Vue({
	el: '#editor',
	data: {
		pathname: '',
		title: '',
		content: '',
	},
	created: function(){
		this.pathname = document.location.pathname;
	},
	methods: {
		do_submit: function(){
			let self = this;
			let article = {
				'title': self.title,
				'content': self.content,
			};
			let APIpost = `${self.pathname}`;
			console.log(APIpost)
			axios.post(APIpost, article)
				.then( function(resp){
				    if( resp.data == 'ok' ){
				        window.location.replace('/blog')
				    }
				})
		}
	}
})