from flask import Flask, render_template, request, redirect, url_for, session
from learn import WordLearner
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
app = Flask(__name__)

app.secret_key = 'some_secret_key'

@app.route('/')
def index():
  if 'username' in session:
    return render_template('index.html')
  else:
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if 'username' in session:
    return redirect(url_for('index'))
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
      session['username'] = username
      return redirect(url_for('index'))
    else:
      return '用户名或密码错误'
  else:
    return render_template('login.html')

word_learner = WordLearner(['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe', 'house', 'ice', 'jacket'])

@app.route('/learn')
def learn():
  if 'username' in session:
    return render_template('learn.html',
      current_word=word_learner.get_current_word(),
      current_word_info=word_learner.get_current_word_info(),
      learned_words_count=word_learner.get_learned_words_count(),
      unlearned_words_count=word_learner.get_unlearned_words_count(),
      progress_percentage=word_learner.get_progress_percentage())
  else:
    return redirect(url_for('login'))

@app.route('/learn_next')
def learn_next():
  if 'username' in session:
    word_learner.next_word()
    return redirect(url_for('learn'))
  else:
    return redirect(url_for('login'))

@app.route('/learn_previous')
def learn_previous():
  if 'username' in session:
    word_learner.previous_word()
    return redirect(url_for('learn'))
  else:
    return redirect(url_for('login'))

@app.route('/query', methods=['GET', 'POST'])
def query():
  # 如果用户已登录
  if 'username' in session:
    # 如果请求方法是POST
    if request.method == 'POST':
      # 获取用户输入的单词
      word = request.form['word']
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 获取单词的信息
        word_info = word_learner.word_info[word]
        # 渲染单词查询页面模板，传入单词和单词信息
        return render_template('query.html', word=word, word_info=word_info)
      # 否则，返回提示信息
      else:
        return '无效的单词'
    # 如果请求方法是GET
    else:
      # 获取URL参数中的单词
      word = request.args.get('word')
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 获取单词的信息
        word_info = word_learner.word_info[word]
        # 渲染单词查询页面模板，传入单词和单词信息
        return render_template('query.html', word=word, word_info=word_info)
      # 否则，返回提示信息
      else:
        return '无效的单词'
  # 否则，重定向到登录页面
  else:
    return redirect(url_for('login'))

@app.route('/practice', methods=['GET', 'POST'])
def practice():
  # 如果用户已登录
  if 'username' in session:
    # 如果请求方法是POST
    if request.method == 'POST':
      # 获取用户输入的单词
      word = request.form['word']
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 获取用户输入的单词信息
        explanation = request.form['explanation']
        example = request.form['example']
        synonym = request.form['synonym']
        antonym = request.form['antonym']
        root = request.form['root']
        affix = request.form['affix']
        # 获取单词的真实信息
        word_info = word_learner.word_info[word]
        # 计算用户的正确率和对比结果
        accuracy, compare = word_learner.calculate_accuracy_and_compare(word, explanation, example, synonym, antonym, root, affix)
        # 渲染单词练习结果页面模板，传入单词，正确率，用户输入的信息，单词的真实信息，对比结果
        return render_template('practice_result.html', word=word, accuracy=accuracy, explanation=explanation, example=example, synonym=synonym, antonym=antonym, root=root, affix=affix, word_info=word_info, compare=compare)
      # 否则，返回提示信息
      else:
        return '无效的单词'
    # 如果请求方法是GET
    else:
      # 获取URL参数中的单词
      word = request.args.get('word')
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 渲染单词练习页面模板，传入单词
        return render_template('practice.html', word=word)
      # 否则，返回提示信息
      else:
        return '无效的单词'
  # 否则，重定向到登录页面
  else:
    return redirect(url_for('login'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
  # 如果用户已登录
  if 'username' in session:
    # 如果请求方法是POST
    if request.method == 'POST':
      # 获取用户输入的单词
      word = request.form['word']
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 获取用户输入的答案
        choice_answer = request.form['choice_answer']
        blank_answer = request.form['blank_answer']
        judge_answer = request.form['judge_answer']
        # 获取单词的真实信息
        word_info = word_learner.word_info[word]
        # 计算用户的正确率和对比结果
        accuracy, compare = word_learner.calculate_accuracy_and_compare_quiz(word, choice_answer, blank_answer, judge_answer)
        # 渲染单词测试结果页面模板，传入单词，正确率，用户输入的答案，单词的真实信息，对比结果
        return render_template('quiz_result.html', word=word, accuracy=accuracy, choice_answer=choice_answer, blank_answer=blank_answer, judge_answer=judge_answer, word_info=word_info, compare=compare)
      # 否则，返回提示信息
      else:
        return '无效的单词'
    # 如果请求方法是GET
    else:
      # 获取URL参数中的单词
      word = request.args.get('word')
      # 如果单词在单词列表中
      if word in word_learner.word_list:
        # 生成单词的选择题，填空题，判断题等
        choice_question, choice_options, blank_question, judge_question = word_learner.generate_quiz_questions(word)
        # 渲染单词测试页面模板，传入单词，选择题，填空题，判断题等
        return render_template('quiz.html', word=word, word_info=word_learner.word_info[word], choice_question=choice_question, choice_options=choice_options, blank_question=blank_question, judge_question=judge_question)
        # 否则，返回提示信息
      else:
        return '无效的单词'
  # 否则，重定向到登录页面
  else:
    return redirect(url_for('login'))

@app.route('/game')
def game():
  # 如果用户已登录，渲染单词游戏页面模板
  if 'username' in session:
    return render_template('game.html')
  # 否则，重定向到登录页面
  else:
    return redirect(url_for('login'))

@app.route('/qa')
def qa():
  # 如果用户已登录
  if 'username' in session:
    return render_template('qa.html')
  # 否则，重定向到登录页面
  else:
    return redirect(url_for('login'))

# @app.route('/account')
# def account():
#   # 如果用户已登录，渲染我的账户页面模板
#   if 'username' in session:
#     return render_template('account.html')
#   # 否则，重定向到登录页面
#   else:
#     return redirect(url_for('login'))
# 创建数据库连接对象
# 创建数据库连接对象
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='zhx123456',
                     charset='utf8')
# 设置一个secret_key
app.secret_key = 'supermarket'
# 或者
import os
app.secret_key = os.urandom(16)

# 创建游标对象
cursor = db.cursor()

# 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS supermarket")

# 选择数据库
cursor.execute("USE supermarket")

# 创建数据表
# 创建users表
cursor.execute("create TABLE IF NOT EXISTS users (id int primary key, username varchar(50), password varchar(50), role varchar(50), permission varchar(50))")

cursor.execute("CREATE TABLE IF NOT EXISTS Suppliers (SupplierID INT PRIMARY KEY, SupplierName VARCHAR(100), Address VARCHAR(200), Phone VARCHAR(20), ContactPerson VARCHAR(50), SupplyProduct VARCHAR(100), CooperationRecord TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS Products (ProductID INT PRIMARY KEY, ProductName VARCHAR(100), Category VARCHAR(50), Price DECIMAL(10,2), StockQuantity INT, SupplierID INT, FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID))")
cursor.execute("CREATE TABLE IF NOT EXISTS SaleDetails (DetailID INT PRIMARY KEY, SaleID INT, ProductID INT, Quantity INT, Subtotal DECIMAL(10,2))")

cursor.execute("CREATE TABLE IF NOT EXISTS Sales (SaleID INT PRIMARY KEY, CustomerID INT, EmployeeID INT, SaleDate DATE, TotalAmount DECIMAL(10,2), DetailID INT, FOREIGN KEY (DetailID) REFERENCES SaleDetails(DetailID))")

cursor.execute("CREATE TABLE IF NOT EXISTS Customers (CustomerID INT PRIMARY KEY, FirstName VARCHAR(50), LastName VARCHAR(50), Gender CHAR(1), Email VARCHAR(100), Phone VARCHAR(20), Address VARCHAR(200), Username VARCHAR(50), Password VARCHAR(50), Points INT, SaleID INT, FOREIGN KEY (SaleID) REFERENCES Sales(SaleID))")
cursor.execute("CREATE TABLE IF NOT EXISTS Employees (EmployeeID INT PRIMARY KEY, FirstName VARCHAR(50), LastName VARCHAR(50), Gender CHAR(1), Email VARCHAR(100), Phone VARCHAR(20), Position VARCHAR(50), Salary DECIMAL(10,2), Username VARCHAR(50), Password VARCHAR(50), SaleID INT, FOREIGN KEY (SaleID) REFERENCES Sales(SaleID))")

cursor.execute("CREATE TABLE IF NOT EXISTS Notifications (NotificationID INT PRIMARY KEY, UserID INT, Message TEXT, NotificationDate DATETIME, Type VARCHAR(50))")
cursor.execute("CREATE TABLE IF NOT EXISTS Recommendations (RecommendationID INT PRIMARY KEY, CustomerID INT, ProductID INT, RecommendationDate DATE, Price DECIMAL(10,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS Voices (VoiceID INT PRIMARY KEY, UserID INT, InteractionDate DATETIME, Transcript TEXT, Type VARCHAR(50))")


# 定义用户管理路由
@app.route('/user')
def user():
    # 查询所有用户信息
    sql = 'select * from users'
    cursor.execute(sql)
    users = cursor.fetchall()
    # 渲染用户管理模板
    return render_template('user.html', users=users)

# 定义添加用户路由
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    # 如果是GET请求，渲染添加用户表单
    if request.method == 'GET':
        return render_template('add_user.html')
    # 如果是POST请求，获取表单数据并插入数据库
    else:
        # 获取表单数据
        id=request.form.get('id')
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        permission = request.form.get('permission')
        # 检查用户名是否已存在
        sql = 'select * from users where id=%s'
        cursor.execute(sql, id)
        result = cursor.fetchone()
        if result:
            # 如果用户名已存在，显示提示信息并返回添加用户表单
            flash('用户id已存在，请重新输入')
            return render_template('add_user.html')
        else:
            # 如果用户名不存在，插入数据库并提交
            sql = 'insert into users (id,username, password, role, permission) values (%s,%s, %s, %s, %s)'
            cursor.execute(sql, (id, username, password, role, permission))
            db.commit()
            # 显示提示信息并重定向到用户管理页面
            flash('添加用户成功')
            return redirect(url_for('user'))

# 定义修改用户路由
@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    # 如果是GET请求，查询用户信息并渲染修改用户表单
    if request.method == 'GET':
        # 查询用户信息
        sql = 'select * from users where id=%s'
        cursor.execute(sql, id)
        user = cursor.fetchone()
        # 渲染修改用户表单
        return render_template('edit_user.html', user=user)
    # 如果是POST请求，获取表单数据并更新数据库
    else:
        # 获取表单数据
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        permission = request.form.get('permission')
        # 更新数据库并提交
        sql = 'update users set username=%s, password=%s, role=%s, permission=%s where id=%s'
        cursor.execute(sql, (username, password, role, permission, id))
        db.commit()
        # 显示提示信息并重定向到用户管理页面
        flash('修改用户成功')
        return redirect(url_for('user'))

# 定义删除用户路由
@app.route('/user/delete/<int:id>')
def delete_user(id):
    # 删除用户信息
    sql = 'delete from users where id=%s'
    cursor.execute(sql, id)
    db.commit()
    # 显示提示信息并重定向到用户管理页面
    flash('删除用户成功')
    return redirect(url_for('user'))

##
@app.route('/logout')
def logout():
  # 如果用户已登录，清除session，并重定向到登录页面
  if 'username' in session:
    session.pop('username')
    return redirect(url_for('login'))
  # 否则，重定向到首页
  else:
    return redirect(url_for('index'))

# 启动Flask应用
if __name__ == '__main__':
  app.run(debug=True)