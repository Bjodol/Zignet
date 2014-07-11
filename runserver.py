from zignet import controller, db

db.drop_all()
db.create_all()
controller.run(debug=True)