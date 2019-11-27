<!DOCTYPE html>
<html>
<head>
	<title>机器学习开发日志</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="/static/blog/post/post_template.css">
</head>

<body>
	<main class="container my_padding">
		<article class="markdown-body entry-content p-3 p-md-6">

<h1>人工智能实验3: 基于TensorFlow的cpatcha注册码识别</h1>
<p>2019-04-16</p>
<h1>人工智能实验: 基于TensorFlow的cpatcha注册码识别</h1>
<h2>实验报告内容</h2>
<ul>
<li>
<p>给出你自己第一个完整的神经网络构建过程，包括</p>
<ul>
<li>生成训练数据集</li>
<li>定义网络模型</li>
<li>训练模型参数并保存</li>
<li>读入参数并测试新数据</li>
</ul>
</li>
<li>
<p>描述实验结果</p>
<br>
</li>
</ul>
<h2>神经网络构建过程</h2>
<ul>
<li>
<p>注:</p>
<p>感谢 <a href="https://github.com/lpty/tensorflow_tutorial/tree/master/captchaCnn">lpty 的 tensorflow_tutorial-captchaCnn 例程</a> 和 <a href="https://github.com/Arfer-ustc/captcha">Arfer 的 TensorFlow CAPTCHA</a>, 本次实验的代码由此改编而来</p>
<p>实验文档采用 <code>markdown</code> 格式进行编写</p>
</li>
</ul>
<ol start="0">
<li>
<p>实验环境</p>
<ul>
<li>Ubuntu 16.04, x64</li>
<li>docker 18.09.0</li>
<li>tensorflow-py3 1.12.0</li>
<li>python 3.5.2</li>
<li>captcha 0.3</li>
<li>PIL 5.3.0</li>
<li>matplotlib 3.0.1</li>
<li>numpy 1.15.4</li>
<li>Jupyter Notebook 5.7.0</li>
</ul>
</li>
<li>
<p>生成训练数据集</p>
<ul>
<li>
<p><code>Captcha</code>（全自动区分计算机和人类的图灵测试，俗称验证码）是目前用于区分人和机器主要办法，其工作原理是通过提供模糊或是有歧义的图片，并要求用户进行回答，以此来区分人和机器</p>
<p>本次实验使用 <code>Python</code> 的第三方库 <code>captcha</code> 来生成图片验证码。由于计算能力有限，生成的验证码中只包含数字，且验证码长度为 <code>4</code></p>
</li>
<li>
<p>生成验证码及其对应标签的 <code>Python</code> 代码及注释如下</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> random
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
<span class="pl-k">from</span> <span class="pl-c1">PIL</span> <span class="pl-k">import</span> Image
<span class="pl-k">from</span> captcha.image <span class="pl-k">import</span> ImageCaptcha

<span class="pl-c"><span class="pl-c">#</span> 验证码仅包含数字字符</span>
<span class="pl-c1">NUMBER</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">'</span>0<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>1<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>2<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>3<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>4<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>5<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>6<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>7<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>8<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>9<span class="pl-pds">'</span></span>]
<span class="pl-c1">CAPTCHA_LIST</span> <span class="pl-k">=</span> <span class="pl-c1">NUMBER</span>
<span class="pl-c"><span class="pl-c">#</span> 验证码字符串长度为 4</span>
<span class="pl-c1">CAPTCHA_LEN</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>
<span class="pl-c"><span class="pl-c">#</span> 验证码图片高度为 60px, 宽度为 160px</span>
<span class="pl-c1">CAPTCHA_HEIGHT</span> <span class="pl-k">=</span> <span class="pl-c1">60</span>
<span class="pl-c1">CAPTCHA_WIDTH</span> <span class="pl-k">=</span> <span class="pl-c1">160</span>

<span class="pl-k">def</span> <span class="pl-en">random_captcha_text</span>(<span class="pl-smi">char_set</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_LIST</span>, <span class="pl-smi">captcha_size</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_LEN</span>):
	<span class="pl-c"><span class="pl-c">#</span> 生成验证码文本</span>
	captcha_text <span class="pl-k">=</span> [random.choice(char_set) <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">range</span>(captcha_size)]
	<span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span><span class="pl-pds">'</span></span>.join(captcha_text)

<span class="pl-k">def</span> <span class="pl-en">gen_captcha_text_and_image</span>(<span class="pl-smi">width</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_WIDTH</span>, <span class="pl-smi">height</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_HEIGHT</span>,<span class="pl-smi">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>):
	<span class="pl-c"><span class="pl-c">#</span> 定义验证码图像的尺寸</span>
	image <span class="pl-k">=</span> ImageCaptcha(<span class="pl-v">width</span><span class="pl-k">=</span>width, <span class="pl-v">height</span><span class="pl-k">=</span>height)
	<span class="pl-c"><span class="pl-c">#</span> 验证码文本</span>
	captcha_text <span class="pl-k">=</span> random_captcha_text()
	<span class="pl-c"><span class="pl-c">#</span> 生成验证码图像</span>
	captcha <span class="pl-k">=</span> image.generate(captcha_text)
	<span class="pl-c"><span class="pl-c">#</span> 保存图像</span>
	<span class="pl-k">if</span> save:
		image.write(captcha_text, captcha_text <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">'</span>.jpg<span class="pl-pds">'</span></span>)
	captcha_image <span class="pl-k">=</span> Image.open(captcha)
	<span class="pl-c"><span class="pl-c">#</span> 为了加快训练速度，我们还可以将验证码转为灰度图</span>
	captcha_image <span class="pl-k">=</span> captcha_image.convert(<span class="pl-s"><span class="pl-pds">'</span>L<span class="pl-pds">'</span></span>)
	<span class="pl-c"><span class="pl-c">#</span> 转化为np数组</span>
	captcha_image <span class="pl-k">=</span> np.array(captcha_image)
	<span class="pl-k">return</span> captcha_text, captcha_image

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
	t, im <span class="pl-k">=</span> gen_captcha_text_and_image(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>)
	<span class="pl-c1">print</span>(t, im)</pre></div>
</li>
<li>
<p>生成的验证码如图</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/captcha_2592.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/captcha_2592.png" alt="captcha_2592" style="max-width:100%;"></a></p>
</li>
</ul>
</li>
<li>
<p>定义网络模型</p>
<ul>
<li>
<p>卷积层的代码如下</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">cnn_graph</span>(<span class="pl-smi">x</span>, <span class="pl-smi">keep_prob</span>, <span class="pl-smi">size</span>, <span class="pl-smi">captcha_list</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_LIST</span>, <span class="pl-smi">captcha_len</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_LEN</span>):
	<span class="pl-c"><span class="pl-c">#</span> 三层卷积神经网络计算图</span>
	<span class="pl-c"><span class="pl-c">#</span> keep_prob 是 dropout 的保留比例</span>

	<span class="pl-c"><span class="pl-c">#</span> 首先将图片 reshape 为 4 维向量</span>
	image_height, image_width <span class="pl-k">=</span> size
	x_image <span class="pl-k">=</span> tf.reshape(x, <span class="pl-v">shape</span><span class="pl-k">=</span>[<span class="pl-k">-</span><span class="pl-c1">1</span>, image_height, image_width, <span class="pl-c1">1</span>])

	<span class="pl-c"><span class="pl-c">#</span> 第 1 层</span>
	<span class="pl-c"><span class="pl-c">#</span> 3x3 的卷积核, 输入为 1, 输出32个特征, 即有 32 个卷积核</span>
	w_conv1 <span class="pl-k">=</span> weight_variable([<span class="pl-c1">3</span>, <span class="pl-c1">3</span>, <span class="pl-c1">1</span>, <span class="pl-c1">32</span>])
	<span class="pl-c"><span class="pl-c">#</span> 偏置</span>
	b_conv1 <span class="pl-k">=</span> bias_variable([<span class="pl-c1">32</span>])
	<span class="pl-c"><span class="pl-c">#</span> relu 激活函数</span>
	h_conv1 <span class="pl-k">=</span> tf.nn.relu(tf.nn.bias_add(conv2d(x_image, w_conv1), b_conv1))
	<span class="pl-c"><span class="pl-c">#</span> 2x2 的 max 池化层</span>
	h_pool1 <span class="pl-k">=</span> max_pool_2x2(h_conv1)
	<span class="pl-c"><span class="pl-c">#</span> dropout 防止过拟合, 同时加快训练速度</span>
	h_drop1 <span class="pl-k">=</span> tf.nn.dropout(h_pool1, keep_prob)

	<span class="pl-c"><span class="pl-c">#</span> 第 2 层</span>
	<span class="pl-c"><span class="pl-c">#</span> 3x3 的卷积核, 输入为 32, 输出 64 个特征, 即有 2 个卷积核</span>
	w_conv2 <span class="pl-k">=</span> weight_variable([<span class="pl-c1">3</span>, <span class="pl-c1">3</span>, <span class="pl-c1">32</span>, <span class="pl-c1">64</span>])
	<span class="pl-c"><span class="pl-c">#</span> 偏置</span>
	b_conv2 <span class="pl-k">=</span> bias_variable([<span class="pl-c1">64</span>])
	<span class="pl-c"><span class="pl-c">#</span> relu 激活函数</span>
	h_conv2 <span class="pl-k">=</span> tf.nn.relu(tf.nn.bias_add(conv2d(h_drop1, w_conv2), b_conv2))
	<span class="pl-c"><span class="pl-c">#</span> 2x2 的 max 池化层</span>
	h_pool2 <span class="pl-k">=</span> max_pool_2x2(h_conv2)
	<span class="pl-c"><span class="pl-c">#</span> dropout 防止过拟合, 同时加快训练速度</span>
	h_drop2 <span class="pl-k">=</span> tf.nn.dropout(h_pool2, keep_prob)

	<span class="pl-c"><span class="pl-c">#</span> 第 3 层</span>
	<span class="pl-c"><span class="pl-c">#</span> 3x3 的卷积核, 输入为 64, 输出 64 个特征, 即有 1 个卷积核</span>
	w_conv3 <span class="pl-k">=</span> weight_variable([<span class="pl-c1">3</span>, <span class="pl-c1">3</span>, <span class="pl-c1">64</span>, <span class="pl-c1">64</span>])
	b_conv3 <span class="pl-k">=</span> bias_variable([<span class="pl-c1">64</span>])
	h_conv3 <span class="pl-k">=</span> tf.nn.relu(tf.nn.bias_add(conv2d(h_drop2, w_conv3), b_conv3))
	<span class="pl-c"><span class="pl-c">#</span> 2x2 的 max 池化层</span>
	h_pool3 <span class="pl-k">=</span> max_pool_2x2(h_conv3)
	h_drop3 <span class="pl-k">=</span> tf.nn.dropout(h_pool3, keep_prob)

	<span class="pl-c"><span class="pl-c">#</span> 全连接层</span>
	<span class="pl-c"><span class="pl-c">#</span> 输入 image_height*image_width*64</span>
	<span class="pl-c"><span class="pl-c">#</span> 输出 1024</span>
	image_height <span class="pl-k">=</span> <span class="pl-c1">int</span>(h_drop3.shape[<span class="pl-c1">1</span>])
	image_width <span class="pl-k">=</span> <span class="pl-c1">int</span>(h_drop3.shape[<span class="pl-c1">2</span>])
	w_fc <span class="pl-k">=</span> weight_variable([image_height<span class="pl-k">*</span>image_width<span class="pl-k">*</span><span class="pl-c1">64</span>, <span class="pl-c1">1024</span>])
	b_fc <span class="pl-k">=</span> bias_variable([<span class="pl-c1">1024</span>])
	h_drop3_re <span class="pl-k">=</span> tf.reshape(h_drop3, [<span class="pl-k">-</span><span class="pl-c1">1</span>, image_height<span class="pl-k">*</span>image_width<span class="pl-k">*</span><span class="pl-c1">64</span>])
	h_fc <span class="pl-k">=</span> tf.nn.relu(tf.add(tf.matmul(h_drop3_re, w_fc), b_fc))
	h_drop_fc <span class="pl-k">=</span> tf.nn.dropout(h_fc, keep_prob)

	<span class="pl-c"><span class="pl-c">#</span> 输出层</span>
	<span class="pl-c"><span class="pl-c">#</span> 输入 1024</span>
	<span class="pl-c"><span class="pl-c">#</span> 输出 10x4 = 40 (验证码仅含数字)</span>
	w_out <span class="pl-k">=</span> weight_variable([<span class="pl-c1">1024</span>, <span class="pl-c1">len</span>(captcha_list)<span class="pl-k">*</span>captcha_len])
	b_out <span class="pl-k">=</span> bias_variable([<span class="pl-c1">len</span>(captcha_list)<span class="pl-k">*</span>captcha_len])
	y_conv <span class="pl-k">=</span> tf.add(tf.matmul(h_drop_fc, w_out), b_out)
	<span class="pl-k">return</span> y_conv</pre></div>
</li>
<li>
<p>总体模型图如下</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/model.jpg"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/model.jpg" alt="model" style="max-width:100%;"></a></p>
</li>
</ul>
</li>
<li>
<p>训练模型参数并保存</p>
<ul>
<li>
<p>优化器计算图</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">optimize_graph</span>(<span class="pl-smi">y</span>, <span class="pl-smi">y_conv</span>):
	<span class="pl-c"><span class="pl-c">#</span> 交叉熵计算 loss 注意 logits 输入是在函数内部进行sigmod操作</span>
	<span class="pl-c"><span class="pl-c">#</span> sigmod_cross适用于每个类别相互独立但不互斥，如图中可以有字母和数字</span>
	<span class="pl-c"><span class="pl-c">#</span> softmax_cross 适用于每个类别独立且互斥的情况，如数字和字母不可以同时出现</span>
	loss <span class="pl-k">=</span> tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(<span class="pl-v">logits</span><span class="pl-k">=</span>y_conv, <span class="pl-v">labels</span><span class="pl-k">=</span>y))
	<span class="pl-c"><span class="pl-c">#</span> 最小化loss优化</span>
	optimizer <span class="pl-k">=</span> tf.train.AdamOptimizer(<span class="pl-v">learning_rate</span><span class="pl-k">=</span><span class="pl-c1">0.001</span>).minimize(loss)
	<span class="pl-k">return</span> optimizer</pre></div>
</li>
<li>
<p>准确率计算图, 这里判断准确率的标准是所有字符都相同, 当然也有一些算法是按照单个对应位置的字符相同就算正确的方法来计算准确率的, 后者的训练速度更快一点, 但是最后的性能可能比不上前者(4 个字符都相同), 但是个人感觉, 这个差距可以通过多试几个验证码来弥补，因为就算是人类识别，有时候也不能每次都保证正确。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">accuracy_graph</span>(<span class="pl-smi">y</span>, <span class="pl-smi">y_conv</span>, <span class="pl-smi">width</span><span class="pl-k">=</span><span class="pl-c1">len</span>(<span class="pl-c1">CAPTCHA_LIST</span>), <span class="pl-smi">height</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_LEN</span>):
	<span class="pl-c"><span class="pl-c">#</span> 预测值</span>
	predict <span class="pl-k">=</span> tf.reshape(y_conv, [<span class="pl-k">-</span><span class="pl-c1">1</span>, height, width])
	max_predict_idx <span class="pl-k">=</span> tf.argmax(predict, <span class="pl-c1">2</span>)
	<span class="pl-c"><span class="pl-c">#</span> 实际值(标签)</span>
	label <span class="pl-k">=</span> tf.reshape(y, [<span class="pl-k">-</span><span class="pl-c1">1</span>, height, width])
	max_label_idx <span class="pl-k">=</span> tf.argmax(label, <span class="pl-c1">2</span>)
	correct_p <span class="pl-k">=</span> tf.equal(max_predict_idx, max_label_idx)
	accuracy <span class="pl-k">=</span> tf.reduce_mean(tf.cast(correct_p, tf.float32))
	<span class="pl-k">return</span> accuracy</pre></div>
</li>
<li>
<p>训练过程</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">train</span>(<span class="pl-smi">height</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_HEIGHT</span>, <span class="pl-smi">width</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_WIDTH</span>, <span class="pl-smi">y_size</span><span class="pl-k">=</span><span class="pl-c1">len</span>(<span class="pl-c1">CAPTCHA_LIST</span>)<span class="pl-k">*</span><span class="pl-c1">CAPTCHA_LEN</span>):
	<span class="pl-c"><span class="pl-c">#</span> cnn在图像大小是2的倍数时性能最高, 如果图像大小不是2的倍数，可以在图像边缘补无用像素</span>
	<span class="pl-c"><span class="pl-c">#</span> 在图像上补2行，下补3行，左补2行，右补2行</span>
	<span class="pl-c"><span class="pl-c">#</span> np.pad(image,((2,3),(2,2)), 'constant', constant_values=(255,))</span>

	<span class="pl-c"><span class="pl-c">#</span> 在准确度达到 95% 时开始保存模型</span>
	acc_rate <span class="pl-k">=</span> <span class="pl-c1">0.95</span>
	<span class="pl-c"><span class="pl-c">#</span> 按照图片大小申请占位符</span>
	x <span class="pl-k">=</span> tf.placeholder(tf.float32, [<span class="pl-c1">None</span>, height <span class="pl-k">*</span> width])
	y <span class="pl-k">=</span> tf.placeholder(tf.float32, [<span class="pl-c1">None</span>, y_size])
	<span class="pl-c"><span class="pl-c">#</span> 防止过拟合 训练时启用 测试时不启用, keep_prob 是 dropout 的保留比例</span>
	keep_prob <span class="pl-k">=</span> tf.placeholder(tf.float32)
	<span class="pl-c"><span class="pl-c">#</span> cnn模型</span>
	y_conv <span class="pl-k">=</span> cnn_graph(x, keep_prob, (height, width))
	<span class="pl-c"><span class="pl-c">#</span> 优化器</span>
	optimizer <span class="pl-k">=</span> optimize_graph(y, y_conv)
	<span class="pl-c"><span class="pl-c">#</span> 偏差</span>
	accuracy <span class="pl-k">=</span> accuracy_graph(y, y_conv)
	<span class="pl-c"><span class="pl-c">#</span> 启动会话.开始训练</span>
	saver <span class="pl-k">=</span> tf.train.Saver()
	sess <span class="pl-k">=</span> tf.Session()
	sess.run(tf.global_variables_initializer())
	step <span class="pl-k">=</span> <span class="pl-c1">0</span>
	<span class="pl-k">while</span> <span class="pl-c1">1</span>:
		batch_x, batch_y <span class="pl-k">=</span> next_batch(<span class="pl-c1">64</span>)
		sess.run(optimizer, <span class="pl-v">feed_dict</span><span class="pl-k">=</span>{x: batch_x, y: batch_y, keep_prob: <span class="pl-c1">0.75</span>})
		<span class="pl-c"><span class="pl-c">#</span> 每训练 100 次测试一次, 即进行一次性能评估</span>
		<span class="pl-k">if</span> step <span class="pl-k">%</span> <span class="pl-c1">100</span> <span class="pl-k">==</span> <span class="pl-c1">0</span>:
			batch_x_test, batch_y_test <span class="pl-k">=</span> next_batch(<span class="pl-c1">100</span>)
			acc <span class="pl-k">=</span> sess.run(accuracy,<span class="pl-v">feed_dict</span><span class="pl-k">=</span>{x:batch_x_test,y:batch_y_test,keep_prob:<span class="pl-c1">1.0</span>})
			<span class="pl-c1">print</span>(datetime.now().strftime(<span class="pl-s"><span class="pl-pds">'</span><span class="pl-c1">%c</span><span class="pl-pds">'</span></span>), <span class="pl-s"><span class="pl-pds">'</span> step:<span class="pl-pds">'</span></span>, step, <span class="pl-s"><span class="pl-pds">'</span> accuracy:<span class="pl-pds">'</span></span>, acc)
			<span class="pl-c"><span class="pl-c">#</span> 准确率高于 0.95 时开始保存模型</span>
			<span class="pl-k">if</span> acc <span class="pl-k">&gt;</span> acc_rate:
				model_path <span class="pl-k">=</span> os.getcwd() <span class="pl-k">+</span> os.sep <span class="pl-k">+</span> <span class="pl-c1">str</span>(acc_rate) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">"</span>captcha.model<span class="pl-pds">"</span></span>
				saver.save(sess, model_path, <span class="pl-v">global_step</span><span class="pl-k">=</span>step)
				acc_rate <span class="pl-k">+=</span> <span class="pl-c1">0.01</span>
				<span class="pl-c"><span class="pl-c">#</span> 当准确率大于 0.99 时结束训练</span>
				<span class="pl-k">if</span> acc_rate <span class="pl-k">&gt;</span> <span class="pl-c1">0.99</span>:
					<span class="pl-k">break</span>
		step <span class="pl-k">+=</span> <span class="pl-c1">1</span>
	sess.close()</pre></div>
</li>
</ul>
</li>
<li>
<p>读入参数并测试新数据</p>
<ul>
<li>
<p>通过训练好的模型, 将验证码图片转化为文本</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">captcha2text</span>(<span class="pl-smi">image_list</span>, <span class="pl-smi">height</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_HEIGHT</span>, <span class="pl-smi">width</span><span class="pl-k">=</span><span class="pl-c1">CAPTCHA_WIDTH</span>):
	x <span class="pl-k">=</span> tf.placeholder(tf.float32, [<span class="pl-c1">None</span>, height <span class="pl-k">*</span> width])
	keep_prob <span class="pl-k">=</span> tf.placeholder(tf.float32)
	y_conv <span class="pl-k">=</span> cnn_graph(x, keep_prob, (height, width))
	saver <span class="pl-k">=</span> tf.train.Saver()
	<span class="pl-k">with</span> tf.Session() <span class="pl-k">as</span> sess:
		<span class="pl-c"><span class="pl-c">#</span> 读取模型</span>
		saver.restore(sess, tf.train.latest_checkpoint(<span class="pl-s"><span class="pl-pds">'</span>.<span class="pl-pds">'</span></span>))
		predict <span class="pl-k">=</span> tf.argmax(tf.reshape(y_conv, [<span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">CAPTCHA_LEN</span>, <span class="pl-c1">len</span>(<span class="pl-c1">CAPTCHA_LIST</span>)]), <span class="pl-c1">2</span>)
		vector_list <span class="pl-k">=</span> sess.run(predict, <span class="pl-v">feed_dict</span><span class="pl-k">=</span>{x: image_list, keep_prob: <span class="pl-c1">1</span>})
		vector_list <span class="pl-k">=</span> vector_list.tolist()
		text_list <span class="pl-k">=</span> [vec2text(vector) <span class="pl-k">for</span> vector <span class="pl-k">in</span> vector_list]
		<span class="pl-k">return</span> text_list

<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
	<span class="pl-c"><span class="pl-c">#</span> 生成测试图片和标签</span>
	text, image <span class="pl-k">=</span> gen_captcha_text_and_image()
	plt.figure(<span class="pl-s"><span class="pl-pds">'</span>color<span class="pl-pds">'</span></span>)
	plt.imshow(image, <span class="pl-v">cmap</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>gray<span class="pl-pds">'</span></span>)
	plt.axis(<span class="pl-s"><span class="pl-pds">'</span>off<span class="pl-pds">'</span></span>)
	<span class="pl-c"><span class="pl-c">#</span> 显示图片</span>
	plt.show()

	<span class="pl-c"><span class="pl-c">#</span> 图片转为灰度图</span>
	image <span class="pl-k">=</span> convert2gray(image)
	image <span class="pl-k">=</span> image.flatten() <span class="pl-k">/</span> <span class="pl-c1">255</span>

	<span class="pl-c"><span class="pl-c">#</span> 输出标签和预测值</span>
	<span class="pl-c"><span class="pl-c">#</span> 输出格式为  </span>
	pred_text <span class="pl-k">=</span> captcha2text([image])
	<span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">'</span>Label:<span class="pl-pds">'</span></span>, text, <span class="pl-s"><span class="pl-pds">'</span> Predict:<span class="pl-pds">'</span></span>, pred_text)</pre></div>
</li>
</ul>
<br>
</li>
</ol>
<h2>实验结果</h2>
<ol>
<li>
<p>补充分析</p>
<p>在进行了 <code>7900</code> 个 <code>step</code> 的训练之后, 模型达到了 <code>99%</code> 的准确率, 每一个 <code>step</code> 中用到了 <code>next_batch(100)</code>, 即 <code>batch_count=64</code>, 因此一共训练了 <code>7900 * 64 = 505600</code> 张图片</p>
<p>同时可以看到, 每经过 <code>100</code> 个 <code>step</code>, 都会进行一次测试, 每次测试用到了 <code>next_batch(100)</code>, 即每次阶段性测试都使用了 <code>100</code> 张图片进行测试, 以判断准确率是否达到要求</p>
</li>
<li>
<p>测试结果截图</p>
<p>部分测试结果截图如下，其中 <code>7991</code> 被识别成了 <code>2991</code>, 其他的都识别正确</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/0000.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/0000.png" alt="0000" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/0263.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/0263.png" alt="0263" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/2059.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/2059.png" alt="2059" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/2189.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/2189.png" alt="2189" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4293.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4293.png" alt="4293" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4531.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4531.png" alt="4531" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4567.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/4567.png" alt="4567" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/6613.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/6613.png" alt="6613" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/6918.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/6918.png" alt="6918" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/7383.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/7383.png" alt="7383" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/7991_2991.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/7991_2991.png" alt="7991_2991" style="max-width:100%;"></a><br>
<a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/8371.png"><img src="https://raw.githubusercontent.com/jJayyyyyyy/USTC-2018-Smester-1/master/AI/exp/04_Captcha/assets/8371.png" alt="8371" style="max-width:100%;"></a></p>
<p>注：由于本地机器性能较差，上述实验结果是通过ssh登陆到远程主机后运行得到的，由于没有图形界面，所以只能通过命令行截图的方式展现，另外由于终端透明度设置的问题，背景上会有一些其他窗口的字，还请见谅。</p>
<br>
</li>
</ol>
<h2>补充问题</h2>
<ul>
<li>
<p>灰度怎么转，为什么使用灰度</p>
<p>可以通过 <code>PIL.Image.convert('L')</code> 将图片转为灰度图，也可以将图片转为 <code>np.array</code> 后，用 <code>img = np.mean(img, -1)</code> 转换为灰度图</p>
<p>使用灰度图可以减少多余的信息，从而减少计算量</p>
</li>
<li>
<p>如何定义训练的准确率，准确率的定义会不会影响训练</p>
<p>关于准确率的描述，在 <code>训练模型参数并保存</code> 一节中已有描述，即，这里判断准确率的标准是所有字符都相同, 当然也有一些算法是按照单个对应位置的字符相同就算正确的方法来计算准确率的, 后者的训练速度更快一点, 但是最后的性能可能比不上前者(4 个字符都相同), 但是个人感觉, 这个差距可以通过多试几个验证码来弥补，因为就算是人类识别，有时候也不能每次都保证正确。</p>
</li>
<li>
<p>每层的激活函数为什么用 <code>Relu</code> 函数不使用 <code>Sigmoid</code> 函数</p>
<p>根据 <a href="https://blog.csdn.net/PKU_Jade/article/details/78213797" rel="nofollow">为什么使用ReLU而不是sigmoid</a> 和 <a href="https://www.jianshu.com/p/95c79381ab4f" rel="nofollow">CNN on TensorFlow</a>, 在 <code>CNN</code> 中</p>
<ul>
<li><code>sigmoid</code> 计算量过大</li>
<li>对于深层网络，<code>sigmoid</code> 函数反向传播时，很容易就会出现梯度消失的情况</li>
<li><code>Relu</code> 会使一部分神经元的输出为 <code>0</code>，这样就造成了网络的稀疏性，并且减少了参数的相互依存关系，缓解了过拟合问题的发生</li>
</ul>
<br>
</li>
</ul>
<h2>参考资料</h2>
<ul>
<li>
<p><a href="https://github.com/lpty/tensorflow_tutorial/tree/master/captchaCnn">lpty 的 tensorflow_tutorial-captchaCnn 例程</a></p>
</li>
<li>
<p><a href="https://github.com/Arfer-ustc/captcha">Arfer 的 TensorFlow CAPTCHA</a></p>
</li>
<li>
<p><a href="https://www.tensorflow.org/api_docs/python/" rel="nofollow">TensorFlow API</a></p>
</li>
<li>
<p><a href="https://docs.docker.com/install/linux/docker-ce/ubuntu/" rel="nofollow">docker for Ubuntu</a></p>
</li>
<li>
<p><a href="https://blog.csdn.net/PKU_Jade/article/details/78213797" rel="nofollow">为什么使用ReLU而不是sigmoid</a></p>
</li>
<li>
<p><a href="https://www.jianshu.com/p/95c79381ab4f" rel="nofollow">CNN on TensorFlow</a></p>
</li>
<li>
<p><a href="https://www.processon.com/" rel="nofollow">ProcessOn</a></p>
<br>
</li>
</ul>
<h2>TODO</h2>
<ul>
<li>
<p>本次实验为什么不使用 <code>softmax_cross</code> 作为 <code>loss</code> 而用 <code>sigmoid_cross</code> 作为 <code>loss function</code></p>
<p>代码中有如下注释</p>
<div class="highlight highlight-source-python"><pre><span class="pl-c"><span class="pl-c">#</span> 交叉熵计算 loss 注意 logits 输入是在函数内部进行sigmod操作</span>
<span class="pl-c"><span class="pl-c">#</span> sigmod_cross适用于每个类别相互独立但不互斥，如图中可以有字母和数字</span>
<span class="pl-c"><span class="pl-c">#</span> softmax_cross 适用于每个类别独立且互斥的情况，如数字和字母不可以同时出现</span></pre></div>
<p>但是还没有完全理解, 需要查阅更多资料, 也希望老师和学长学姐能够不吝赐教</p>
</li>
<li>
<p>如果要使用 <code>softmax_cross</code> 作为 <code>loss function</code>，应该怎么改变训练方法</p>
<br>
</li>
</ul>

		</article>
	</main>
</body>

<section class="row justify-content-end">
	<div class="col-1 text-right">
		<button type="button" id="go-to-top" class="btn btn-sm btn-outline-primary" onclick="goToTop()" style="display: none; position: fixed; bottom: 80px; right: 16px;">↑</button>
	</div>
</section>

<script type="text/javascript">
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function(){
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		document.getElementById("go-to-top").style.display = "block";
	} else {
		document.getElementById("go-to-top").style.display = "none";
	}
};

// https://www.w3schools.com/tags/ev_onclick.asp
// http://www.w3school.com.cn/jsref/met_win_setinterval.asp
function goToTop(){
	let t = setInterval( function(){
		if( document.documentElement.scrollTop <= 0 ){
			clearInterval(t);
		}else{
			document.documentElement.scrollTop -= 40;
		}
	}, 20);
};
</script>

</html>