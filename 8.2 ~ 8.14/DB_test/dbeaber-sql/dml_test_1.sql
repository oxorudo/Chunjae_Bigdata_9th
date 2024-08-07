-- 유저 데이터를 3건 추가.
INSERT INTO tb_user (
	login_id,
	login_password,
	name,
	address,
	phone
) VALUES 
('user1', 'user1', 'aaa', '서울시', NULL),
('user2', 'user2', 'bbb', NULL, '010-1111-111'),
('user3', 'user3', 'ccc', '경기도 안양시', '010-222-2222')

-- 게시판 테이블에 데이터를 10건 추가.
INSERT INTO tb_board(
	title, content, user_id
)
VALUES
('제목 1', '내용입니다.', 1),
('제목 2', '안녕하세요', 2),
('제목 3', '데이터베이스는 재미있어요', 3),
('제목 4', '내용입니다.', 1),
('제목 5', '반갑습니다.', 2),
('제목 6', '오늘은 점심으로 무엇이 좋을까요', 3),
('제목 7', '안녕하세요', 3),
('제목 8', '데이터가 골고루 들어갈 수 있도록 해주세요', 3),
('제목 9', '내용입니다.', 2),
('제목 10', '내용입니다.', 1)

-- 3. id=3인 tb_board 데이터를 검색.
SELECT 
	id, 
	title, 
	content, 
	user_id, 
	create_date, 
	update_date 
FROM 
	tb_board
WHERE id = 3;

-- 전화번호가 없는 회원 데이터에 전화번호 추가
-- 특정 컬럼이 NULL 일경우 찾아오는 방법 : IS NULL
-- 아닐 경우 : IS NOT NULL
SELECT id, login_id FROM tb_user WHERE tb_user.phone IS NULL

UPDATE tb_user SET
	phone = '010-333-3333'
WHERE phone IS NULL

-- 최근에 만들어진 tb_board의 데이터 삭제
DELETE FROM tb_board WHERE id = 10;
