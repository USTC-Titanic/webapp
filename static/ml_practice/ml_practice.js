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

var mycontent1 = "The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.\
\
One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.\
\
In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.\
\
Practice Skills\
Binary classification\
Python and R basics\
\
RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean in 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the estimated 2,224 passengers and crew aboard, more than 1,500 died, making it one of modern history's deadliest commercial marine disasters during peacetime. RMS Titanic was the largest ship afloat at the time she entered service and was the second of three Olympic-class ocean liners operated by the White Star Line. She was built by the Harland and Wolff shipyard in Belfast. Thomas Andrews, chief naval architect of the shipyard at the time, died in the disaster.[4]";

var app = new Vue({
	el: '#practice',
	data:{
		article_number: 1,
		mycontent1: mycontent1,
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
	created: function(){
		this.pathname = document.location.pathname;
		this.redirectPath = document.location.search;
	},
	methods:{
		do_submit_passenger_info: function(){
			var self = this;
			self.form = {
				Pclass: self.Pclass,
				Name: self.Name,
				Sex: self.Sex,
				Age: self.Age,
				SibSp: self.SibSp,
				Parch: self.Parch,
			}
			var APIpost = `/predict`;
			console.log(APIpost);

			axios.post(APIpost, self.form)
				.then(function(resp){
					console.log(resp);
					self.response = '生存指数: ' + resp.data;
				})
		}
	}
})

// echarts visualization



var mychart1 = echarts.init(document.getElementById('mychart1'));
var option = {
	title:{
		text: '生存率',
		x: 'center',
	},
	tooltip:{
		trigger: 'item',
		formatter: '{c}%'
	},
	series:[{
		name: '生存率',
		type: 'pie',
		// 半径radius 是 min(width, heigh) 的 60%
		radius: '50%',
		// 也可以直接输入绝对值
		data: [
			{value: 38.38, name: '生存', itemStyle:{color: '#34c726'}},
			{value: 61.62, name: '遇难', itemStyle:{color: '#767676'}},
		]
	}],
};
mychart1.setOption(option);



var mychart2 = echarts.init(document.getElementById('mychart2'));
option = {
	title:{
		text: '性别与生存率的关系'
	},
	tooltip:{
		trigger: 'item',
		formatter: '{c}'
	},
	legend:{
		data: ['生存', '遇难'],
	},
	xAxis:{
		data: ['男性', '女性'],
	},
	yAxis:{
	},
	series:[
		{
			name: '生存',
			type: 'bar',
			data: [110, 230],
			barWidth: 50,
			itemStyle:{color: '#34c726'},
			barGap: "10%",
		},
		{
			name: '遇难',
			type: 'bar',
			data: [470, 90],
			barWidth: 50,
			itemStyle:{color: '#767676'},
			barGap: "10%",
		},

	]
};
mychart2.setOption(option);

var mychart3 = echarts.init(document.getElementById('mychart3'));
option = {
	title:{
		text: '船舱等级与生存率的关系',
		x: 'center',
	},
	tooltip:{
		trigger: 'item',
		formatter: '{c}'
	},
	legend:{
		data: ['生存', '遇难'],
		x: '75%',
	},
	xAxis:{
		data: ['一等舱', '二等舱', '三等舱'],
	},
	yAxis:{
	},
	series:[
		{
			name: '生存',
			type: 'bar',
			data: [140, 90, 115],
			barWidth: 50,
			itemStyle:{color: '#34c726'},
			barGap: "10%",
		},
		{
			name: '遇难',
			type: 'bar',
			data: [80, 100, 375],
			barWidth: 50,
			itemStyle:{color: '#767676'},
			barGap: "10%",
		}
	]
};
mychart3.setOption(option);

var mychart4 = echarts.init(document.getElementById('mychart4'));
option = {
	title:{
		text: '上船港口与生存率的关系',
		x: 'center',
	},
	tooltip:{
		trigger: 'item',
		formatter: '{c}'
	},
	legend:{
		data: ['生存', '遇难'],
		x: '75%',
	},
	xAxis:{
		data: ['南安普顿', '瑟堡', '昆士顿'],
	},
	yAxis:{
	},
	series:[
		{
			name: '生存',
			type: 'bar',
			data: [215, 95, 35],
			barWidth: 50,
			itemStyle:{color: '#34c726'},
			barGap: "10%",
		},
		{
			name: '遇难',
			type: 'bar',
			data: [425, 75, 100],
			barWidth: 50,
			itemStyle:{color: '#767676'},
			barGap: "10%",
		}
	]
};
mychart4.setOption(option);



var mychart5 = echarts.init(document.getElementById('mychart5'));
option = {
	title:{
		text: '船上亲人数量与生存率的关系',
		x: 'center',
	},
	tooltip:{
		trigger: 'item',
		formatter: '{c}'
	},
	legend:{
		data: ['生存', '遇难'],
		x: '75%',
	},
	xAxis:{
		data: ['0', '1', '2', '3', '4', '5'],
	},
	yAxis:{
	},
	series:[
		{
			name: '生存',
			type: 'bar',
			data: [205, 110, 10, 3, 3, 1],
			barWidth: 30,
			itemStyle:{color: '#34c726'},
			barGap: "5%",
		},
		{
			name: '遇难',
			type: 'bar',
			data: [400, 98, 12, 11, 12, 3],
			barWidth: 30,
			itemStyle:{color: '#767676'},
			barGap: "5%",
		}
	]
};
mychart5.setOption(option);
