# Week 13 – Programming & Strings: Optional Bonus Features

## Objective

This week, you’ll use your programming and string manipulation skills to add **bonus features**  
to your monitoring system. Choose at least one enhancement to implement.

---

## Suggested Features (Pick 1–2)

1. Count how many times CPU > 80% and display in console  
2. Generate a **text summary report** showing key metrics (average, max, peaks)  
3. (Optional) Simulate sending an email alert when CPU > 90%  
4. (Optional) Save your summary as `summary.txt`  

---

## Example Output

 **System Summary**

Total Records: 120

Average CPU Usage: 31.45%

Maximum CPU Usage: 95.2%

Network DOWN count: 4

Top 3 CPU Peaks: [95.2, 93.6, 90.1]

⚠️ ALERT: 2 records exceeded 90% CPU usage.

---

## Submission Checklist

- [ ] At least one bonus feature implemented  
- [ ] Output printed in console or written to a file  
- [ ] Screenshot or log output included  
- [ ] Code committed and pushed to GitHub

---

## Bonus (Optional)

- Simulate email notification (use `smtplib` or console print)
- Add alert history table into `log.db`
- Create a simple summary text file (`summary.txt`)
