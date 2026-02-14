# Nashville Tech Talent Market Analysis

A data-driven analysis of the Nashville, TN tech job market — built to quantify the rarity and market value of a multi-disciplinary skillset spanning data analytics, AI/ML, MCP, and full-stack development.

> **Methodology:** This analysis was generated using [Cursor](https://cursor.com) with Claude Opus 4.6 (Anthropic) and the [Dice.com MCP server](https://www.dice.com). Live job listings were queried programmatically through the Dice MCP API, salary data was extracted and aggregated, and the findings were compiled into the report and structured data files below. All data reflects the Dice.com job market as of February 14, 2026.

---

## Skill Rarity & Market Value

Joshua's certifications and hands-on experience place him in a remarkably thin talent pool. The index below reflects how scarce each skill is among current Dice.com candidates and job postings.

```
██████████  10/10  Model Context Protocol (MCP)
████████░░   8/10  AI/ML + Data Analytics (combined)
████████░░   8/10  CompTIA Quad-Stack (A+, Data+, Cloud+, Network+)
███████░░░   7/10  Power BI / Data Visualization
███████░░░   7/10  Revenue Forecasting & Profitability Modeling
██████░░░░   6/10  Python (Data/Analytics focus)
██████░░░░   6/10  API Integration (Square, webhooks, custom)
█████░░░░░   5/10  JavaScript / Node.js (for data dashboarding)
```

| Skill | Rarity | Detail |
|-------|:------:|--------|
| **Model Context Protocol (MCP)** | 10/10 | Anthropic's MCP is brand-new (2025–2026). Very few certified practitioners exist. Joshua holds the Anthropic Advanced MCP certification. |
| **AI/ML + Data Analytics** | 8/10 | Strong demand but most postings require 5+ years. Hands-on predictive modeling experience with Cursor AI at an early career stage is uncommon. |
| **CompTIA Quad-Stack** | 8/10 | Breadth across IT fundamentals, data management, cloud architecture, and networking. Very few data analysts also hold Cloud+ and Network+. |
| **Power BI / Data Visualization** | 7/10 | Only 1 Power BI-specific role in Nashville. National demand is strong but local supply of practitioners is thin. |
| **Revenue Forecasting & Profitability Modeling** | 7/10 | Hands-on revenue forecasting for multi-unit retail is a specialized skill rarely found in early-career candidates. |
| **Python (Data/Analytics)** | 6/10 | Python is the #1 language for data analytics. Strong demand, moderate supply. |
| **API Integration** | 6/10 | API-first data extraction is in growing demand. Combining API skills with analytics is a strong differentiator. |
| **JavaScript / Node.js** | 5/10 | Many JS developers exist, but few combine JS with data analytics and dashboard automation. |

The combination is what matters most. Thousands of professionals possess one or two of these skills; almost none hold all of them. The Anthropic Advanced MCP credential alone narrows the field to a handful of practitioners nationally — and Joshua pairs it with four CompTIA certifications, production AI/ML work, and full-stack development experience.

---

## What This Skillset Commands

Based on 115 national and 13 Nashville salary data points:

| Benchmark | Range | Midpoint |
|-----------|-------|:--------:|
| National median | $114,400 – $155,000/yr | $134,700 |
| Nashville average | $119,417 – $145,491/yr | $132,454 |
| **Joshua's ask** | — | **$60,000** |

- **55.5% below** the national median (~$74,700/yr difference)
- **54.7% below** the Nashville average (~$72,454/yr difference)

Individually, each skill area Joshua covers commands:

| Skill Area | Typical Salary Range |
|------------|---------------------|
| Data Analyst | $56K – $213K |
| Python Developer | $83K – $286K |
| AI / ML Engineer | $80K – $257K |
| BI Analyst / Power BI | $62K – $184K |
| MCP / AI Automation | Emerging — very few benchmarks exist |
| Node.js / JavaScript | $101K – $380K |
| Data Scientist | $97K – $237K |
| Data Engineer | $48K – $223K |

A candidate who spans multiple rows of this table — particularly MCP, AI/ML, and analytics together — represents a rare convergence of capability that the market has not yet fully priced.

---

## Current Nashville Openings (Feb 2026)

18 live positions in or near Nashville match Joshua's skills. Every listed salary exceeds the $60K ask — most by a wide margin. These are the roles his skillset qualifies him for, and the rates the market is willing to pay for them.

| Role | Company | Type | Salary |
|------|---------|------|--------|
| Senior Data Analyst | Ascension Health | Hybrid | $70K–$100K |
| SAP Data Analyst | Judge Group | On-Site | $104K–$124K |
| Python Data Azure Engineer | SIAL Technology | Hybrid | DOE |
| Python Analytics Developer | SIAL Technology | Hybrid | DOE |
| Python Analytics Developer | SANS | On-Site | $166K–$208K |
| Team Lead Software (C#/Python) | SIAL Technology | On-Site | DOE |
| AI Engineer | Jobot (AI Startup) | On-Site | $175K–$200K |
| Sr AI Research Engineer | Vanderbilt University | On-Site | DOE |
| Senior BI Analyst | Vaco by Highspring | Hybrid | $135K–$145K |
| Sr. BI Engineer | Vaco by Highspring | Hybrid | $156K–$176K |
| BI Developer | Nobl Q | On-Site | DOE |
| Sr. BI Engineer (Remote) | Vaco by Highspring | Remote | $135K–$166K |
| Business Analyst II | Apex Systems | On-Site | $62K–$70K |
| Sr. Associate – Transaction Analytics | Alvarez & Marsal | On-Site | $130K |
| Power BI Developer/Analyst | OtterBase | On-Site | $90K–$95K |
| Sr Software Engineer | Robert Half | On-Site | $112K–$128K |
| Senior Data Scientist | Oracle | Hybrid | $91K–$199K |
| Data Engineer | Kforce | Hybrid | $124K–$145K |

---

## Data Source

Of **68,718** total tech jobs on Dice.com, **2,214 listings** across 9 skill categories were analyzed. All data was retrieved live on February 14, 2026 via the Dice MCP API. Salary figures are based on posted ranges; hourly rates were annualized at 2,080 hours/year.

## Repository Contents

| File | Description |
|------|-------------|
| `nashville_market_analysis.py` | Python script — data, analysis logic, and report generation |
| `Nashville_Market_Analysis_Executive_Summary.txt` | Plain-text executive summary |
| `nashville_analysis_data.json` | Structured JSON output (candidate, stats, rarity scores, value proposition) |

## Usage

```bash
python3 nashville_market_analysis.py
```

Generates both the executive summary (`.txt`) and structured data (`.json`) in the project root.
