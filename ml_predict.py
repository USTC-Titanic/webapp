from page import PageHandler
from random import random
from MachineLearningModules import predict
rel_path = './MachineLearningModules/'

class MLPredictHandler(PageHandler):
	def get(self):
		filename = 'predict/index.html'
		return self.render_file(filename)

	def post(self):
		form = self.get_form()
		print(form)
		user_data = {}
		for k, v in form.items():
			user_data[k] = [v]
		print(user_data)
		
		default_user_data = {
		              "Sex": ["male"],
		              "Pclass": ["3"],
		              "Name": ["Kelly, Mr. James"],
		              "Age": ["34.5"],
		              "SibSp": ["0"],
		              "Parch": ["0"]
		            }
		print(default_user_data)
		
		survival_index = predict.get_survival_index(user_data=user_data, rel_path=rel_path)
		print(survival_index)
		return self.render(str(survival_index))
