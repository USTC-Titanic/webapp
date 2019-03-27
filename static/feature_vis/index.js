'use strict';
var myPie = echarts.init(document.getElementsByTagName('article')[0]);
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
myPie.setOption(option);



var myBar2 = echarts.init(document.getElementById('article2'));
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
myBar2.setOption(option);

var myBar3 = echarts.init(document.getElementById('article3'));
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
myBar3.setOption(option);

var myBar4 = echarts.init(document.getElementById('article4'));
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
myBar4.setOption(option);



var myBar5 = echarts.init(document.getElementById('article5'));
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
myBar5.setOption(option);
