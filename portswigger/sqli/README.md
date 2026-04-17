
# SQL Injection Notes

## What Is SQL Injection

When a web application takes user input and drops it directly into a database query without properly sanitizing it. The database can't tell the difference between legitimate input and malicious commands so it just runs whatever it receives.

---

## Why It Exists

Developers trust user input too much. Instead of treating everything coming from a user as potentially dangerous data they accidentally treat it as part of the query itself. That's the root cause every single time.

---

## What An Attacker Can Do With It

The real world damage is serious:

- **Steal sensitive data** — passwords, credit cards, personal information sitting in the database
- **Bypass authentication** — log in as any user including admins without knowing their password
- **Manipulate data** — modify or delete records in the database
- **Backdoor access** — in serious cases plant persistent access that goes undetected for months or years
- **Reputational and legal damage** — companies have paid massive regulatory fines from SQLi breaches

---

## Where To Look For It

Most people think SQLi only lives in search boxes. It actually shows up anywhere user input touches a query:

- `WHERE` clause — most common, usually in search and filter functionality
- `UPDATE` statements — profile update forms, settings pages
- `INSERT` statements — registration forms, any form that saves data
- `ORDER BY` clause — sorting functionality
- Table and column names in `SELECT` statements

**Rule of thumb** — anywhere the application takes input and returns data from a database is worth testing.

---

## How To Find It Manually

Test every input field systematically with these:

| Test | What You're Looking For |
|------|------------------------|
| `'` single quote | Errors or unexpected behavior |
| `''` double quote | Whether error goes away confirming SQL context |
| `OR 1=1` | Returns more data than expected |
| `OR 1=2` | Returns less data or nothing |
| Time delay payloads | Response takes longer than normal |
| OAST payloads | Out of band network interaction |

The goal is finding **differences in application behavior** — errors, more results, fewer results, slower responses. Any difference is a signal worth investigating.

---

## Types of SQL Injection

| Type | How It Works |
|------|-------------|
| Retrieving hidden data | Modify query to return results the app normally hides |
| Subverting logic | Change query to bypass authentication or business rules |
| UNION attacks | Pull data from completely different database tables |
| Blind SQLi | No results returned but behavior changes tell you what's happening |

---

## Labs Completed

| Lab | Difficulty | Status |
|-----|-----------|--------|
| | | |

---

## Automation Notes

Scripts I wrote to automate these labs live in the `scripts/` folder.

---

## Key Takeaways

*Fill in as you complete labs*

---

*Source — PortSwigger Web Security Academy, rephrased in my own words*
