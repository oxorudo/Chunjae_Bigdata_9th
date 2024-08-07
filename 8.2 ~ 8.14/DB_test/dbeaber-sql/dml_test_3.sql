-- 유저 데이터 3건 추가하기
INSERT INTO tb_user(
	login_id, login_password, name, address, phone 
) VALUES 
('user4', 'user4', 'ddd', NULL, NULL),
('user5', 'user5', 'eee', NULL, NULL),
('user6', 'user6', 'Fff', NULL, NULL)

-- user.id가 3인 회원의 이름과 작성글의 제목, 내용을 가져오기
SELECT name, title, content
FROM
	tb_user USER -- AS 생략 가능
INNER JOIN tb_board board 
	ON USER.id = board.user_id
WHERE USER.id = 3;

-- 모든 회원 목록과 회원들이 작성한 게시글의 이름, 내용을 가져오기. 이 때, 회원이 작성한 글이 없다면 게시글 목록은 NULL로 표시.
SELECT 
user.id,
	user.login_id,
	user.login_password,
	user.name,
	user.address,
	user.phone,
	user.error_count,
	board.title,
	board.content
FROM
	tb_user user
LEFT OUTER JOIN tb_board board 
	ON USER.id = board.user_id;



