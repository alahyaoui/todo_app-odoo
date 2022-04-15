# todo_app-odoo
An odoo module allowing helping team members to distribute tasks among themselves

# Definition
## Enterprise resource planning
Enterprise resource planning (ERP) refers to a type of software that organizations use to manage day-to-day business activities such as accounting, procurement, project management, risk management and compliance, and supply chain operations.

# Usage
## Installation
### Without a ssh key:
```
$ git clone https://github.com/alahyaoui/todo_app-odoo.git
```

### With a ssh key:
```
$ git clone git@github.com:alahyaoui/todo_app-odoo.git
```

### Then you need to install the module
```
$ python <path_to_odoo-bin> --config <path_to_config_file> --init todo_stage
```
#### Where
> - **path_to_odoo-bin** is the path to odoo-bin, odoo-bin is located in odoo src files  
> - **path_to_config_file** it the path to the config file


#### Nota Bene: You need to have odoo installed.  
> You can install the src files from <a href="https://github.com/odoo/odoo">here</a> (recommended)  
> or you can install odoo from <a href="https://www.odoo.com/page/download">here</a>

## Execution
### First time (it will generate a config file with the given config options)
```
$ python odoo-bin --database=<name> --db_user=<user> --db_password=<password> --db_host=<host> --db_port=<port> --config <path_to_config_file> --save
```
#### Where
> - **name** is the database name
> - **user** is the database user name
> - **password** is the database user password
> - **host** is the name of your database server
> - **port** is the database port you're using
> - **path_to_config_file** it the path where you want to store the config file

#### Example:
```
$ python odoo-bin --database=dev01 --db_user=erp --db_password=admin --db_host=localhost --db_port=5432 --config ../../.odoorc --save
```

### Second time (after that the config file has been generated)
```
$ python <path_to_odoo-bin> --config <path_to_config_file>
```

### Final Step
After running the command above go to https://localhost:8069

# Authors
- **Lahyaoui Ayoub**
