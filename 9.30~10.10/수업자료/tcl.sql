
CREATE TABLE "role1" (
	"role_id" INT,
	"role_name" VARCHAR
);

INSERT INTO "role1" VALUES (1, '학생');

COMMIT;

SELECT *
FROM "role1"
LIMIT 5;

-- TCL 확인 시 DBeaver 설정을 매뉴얼 커밋 모드로 변경하여야 합니다.

-- COMMIT?
INSERT INTO "role1" VALUES (2, '교사');
-- 이 사이에서 role 테이블의 DATA 상태를 확인하면 아직 INSERT 한 내용이 반영되지 않았습니다.
-- COMMIT 을 입력해야만 원하는 내용이 정상적으로 수행됩니다.
COMMIT;

-- ROLLBACK
INSERT INTO "role1" VALUES (3, '친구');
-- SAVEPOINT 없이 ROLLBACK 시 직전 COMMIT 이 있었던 부분까지 뒤로 돌아갑니다.
ROLLBACK;

SELECT *
FROM "role1"
;

-- SAVEPOINT
INSERT INTO "role1" VALUES (4, '부모');
SAVEPOINT "mysave";
INSERT INTO "role1" VALUES (5, 'asdf');
ROLLBACK TO SAVEPOINT "mysave";
INSERT INTO "role1" VALUES (5, '친인척');
COMMIT;




