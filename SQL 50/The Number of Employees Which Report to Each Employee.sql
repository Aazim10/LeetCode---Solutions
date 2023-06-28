SELECT E.EMPLOYEE_ID, E.NAME, (SELECT COUNT(REPORTS_TO) FROM EMPLOYEES WHERE REPORTS_TO=E.EMPLOYEE_ID) AS REPORTS_COUNT, 
ROUND((SELECT AVG(AGE)FROM EMPLOYEES WHERE REPORTS_TO=E.EMPLOYEE_ID)) AS AVERAGE_AGE
FROM EMPLOYEES E
WHERE E.EMPLOYEE_ID IN (SELECT REPORTS_TO FROM EMPLOYEES)
ORDER BY E.EMPLOYEE_ID;
