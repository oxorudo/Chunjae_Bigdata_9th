-- join해보기
SELECT * -- 모든 열 선택
FROM
	tb_board AS board -- 애칭 만들기
INNER JOIN tb_board_comment AS comment -- INNER JOIN
	ON board.id = comment.board_id -- board.id가 comment.board_id가 같은 것들을 합침, 행 수가 적은 쪽이 많은 쪽으로 맞춰짐
WHERE board.id = 3; -- board.id가 3인 것만 걸러냄

SELECT *
FROM
	tb_user AS user
LEFT OUTER JOIN tb_board AS board  -- 상위 테이블(왼쪽)을 기준으로 하위(오른쪽) 테이블이 맞춰짐, 합쳐지면서 빈 곳은 null로 채워짐
	ON USER.id = board.user_id;

SELECT *
FROM
	tb_user AS user
RIGHT OUTER JOIN tb_board AS board -- 하위 테이블(오른쪽)을 기준으로 상위(왼쪽) 테이블이 맞춰짐, 합쳐지면서 빈 곳은 null로 채워짐
	ON USER.id = board.user_id;

