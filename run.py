from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
