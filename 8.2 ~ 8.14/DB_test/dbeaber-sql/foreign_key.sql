-- 외래 키(foreign key) : 다른 테이블과의 관계를 맺는다.
-- 테이블 생성하면서 foreign key 지정하기
CREATE TABLE tb_board_comment (
id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
board_id BIGINT NOT NULL,
user_id BIGINT NOT NULL,
comment varchar(200) NULL,
create_date datetime NOT NULL DEFAULT current_timestamp,
update_date datetime NOT NULL DEFAULT current_timestamp
-- FOREIGN KEY	(board_id) REFERENCES tb_board(id)
);

-- 이미 있는 테이블에 foreign key 지정하여 연결하기
ALTER TABLE tb_board  ADD CONSTRAINT
FOREIGN KEY(user_id) REFERENCES tb_user(id);

ALTER TABLE tb_board_comment  ADD CONSTRAINT
FOREIGN KEY	(board_id) REFERENCES tb_board(id);

