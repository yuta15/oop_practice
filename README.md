# oop_practice
オブジェクト指向の勉強用リポジトリ

# 考え方
## ディレクトリ構成
```
.
├── README.md
├── entity
│   ├── __init__.py
│   ├── todo.py
│   └── user.py
├── db_operator
│   ├── database_operator.py
│   └── sqlite3_database_operator.py
├── repository
│   └── todo_repository.py
└── settings
    ├── __init__.py
    └── create_table.py

4 directories, 9 files
```
### entity
Entityを格納するディレクトリ。
基本的にドメインそのものを定義したファイルを格納する。

### repository
Repositoryを格納するディレクトリ
Entity毎のできることを格納する。

### db_operator
DB操作に関するファイルを格納するディレクトリ。
各DBの差分を吸収する。

### settings
ローカル環境の設定やシークレット情報を格納するディレクトリ。