WITH filtered_member AS
  (-- 사용자의 아이디와 학년 매칭
 SELECT userid,
        grade
   FROM e_member
   WHERE 1=1
     AND grade BETWEEN 3 AND 6 ),
     who_studied AS
  (-- 사용자 중 학습한 사용자만 필터링해서 사용자가 즐긴 콘텐츠와 사용 시간 선택
 SELECT s.userid,
        s.mcode,
        ABS(DATE_DIFF('hour', s.enddate, s.credate)) AS study_hours
   FROM e_study AS s
   INNER JOIN filtered_member AS fm ON s.userid = fm.userid
   WHERE 1=1
     AND s.yyyy = '2022'
     AND s.mm in ('01',
                  '02',
                  '03')-- 여기 달을 수정하면 분기 수정 가능.
),
     common_mcode AS
  (-- 미디어와 테스트 둘 다 제공하는 콘텐츠만 필터링
 SELECT DISTINCT t.mcode
   FROM e_media AS m
   INNER JOIN e_test AS t ON m.mcode = t.mcode),
     temp AS
  (-- 필터링한 콘텐츠 중에서 콘텐츠 별 사용자 수와 학습 시간 합 구하기
 SELECT w.mcode,
        COUNT(DISTINCT w.userid) AS student_count,
        SUM(w.study_hours) AS total_study_hours
   FROM who_studied AS w
   WHERE 1=1
     AND w.mcode IN
       (SELECT mcode
        FROM common_mcode)
   GROUP BY w.mcode), testscores AS
  (-- 문항 수와 정답 수 평균, 점수 평균 구하기
 SELECT mcode,
        AVG(item_count) AS avg_item_count,
        AVG(correct_count) AS avg_correct_count,
        AVG(score) AS avg_score
   FROM e_test
   WHERE 1=1
     AND mcode IN
       (SELECT mcode
        FROM common_mcode)
   GROUP BY mcode),
                      usergrades AS
  (-- 콘텐츠 사용자들의 학년 평균 구하기
 SELECT s.mcode,
        AVG(m.grade) AS avg_grade
   FROM e_study AS s
   INNER JOIN e_member AS m ON s.userid = m.userid
   WHERE 1=1
     AND m.grade BETWEEN 3 AND 6
     AND s.mcode IN
       (SELECT mcode
        FROM common_mcode)
   GROUP BY s.mcode) -- 콘텐츠 코드 매칭해서 최종 결과 구하기

SELECT temp.mcode,
       temp.student_count,
       ROUND(ug.avg_grade, 2) AS avg_user_grade,
       ROUND(temp.total_study_hours, 2) AS total_study_hours,
       ROUND(ts.avg_item_count, 2) AS avg_item_count,
       ROUND(ts.avg_correct_count, 2) AS avg_correct_count,
       ROUND(ts.avg_score, 2) AS avg_score
FROM temp
INNER JOIN testscores AS ts ON temp.mcode = ts.mcode
INNER JOIN usergrades AS ug ON temp.mcode = ug.mcode;