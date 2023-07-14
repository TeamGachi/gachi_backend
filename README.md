# gachi_backend
## APP Structure
### Authentication
Input : id && password

Output : JWT

### ImageUpload
Input : N 장의 사진

Output : None 

### Classification
Input : 여행세션 id 

Output : 분류된 N장의 사진 

## PostgreSQL 
### Session
결성된 여행 세션 테이블 
* session_id (PK)
* email (fk)
### User
* email (PK)
* password
* name
* gender
* 친구는 key-value 형태의 noSql이 가능하지 않을까?
### Image
* email (fk)
* session_id
* path // 로컬 파일시스템에 저장되어있는 이미지 변수 
