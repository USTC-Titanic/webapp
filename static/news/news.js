'use strict';

var app = new Vue({
	el: '#newspage',
	data: {
		src_netease: [],
		src_36kr: [],
		src_huxiu: [],
		news_list: [],
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.get_news_list();
	},
	filters: {
		get_time_delay: function(date){
			var past = new Date(date);
			var now = new Date();
			var sec = (now - past) / 1000;
			var minute = Math.floor( sec / 60 );
			var hour = Math.floor( minute / 60 );
			var day = Math.floor( hour / 24 );
			if( day > 0 ){
				return day + 'd ago';
			}
			else if( hour > 0 ){
				return hour + 'h ago';
			}
			else{
				return minute + 'min ago';
			}
		}
	},
	methods: {
		get_news_list: function(){
			var self = this;
			var API_36kr = `${self.pathname}?q=json&src=36kr`;
			axios.get(API_36kr)
				.then( function(resp) {
					self.src_36kr = resp.data;
					self.news_list = resp.data;
				});
			var API_netease = `${self.pathname}?q=json&src=netease`;
			axios.get(API_netease)
				.then( function(resp) {
					self.src_netease = resp.data;
				});
		},
	}
})