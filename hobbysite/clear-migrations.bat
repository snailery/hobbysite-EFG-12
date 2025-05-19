IF EXIST "db.sqlite3" (
    del "db.sqlite3"
)
FOR /d /r . %%d IN (migrations) DO @IF EXIST "%%d" rd /s /q "%%d"