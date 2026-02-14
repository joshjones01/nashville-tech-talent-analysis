# Nashville Tech Talent Market Analysis

A data-driven analysis of the Nashville, TN tech job market — built to quantify the rarity and market value of a multi-disciplinary skillset spanning data analytics, AI/ML, MCP, and full-stack development.

## Key Findings

### Skill Rarity

| Skill | Rarity (1–10) | Notes |
|-------|:---:|-------|
| Model Context Protocol (MCP) | **10** | Ultra-rare. Fewer than 10 Dice listings nationally even mention MCP. |
| AI/ML + Data Analytics | **8** | High demand, but most postings require 5+ yrs. Early-career hands-on experience is uncommon. |
| CompTIA Quad-Stack (A+, Data+, Cloud+, Network+) | **8** | Very few data analysts also hold Cloud+ and Network+. |
| Power BI / Data Visualization | **7** | Only 1 Power BI-specific role in Nashville. National demand is strong, local supply is thin. |
| Revenue Forecasting & Profitability Modeling | **7** | Niche skill rarely found in early-career candidates. |
| Python (Data/Analytics) | **6** | #1 language for data analytics. Strong demand, moderate supply. |
| API Integration (Square, webhooks) | **6** | Growing demand. Combining API skills with analytics is a strong differentiator. |
| JavaScript / Node.js (dashboarding) | **5** | Many JS devs exist, but few combine it with data analytics and dashboard automation. |

Thousands of professionals possess one or two of these skills — almost none hold all of them.

### Salary Benchmarks

Across 115 national and 13 Nashville salary data points from Dice.com:

| Benchmark | Range | Midpoint |
|-----------|-------|:--------:|
| National median | $114,400 – $155,000/yr | $134,700 |
| Nashville average | $119,417 – $145,491/yr | $132,454 |
| **Joshua's ask** | — | **$60,000** |

- **55.5% below** the national median (~$74,700/yr difference)
- **54.7% below** the Nashville average (~$72,454/yr difference)

### Per-Skill Market Rates

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

### Nashville Openings

18 live positions in or near Nashville match this skillset (Feb 2026). Every listed salary exceeds the $60K ask — most by a wide margin.

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

## Data Source

All job data was retrieved live from [Dice.com](https://www.dice.com) on February 14, 2026 via the Dice MCP API. A total of **2,214 listings** were analyzed across 9 skill categories, drawn from a pool of **68,718** total tech jobs nationwide.

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

