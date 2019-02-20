import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
# https://scikit-learn.org/stable/modules/model_persistence.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html
# https://stackoverflow.com/questions/52640386/how-do-i-solve-the-future-warning-min-groups-self-n-splits-warning-in

def feature_engineering_test_data():
	# 读取测试数据集
	data_test = pd.read_csv('test.csv')
	# 获取乘客ID，方便构造最后要提交的数据
	PassengerId = data_test['PassengerId']
	# 将性别从字符串类型转换为0或1数值型数据
	data_test['Sex'] = data_test['Sex'].apply(lambda s: 1 if s == 'male' else 0)
	
	# 计算年龄平均值
	age_mean = data_test.Age.mean()
	# 年龄的缺失值用平均值进行填充
	data_test.Age = data_test.Age.fillna(age_mean)

	# 其他的缺失值填0
	data_test = data_test.fillna(0)
	print(data_test.dtypes)
	# 选取特征
	dataset_X = data_test[['Sex', 'Age', 'Pclass', 'SibSp', 'Parch']].values
	return PassengerId, dataset_X

def user_data_filter(user_data):
	# test_data = pd.read_json(user_data)
	test_data = pd.DataFrame.from_dict(user_data)
	# print(test_data.info())
	test_data = test_data.fillna(0)
	test_data['Sex'] = test_data['Sex'].apply(lambda s: 0 if s == 'female' else 1)
	# https://datascience.stackexchange.com/questions/42055/the-truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any

	test_data['Age'] = test_data['Age'].astype('float')
	test_data['Pclass'] = test_data['Pclass'].astype('int')
	test_data['SibSp'] = test_data['SibSp'].astype('int')
	test_data['Parch'] = test_data['Parch'].astype('int')
	# print()
	# print(test_data.info())
	dataset_X = test_data[['Sex', 'Age', 'Pclass', 'SibSp', 'Parch']].values
	return dataset_X

def feature_engineering_train_data():
	# 读训练数据
	data_train = pd.read_csv('train.csv')
	# 将性别从字符串类型转换为0或1数值型数据
	data_train['Sex'] = data_train['Sex'].apply(lambda s: 1 if s == 'male' else 0)

	age_mean = data_train.Age.mean()
	# 年龄的缺失值用平均值进行填充
	data_train.Age = data_train.Age.fillna(age_mean)

	# 其他缺失值填0
	data_train = data_train.fillna(0)

	# 选取特征
	dataset_X = data_train[['Sex', 'Age', 'Pclass', 'SibSp', 'Parch']].values

	# 建立标签
	dataset_Y = data_train['Survived'].values

	return dataset_X, dataset_Y

def train():
	dataset_X, dataset_Y = feature_engineering_train_data()
	# lr_model = LogisticRegression(solver='lbfgs')
	lr_model = LinearRegression()
	lr_model.fit(dataset_X, dataset_Y)
	joblib.dump(lr_model, 'model_lr.joblib')
	print('train finished')

def gen_submission():
	PassengerId, X_test = feature_engineering_test_data()
	lr_model = joblib.load('model_lr.joblib')
	Y_test = lr_model.predict(X_test)
	print(Y_test)
	submission = pd.DataFrame({
			"PassengerId": PassengerId,
			"Survived": Y_test
		})
	submission.to_csv("titanic-submission.csv", index=False)
	print('submission generated')

default_user_data = {
	                  "Sex": ["male"],
	                  "Pclass": ["3"],
	                  "Name": ["Kelly, Mr. James"],
	                  "Age": ["34.5"],
	                  "SibSp": ["0"],
	                  "Parch": ["0"]
	                }

def get_survival_index(user_data=default_user_data, rel_path='./'):
	X_test = user_data_filter(user_data)
	lr_model = joblib.load(rel_path + 'model_lr.joblib')
	Y_test = lr_model.predict(X_test)
	survival_index = '%.2f' % (Y_test[0] * 100)
	return survival_index

def main():
	survival_index = get_survival_index(user_data=default_user_data, rel_path='./')
	print('done')

if __name__ == '__main__':
	# train()
	# gen_submission()
	main()