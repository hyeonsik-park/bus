from config.config import cursor, db
#데이터베이스 
#정의어,제어어,처리어 가 있다

# -----------테이블 보기----------
'''
cursor.execute("SHOW tables;")
result = cursor.fetchall()
print(result)
'''

#SElECT 문
"""
cursor.execute('SELECT * FROM user')
result = cursor.fetchall()
print(result)
"""

#DELETE 문 ROW 삭제
"""
cursor.execute('DELETE FROM user WHERE id = 3;')
db.commit()
db.close()
"""

#DROP 문 테이블 삭제
"""
cursor.execute('DROP TABLE users_tb')
db.commit()
db.close()
"""

#CREATE 문
"""
cursor.execute(
    '''
    CREATE TABLE tset_table(
    name VARCHAR(255),
    password VARCHAR(255)
    )
    '''
)
db.commit()
db.close()
"""
#CREATE 문 TABLE 생성
'''
cursor.execute(
    """
    CREATE TABLE users_tb(
    id char(36) PRIMARY KEY,
    login_id VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
)
db.commit()
db.close()
'''