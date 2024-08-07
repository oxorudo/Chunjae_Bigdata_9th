INSERT INTO tb_board(
-- 테이블을 선택하지 않을 수도 있는데, 그러면 각각 열들을 완벽하게 찾아서 넣어야 한다.
	title, 
	content, 
	user_id
) VALUES (
-- 위의 열에 넣을 값들을 순서를 맞춰서 넣는다.
	'안녕하세요',
	'글 내용 입니다.',
	1
)

UPDATE tb_board SET 
	title = '수정되었습니다.',
	content = '수정된 내용입니다.'
WHERE id = 1
-- 보통 id를 가지고 필터링한다.

SELECT 
    id, title, content 
-- 모든 열을 선택하려면 * 를 사용하면 되는데, 가독성 문제가 있으니 가급적 사용하지 말 것
FROM 
	TB_BOARD
WHERE id = 1

DELETE FROM TB_BOARD
WHERE id = 1
