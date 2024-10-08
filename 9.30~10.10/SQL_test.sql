WITH quarter_input AS (
    SELECT '2' AS selected_quarter -- 여기에서 '1', '2', '3', '4' 중 원하는 분기로 수정하세요
),
filtered_member AS ( -- 사용자의 아이디와 학년 매칭
    SELECT
        userid,
        grade
    FROM e_member
    WHERE grade BETWEEN 3 AND 6 -- 3학년 ~ 6학년 대상으로만 제한
),
who_studied AS ( -- 위에서 설정한 분기 동안에 학습한 사용자만 필터링하고 사용자가 즐긴 콘텐츠와 사용 시간 산출
    SELECT
        s.userid, -- 학습한 사용자만 선택하기 위해 e_study의 userid 사용
        s.mcode,
        ABS(DATE_DIFF('hour', s.enddate, s.credate)) AS study_hours -- 학습 시작 시간과 끝난 시간의 차이를 구함. 시간은 양수값이므로 절댓값을 취함
    FROM e_study AS s 
    INNER JOIN filtered_member AS fm ON s.userid = fm.userid
    INNER JOIN quarter_input AS qi ON qi.selected_quarter = CASE  -- 월 데이터에 따라 분기 분류해서 일치하는 분기만 추출
            WHEN s.mm IN ('01', '02', '03') THEN '1'
            WHEN s.mm IN ('04', '05', '06') THEN '2'
            WHEN s.mm IN ('07', '08', '09') THEN '3'
            WHEN s.mm IN ('10', '11', '12') THEN '4'
        END
    WHERE 1=1 
    AND s.yyyy = '2022' -- 2022년 데이터만 선택
),
common_mcode AS ( -- 미디어와 테스트 둘 다 제공하는 콘텐츠만 필터링
    SELECT
        DISTINCT t.mcode
    FROM e_media AS m
    INNER JOIN e_test AS t ON m.mcode = t.mcode -- 미디어와 테스트에 둘 다 존재하는 mcode만을 선택
),
temp AS ( -- 필터링한 콘텐츠 중에서 콘텐츠 별 사용자 수와 학습 시간 합 구하기
    SELECT
        w.mcode,
        COUNT(DISTINCT w.userid) AS student_count, -- 총 이용 학생 수 구하기
        SUM(w.study_hours) AS total_study_hours -- 학습 시간의 합 구하기
    FROM who_studied AS w
    WHERE w.mcode IN (SELECT mcode FROM common_mcode) -- 미디어와 테스트에 둘 다 존재하는 mcode 선택
    GROUP BY w.mcode
),
testscores AS ( -- 문항 수와 정답 수 평균, 점수 평균 구하기
    SELECT
        mcode,
        AVG(item_count) AS avg_item_count, -- 문항 수의 평균
        AVG(correct_count) AS avg_correct_count, -- 정답 문항 수의 평균
        AVG(score) AS avg_score -- 점수 평균
    FROM e_test
    WHERE mcode IN (SELECT mcode FROM common_mcode) -- 미디어와 테스트에 둘 다 존재하는 mcode 선택(위의 temp와 다름)
    GROUP BY mcode
),
usergrades AS ( -- 콘텐츠 사용자들의 학년 평균 구하기
    SELECT
        s.mcode,
        AVG(m.grade) AS avg_grade -- 사용자 학년 평균
    FROM e_study AS s
    INNER JOIN e_member AS m ON s.userid = m.userid -- 학습 이용자로 대상 제한
    WHERE m.grade BETWEEN 3 AND 6
        AND s.mcode IN (SELECT mcode FROM common_mcode) -- 미디어와 테스트에 둘 다 존재하는 mcode 선택
    GROUP BY s.mcode
) -- 콘텐츠 코드 매칭해서 최종 결과 구하기
SELECT
    temp.mcode,
    temp.student_count,
    ROUND(ug.avg_grade, 2) AS avg_user_grade, 
    ROUND(temp.total_study_hours, 2) AS total_study_hours,
    ROUND(ts.avg_item_count, 2) AS avg_item_count,
    ROUND(ts.avg_correct_count, 2) AS avg_correct_count,
    ROUND(ts.avg_score, 2) AS avg_score -- 소수점 둘째자리까지 표현
FROM temp
INNER JOIN testscores AS ts ON temp.mcode = ts.mcode 
INNER JOIN usergrades AS ug ON temp.mcode = ug.mcode -- 평균 관련 지표를 연도, 분기별 데이터로 제한
; 