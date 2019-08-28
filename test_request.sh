#!/bin/bash/


curl -X POST -H "Content-Type: application/json"  -d '{
"loan_amnt": [100], "int_rate": [0.02039], "purpose": ["credit_card"], "grade": ["A"], "annual_inc": [80000.00], "revol_util": [0.05], "emp_length": ["10+ years"], "dti": [1.46], "delinq_2yrs": [0], "home_ownership": ["RENT"]}' http://127.0.0.1:5000/predict/
