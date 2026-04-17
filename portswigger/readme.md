# PortSwigger Web Security Academy

## My Approach

Every topic follows the same process:

1. Read all theory before touching any lab
2. Attempt manually first — no tools, just understanding
3. Automate with Python and requests
4. Write notes on why the vulnerability exists
5. Move on only when it genuinely clicks

---

## Progress

| Topic | Labs Completed | Status |
|-------|---------------|--------|
| SQL Injection | 0/18 | 🔄 In Progress |
| Authentication | 0/14 | ⏳ Not Started |
| Path Traversal | 0/6 | ⏳ Not Started |
| Command Injection | 0/5 | ⏳ Not Started |
| Business Logic | 0/11 | ⏳ Not Started |
| Information Disclosure | 0/5 | ⏳ Not Started |
| Access Control | 0/13 | ⏳ Not Started |
| SSRF | 0/7 | ⏳ Not Started |
| XXE Injection | 0/9 | ⏳ Not Started |
| File Upload | 0/7 | ⏳ Not Started |

---

## Structure

```
portswigger/
├── README.md
├── sqli/
│   ├── README.md
│   └── scripts/
├── authentication/
│   ├── README.md
│   └── scripts/
├── path-traversal/
│   ├── README.md
│   └── scripts/
├── command-injection/
│   ├── README.md
│   └── scripts/
├── business-logic/
│   ├── README.md
│   └── scripts/
├── information-disclosure/
│   ├── README.md
│   └── scripts/
├── access-control/
│   ├── README.md
│   └── scripts/
├── ssrf/
│   ├── README.md
│   └── scripts/
├── xxe/
│   ├── README.md
│   └── scripts/
└── file-upload/
    ├── README.md
    └── scripts/
```

---

## Notes Format

Each topic folder contains a README with:

- **What is it** — simple explanation in my own words
- **Why it exists** — root cause of the vulnerability
- **How to find it** — recon and discovery methodology
- **How to exploit it** — step by step approach
- **How to automate it** — Python and requests scripts
- **Real world impact** — what an attacker could actually do
- **Key takeaways** — what I learned

---

## Tools Used

- Burp Suite Community Edition — intercepting and modifying requests
- Python3 + requests — automating exploitation
- Browser dev tools — understanding request structure

---

*All labs completed on PortSwigger's authorized platform only.*
