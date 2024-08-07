-- 새 테이블 tb_board_comment 생성
CREATE TABLE tb_board_comment (
id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
board_id BIGINT NOT NULL,
user_id BIGINT NOT NULL,
comment varchar(200) NULL,
create_date datetime NOT NULL DEFAULT current_timestamp,
update_date datetime NOT NULL DEFAULT current_timestamp);

-- 테이블에 값들 한번에 삽입(차례대로 자리를 맞추어서 값을 넣어야 한다.)
INSERT INTO TB_BOARD_COMMENT(
BOARD_ID,USER_ID,comment
) VALUES (2,1,'comment'),(2,2,'comment'),(2,3,'comment'),(3,4,'comment'),(3,5,'comment'),
(3,6,'comment'),(4,7,'comment'),(4,8,'comment'),(4,9,'comment'),(4,10,'comment');

-- user_id가 2인 행의 comment의 값을 comment+'-'+id로 수정
UPDATE TB_BOARD_COMMENT 
SET comment = CONCAT(comment, '-', id) 
WHERE USER_ID = 2;

-- board_id가 4인 행을 모두 삭제
DELETE FROM TB_BOARD_COMMENT
	WHERE board_id = 4;
