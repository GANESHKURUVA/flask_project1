from flask import Flask

FAI=Flask(__name__)

@FAI.route('/gani')
def Gani():
    return 'GANESH'



@FAI.route('/mani')
def mani():
    return 'Mani'



@FAI.route('/wish/<name>/')
def wish(name):
    return f'Hello MR/MRS {name}'

if __name__=='__main__':
    FAI.run(debug=True)
    FAI.run(debug=True)
    FAI.run(debug=True,host='192.168.92.151',port=5004)



