'use strict';

var app = new Vue({
	el: '#infosheet',
	data:
	{
		pathname: '',
		Pclass: '',
		Name: '',
		Sex: '',
		Age: '',
		SibSp: '',
		Parch: '',
		form: '',
		response: '',
	},
	created: function()
	{
		this.pathname = document.location.pathname;
		this.redirectPath = document.location.search;
	},
	methods:
	{
		do_submit_passenger_info: function()
		{
			var self = this;
			self.form = {
				Pclass: self.Pclass,
				Name: self.Name,
				Sex: self.Sex,
				Age: self.Age,
				SibSp: self.SibSp,
				Parch: self.Parch,
			}
			var APIpost = `${self.pathname}${self.redirectPath}`;
			console.log(APIpost);

			axios.post(APIpost, self.form)
				.then(function(resp){
					console.log(resp);
					self.response = '生存指数: ' + resp.data;
				})
		}
	}
})
