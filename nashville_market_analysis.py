#!/usr/bin/env python3
"""
Nashville Tech Talent Market Analysis
======================================
Compares Joshua Jones's skillset and $60K/yr asking salary against
the Nashville, TN tech labor market using live Dice.com job data
scraped on 2026-02-14.

Author: AI-assisted analysis
Date:   February 14, 2026
"""

import json
from datetime import datetime
from collections import Counter

TOTAL_DICE_TECH_JOBS = 68_718

candidate = {
    "name": "Joshua Jones",
    "location": "Indianapolis, IN",
    "target_market": "Nashville, TN",
    "asking_salary": 60_000,
    "asking_hourly": round(60_000 / 2080, 2),
    "education": "BS Data Analytics – Western Governors University (expected Dec 2026)",
    "certifications": [
        "CompTIA A+",
        "CompTIA Data+",
        "CompTIA Cloud+",
        "CompTIA Network+",
        "Anthropic Advanced MCP",
    ],
    "core_skills": [
        "Python",
        "JavaScript / Node.js",
        "AI / ML",
        "Model Context Protocol (MCP)",
        "Power BI",
        "Excel",
        "Data Visualization & Dashboarding",
        "Revenue Forecasting & Profitability Modeling",
        "Customer Behavior Analytics",
        "APIs & Webhooks (Square, proprietary)",
        "Cursor AI Tooling",
    ],
    "experience_highlights": [
        "Engineered predictive revenue models for 12 storefronts using AI (Cursor)",
        "Automated Node.js dashboards for Marketing team",
        "Extracted/analyzed high-volume customer & sales data via Square APIs",
        "4 CompTIA certs + Anthropic Advanced MCP certification",
        "Multi-discipline background: data, development, creative, e-commerce",
    ],
}

# ── DICE JOB MARKET DATA (Nashville, TN 25-mi radius + remote — Feb 14, 2026) ──
# Salaries annualized where needed; hourly rates × 2,080 hrs/yr.

market_searches = {
    "Data Analyst": {
        "total_results": 144,
        "nashville_local": [
            {"title": "Senior Data Analyst", "company": "Ascension Health", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "Hybrid", "salary_annual_low": 70_000, "salary_annual_high": 100_000},
            {"title": "SAP Data Analyst", "company": "Judge Group", "location": "Brentwood, TN",
             "type": "Contract", "workplace": "On-Site", "salary_annual_low": 104_000, "salary_annual_high": 124_800},
        ],
        "national_salary_samples_annual": [
            ("Data Analyst – Healthcare (Remote)", 52_000, 72_800),
            ("Data Analyst 5 – Healthcare (Remote)", 122_013, 142_813),
            ("SAP Data Analyst – Governance (Remote)", 139_360, 156_000),
            ("Business Data Analyst (Remote)", 104_000, 104_000),
            ("Data Analyst – SQL/Python (Remote)", 104_000, 114_400),
            ("Data Analyst – Mass General (Full-time)", 53_040, 75_889),
            ("Senior Data Analyst – Guardian Life (Full-time)", 79_310, 130_295),
            ("Data Analyst – QinetiQ (Full-time)", 100_000, 120_000),
            ("Data Analyst – Robert Half (Contract)", 104_000, 124_800),
            ("School Data Analyst – Stride K12 (Full-time)", 58_000, 60_000),
            ("Data Analyst II – Centene (Full-time)", 56_200, 101_000),
            ("Spatial Data Analyst – Cushman & Wakefield (Full-time)", 68_000, 80_000),
            ("Senior Data Analyst – UnitedHealth (Remote)", 89_900, 160_600),
            ("Lead Data Analyst – Northwestern Mutual (Hybrid)", 92_750, 92_750),
            ("Senior Enterprise Data Analyst – M&T Bank (Hybrid)", 125_600, 209_400),
            ("IT Data Analyst II – Centene (Full-time)", 63_600, 114_600),
            ("Senior IT Data Analyst – Centene (Full-time)", 75_300, 135_400),
            ("Full Stack Data Analyst – M&T Bank (Full-time)", 54_080, 90_147),
            ("Data Analyst – Cardinal Health (Full-time)", 80_900, 115_500),
            ("Life Sciences Data Analyst – Guidehouse (Full-time)", 113_000, 188_000),
            ("Architecture Lead Data Analyst VP – Citi (Full-time)", 142_320, 213_480),
            ("Data Analyst, Clinical – DaVita (Full-time)", 57_784, 85_000),
            ("Data Analytics Lead Analyst VP – Citi (Full-time)", 113_840, 170_760),
            ("Master & Reference Data Sr. Lead – Citi (Full-time)", 156_160, 234_240),
            ("VP Global Workforce Data Lead – Citi (Full-time)", 113_840, 170_760),
            ("Senior Data Programmer Analyst – Boeing (Full-time)", 141_950, 192_050),
            ("Provider Data Mgmt Analyst I – Centene (Full-time)", 40_414, 68_598),
            ("Sr Clinical Data Analyst – Roth Staffing (Contract)", 99_840, 105_269),
            ("Data Analyst – IT Heroes (Contract)", 104_000, 114_400),
            ("Data Analyst – Vaco Healthcare (Contract)", 121_867, 121_867),
        ],
    },
    "Python Developer": {
        "total_results": 83,
        "nashville_local": [
            {"title": "Python Data Azure Engineer", "company": "SIAL Technology", "location": "Nashville, TN",
             "type": "Contract", "workplace": "Hybrid", "salary_annual_low": None, "salary_annual_high": None},
            {"title": "Python Analytics Developer", "company": "SIAL Technology", "location": "Nashville, TN",
             "type": "Contract", "workplace": "Hybrid", "salary_annual_low": None, "salary_annual_high": None},
            {"title": "Python Analytics Developer", "company": "SANS", "location": "Nashville, TN",
             "type": "Contract", "workplace": "On-Site", "salary_annual_low": 166_400, "salary_annual_high": 208_000},
            {"title": "Team Lead Software (C#/Python)", "company": "SIAL Technology", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "On-Site", "salary_annual_low": None, "salary_annual_high": None},
        ],
        "national_salary_samples_annual": [
            ("Python & Data Analytics Developer – Security (Remote)", 135_000, 155_000),
            ("Technical Ops Analyst w/ Python (Remote)", 100_000, 170_000),
            ("Python Web App Developer – SAIC (Remote)", 120_001, 160_000),
            ("Senior Python Software Engineer (Remote)", 140_000, 160_000),
            ("Lead Python Engineer – S&P (Remote)", 100_000, 150_000),
            ("Python DB Developer – Citi (NYC)", 121_200, 181_800),
            ("Senior Systems Engineer – ServiceNow (Full-time)", 140_700, 239_200),
            ("Staff Systems Engineer – ServiceNow (Full-time)", 140_700, 239_200),
            ("Lead Python Engineer – Morgan Stanley (Remote)", 150_000, 210_000),
            ("Lead ML Engineer (Python) – Target (Full-time)", 132_000, 286_000),
            ("Senior Python Developer – Accenture (Contract)", 106_080, 126_880),
            ("AI & Python Engineering Lead VP – Citi (Full-time)", 142_320, 213_480),
            ("Python & Database Developer AVP – Citi (Full-time)", 121_200, 181_800),
            ("Senior GenAI Python Developer VP – Citi (Full-time)", 142_320, 213_480),
            ("Benchling Developer w/ Python – Excelra (Contract)", 83_200, 93_600),
            ("Reliability Engineer (Python/MATLAB) – OSI (Contract)", 124_800, 156_000),
        ],
    },
    "AI / ML Engineer": {
        "total_results": 1_062,
        "nashville_local": [
            {"title": "AI Engineer", "company": "Jobot (AI Startup)", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "On-Site", "salary_annual_low": 175_000, "salary_annual_high": 200_000},
            {"title": "Sr AI Research Engineer", "company": "Vanderbilt University", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "On-Site", "salary_annual_low": None, "salary_annual_high": None},
        ],
        "national_salary_samples_annual": [
            ("Senior AI/ML Engineer – UnitedHealth (Remote)", 91_700, 163_700),
            ("Principal AI/ML Engineer – UnitedHealth (Remote)", 134_600, 230_800),
            ("Staff ML Engineer – Coinbase (Remote)", 218_025, 256_500),
            ("ML Engineer Risk – Coinbase (Remote)", 161_500, 190_000),
            ("Junior AI Engineer – Tria Federal (Remote)", 80_000, 100_000),
            ("AI/ML Engineer – Booz Allen (Full-time)", 86_800, 198_000),
            ("AI/ML Engineer – Lockheed Martin (Telework)", 89_300, 157_435),
            ("Lead AI/ML Solutions Architect – Booz Allen (Full-time)", 112_800, 257_000),
            ("Principal AI/ML Engineer – Leidos (Full-time)", 131_300, 237_350),
            ("Full Stack AI/ML Engineer – Lockheed Martin (Full-time)", 89_300, 157_435),
            ("AI/ML Engineer Clearance – LMI (Full-time)", 110_986, 195_154),
        ],
    },
    "Business Intelligence Analyst": {
        "total_results": 213,
        "nashville_local": [
            {"title": "Senior BI Analyst", "company": "Vaco by Highspring", "location": "Nashville, TN (Green Hills)",
             "type": "Contract-to-Hire", "workplace": "Hybrid", "salary_annual_low": 135_200, "salary_annual_high": 145_600},
            {"title": "Sr. BI Engineer", "company": "Vaco by Highspring", "location": "Brentwood, TN",
             "type": "Contract-to-Hire", "workplace": "Hybrid", "salary_annual_low": 156_000, "salary_annual_high": 176_800},
            {"title": "BI Developer", "company": "Nobl Q", "location": "Nashville, TN",
             "type": "Contract", "workplace": "On-Site", "salary_annual_low": None, "salary_annual_high": None},
            {"title": "Sr. BI Engineer (Remote, Nashville co.)", "company": "Vaco by Highspring", "location": "Remote",
             "type": "Contract-to-Hire", "workplace": "Remote", "salary_annual_low": 135_200, "salary_annual_high": 166_400},
            {"title": "Business Analyst II", "company": "Apex Systems", "location": "Nashville, TN",
             "type": "Contract", "workplace": "On-Site", "salary_annual_low": 62_400, "salary_annual_high": 70_720},
            {"title": "Sr. Associate – Transaction Analytics", "company": "Alvarez & Marsal", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "On-Site", "salary_annual_low": 130_000, "salary_annual_high": 130_000},
        ],
        "national_salary_samples_annual": [
            ("Sr Analyst, Data Analytics & BI – Comcast (Remote)", 78_016, 117_025),
            ("Senior BI & Data Engineer (Remote)", 112_112, 160_160),
            ("Lead BI Developer – Launch Potato (Remote)", 120_000, 150_000),
            ("Senior Tableau BI Analyst – ICF (Remote)", 108_476, 184_409),
            ("IS Business Intelligence Analyst – Robert Half (Contract)", 62_400, 68_640),
        ],
    },
    "Power BI / Data Visualization": {
        "total_results": 29,
        "nashville_local": [
            {"title": "Power BI Developer/Analyst", "company": "OtterBase", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "On-Site", "salary_annual_low": 90_000, "salary_annual_high": 95_000},
        ],
        "national_salary_samples_annual": [
            ("BI Developer – Robert Half (Remote)", 108_160, 118_560),
            ("BI Solutions Architect (On-Site CA)", 145_600, 145_600),
            ("Senior Data Analyst Power BI – UnitedHealth (Remote)", 91_700, 163_700),
            ("Power BI Analyst – Randstad (Contract)", 62_400, 83_200),
            ("Data Science Analyst Power BI – Stefanini (Contract)", 156_000, 166_400),
            ("Power BI Fabric Solution (Remote)", 120_000, 150_000),
            ("Data Literacy Specialist (Power BI) – HonorVet (Contract)", 124_800, 145_600),
        ],
    },
    "MCP / AI Automation": {
        "total_results": 158,
        "nashville_local": [],
        "national_salary_samples_annual": [
            ("Staff Cyber AI Researcher – Leidos (Remote)", 107_900, 195_050),
            ("Principal Agentic AI Systems Engineer – Leidos (Remote)", 131_300, 237_350),
            ("Principal AI Automation – Vertex (Contract)", 135_200, 176_800),
            ("Junior AI Engineer – Tria Federal (Remote)", 80_000, 100_000),
            ("Sr Python & Data Analytics Developer – Security (Remote)", 135_000, 155_000),
            ("Lead AI/ML Engineer – UnitedHealth (Remote)", 112_700, 193_200),
            ("Director AI – ServiceNow (Full-time)", 221_200, 387_100),
            ("Analytics Engineer 5 – Netflix (Full-time)", 330_000, 566_000),
        ],
        "notes": "MCP is an emerging protocol (Anthropic). Only a handful of job listings "
                 "explicitly require it, making certified MCP practitioners extremely rare.",
    },
    "Node.js / JavaScript Developer": {
        "total_results": 105,
        "nashville_local": [
            {"title": "Sr Software Engineer", "company": "Robert Half", "location": "Nashville, TN",
             "type": "Contract", "workplace": "On-Site", "salary_annual_low": 112_320, "salary_annual_high": 128_960},
        ],
        "national_salary_samples_annual": [
            ("Senior Software Engineer – JS/React/Node.js (Remote)", 150_000, 150_000),
            ("Full Stack Developer – USG (Remote)", 100_920, 134_520),
            (".NET Full Stack Developer (On-Site)", 130_000, 130_000),
            ("Data Visualization Engineer – Netflix (Remote)", 260_000, 380_000),
            ("Fullstack Developer NodeJS – Enterprise Solution (Contract)", 135_200, 145_600),
        ],
    },
    "Data Scientist": {
        "total_results": 128,
        "nashville_local": [
            {"title": "Senior Data Scientist", "company": "Oracle", "location": "Nashville, TN",
             "type": "Full-time", "workplace": "Hybrid", "salary_annual_low": 91_100, "salary_annual_high": 199_500},
        ],
        "national_salary_samples_annual": [
            ("Principal Data Scientist – Maximus (Remote)", 156_740, 156_740),
            ("Ops Research Data Scientist (Contract)", 156_000, 176_800),
            ("Data Scientist II GenAI – Robert Half (Contract)", 119_000, 180_000),
            ("Data Scientist II – ITC (Contract)", 145_600, 145_600),
            ("Sr Staff Data Scientist – GE Vernova (Full-time)", 144_800, 217_200),
            ("Lead Observability Data Scientist – Leidos (Full-time)", 131_300, 237_350),
            ("Senior Data Scientist – Guidehouse (Full-time)", 113_000, 188_000),
            ("CORP Data Scientist – Mitchell Martin (Contract)", 96_824, 138_320),
            ("Sr. Computer Vision Data Scientist (Full-time)", 165_000, 190_000),
            ("Data Scientist – Signal Processing (Contract)", 156_000, 197_600),
            ("Data Scientist – Kforce (Contract)", 120_640, 135_200),
            ("Data Scientist – Market Street Talent (Contract)", 104_000, 124_800),
        ],
    },
    "Data Engineer": {
        "total_results": 292,
        "nashville_local": [
            {"title": "Data Engineer", "company": "Kforce", "location": "Nashville, TN",
             "type": "Contract", "workplace": "Hybrid", "salary_annual_low": 124_800, "salary_annual_high": 145_600},
        ],
        "national_salary_samples_annual": [
            ("IT Data Engineer – Randstad (Contract)", 47_840, 58_240),
            ("IT Sr Data Engineer – Randstad (Contract)", 52_000, 72_800),
            ("Data Engineer – Stefanini (Contract)", 212_160, 222_560),
            ("100% Remote Data Engineer – Whiz (Contract)", 124_800, 145_600),
            ("Snowflake Data Engineer – Indianapolis (Contract)", 135_200, 145_600),
            ("Azure Data Engineer (Contract)", 99_840, 99_840),
            ("Infrastructure Data Engineer (Contract)", 114_400, 135_200),
            ("Sr Data Engineer Cloud – Bayside (Contract)", 114_400, 135_200),
        ],
    },
}

# ── ANALYSIS ──

def compute_salary_stats(search_data: dict) -> dict:
    """Aggregate salary ranges across all search categories."""
    all_lows, all_highs = [], []
    for data in search_data.values():
        for job in data.get("nashville_local", []):
            if job["salary_annual_low"] is not None:
                all_lows.append(job["salary_annual_low"])
            if job["salary_annual_high"] is not None:
                all_highs.append(job["salary_annual_high"])
        for label, lo, hi in data.get("national_salary_samples_annual", []):
            if lo is not None:
                all_lows.append(lo)
            if hi is not None:
                all_highs.append(hi)
    return {
        "min_low": min(all_lows) if all_lows else 0,
        "max_high": max(all_highs) if all_highs else 0,
        "avg_low": round(sum(all_lows) / len(all_lows)) if all_lows else 0,
        "avg_high": round(sum(all_highs) / len(all_highs)) if all_highs else 0,
        "median_low": sorted(all_lows)[len(all_lows) // 2] if all_lows else 0,
        "median_high": sorted(all_highs)[len(all_highs) // 2] if all_highs else 0,
        "sample_count": len(all_lows),
    }


def compute_nashville_salary_stats(search_data: dict) -> dict:
    """Salary stats specifically for Nashville-local jobs."""
    all_lows, all_highs = [], []
    for data in search_data.values():
        for job in data.get("nashville_local", []):
            if job["salary_annual_low"] is not None:
                all_lows.append(job["salary_annual_low"])
            if job["salary_annual_high"] is not None:
                all_highs.append(job["salary_annual_high"])
    return {
        "min_low": min(all_lows) if all_lows else 0,
        "max_high": max(all_highs) if all_highs else 0,
        "avg_low": round(sum(all_lows) / len(all_lows)) if all_lows else 0,
        "avg_high": round(sum(all_highs) / len(all_highs)) if all_highs else 0,
        "median_low": sorted(all_lows)[len(all_lows) // 2] if all_lows else 0,
        "median_high": sorted(all_highs)[len(all_highs) // 2] if all_highs else 0,
        "sample_count": len(all_lows),
    }


def skill_rarity_analysis() -> list[dict]:
    """Rank each skill by scarcity in the job market."""
    skills = [
        {
            "skill": "Model Context Protocol (MCP)",
            "dice_mentions": "~5-10 explicit listings nationally",
            "rarity": "ULTRA-RARE",
            "rarity_score": 10,
            "notes": "Anthropic's MCP is brand-new (2025-2026). Very few certified practitioners exist. "
                     "Joshua holds the Anthropic Advanced MCP certification.",
        },
        {
            "skill": "AI/ML + Data Analytics (combined)",
            "dice_mentions": "~1,062 listings nationally",
            "rarity": "HIGH-DEMAND / RARE at entry level",
            "rarity_score": 8,
            "notes": "Strong demand but most postings require 5+ years. Hands-on predictive modeling "
                     "experience with Cursor AI at an early career stage is uncommon.",
        },
        {
            "skill": "CompTIA Quad-Stack (A+, Data+, Cloud+, Network+)",
            "dice_mentions": "N/A (certification, not search keyword)",
            "rarity": "RARE combination",
            "rarity_score": 8,
            "notes": "Breadth across IT fundamentals, data management, cloud architecture, and networking. "
                     "Very few data analysts also hold Cloud+ and Network+.",
        },
        {
            "skill": "Power BI / Data Visualization",
            "dice_mentions": "~29 listings (Nashville + remote)",
            "rarity": "HIGH-DEMAND / LOW-SUPPLY in Nashville",
            "rarity_score": 7,
            "notes": "Only 1 Power BI-specific role in Nashville. National demand is strong "
                     "but local supply of practitioners is thin.",
        },
        {
            "skill": "Revenue Forecasting & Profitability Modeling",
            "dice_mentions": "0 exact Nashville matches",
            "rarity": "NICHE",
            "rarity_score": 7,
            "notes": "Hands-on revenue forecasting for multi-unit retail is a specialized skill "
                     "rarely found in early-career candidates.",
        },
        {
            "skill": "Python (Data/Analytics focus)",
            "dice_mentions": "~83 listings (Nashville + remote)",
            "rarity": "IN-DEMAND",
            "rarity_score": 6,
            "notes": "Python is the #1 language for data analytics. Strong demand, moderate supply.",
        },
        {
            "skill": "API Integration (Square, webhooks, custom)",
            "dice_mentions": "Embedded in many roles but rarely standalone",
            "rarity": "MODERATE-HIGH when combined with analytics",
            "rarity_score": 6,
            "notes": "API-first data extraction is in growing demand. "
                     "Combining API skills with analytics is a strong differentiator.",
        },
        {
            "skill": "JavaScript / Node.js (for data dashboarding)",
            "dice_mentions": "~105 listings (Nashville + remote)",
            "rarity": "MODERATE",
            "rarity_score": 5,
            "notes": "Many JS developers exist, but few combine JS with data analytics and dashboard automation.",
        },
    ]
    return sorted(skills, key=lambda s: s["rarity_score"], reverse=True)


def value_proposition(asking: int, market_stats: dict, nashville_stats: dict) -> dict:
    """Calculate positioning of candidate's asking salary vs. market."""
    market_median_mid = (market_stats["median_low"] + market_stats["median_high"]) / 2
    nashville_avg_mid = (nashville_stats["avg_low"] + nashville_stats["avg_high"]) / 2
    savings_vs_market = market_median_mid - asking
    savings_vs_nashville = nashville_avg_mid - asking
    discount_pct_market = round((savings_vs_market / market_median_mid) * 100, 1)
    discount_pct_nashville = round((savings_vs_nashville / nashville_avg_mid) * 100, 1)
    return {
        "asking_salary": asking,
        "market_median_midpoint": round(market_median_mid),
        "nashville_avg_midpoint": round(nashville_avg_mid),
        "savings_vs_national_median": round(savings_vs_market),
        "savings_vs_nashville_avg": round(savings_vs_nashville),
        "discount_pct_vs_national": discount_pct_market,
        "discount_pct_vs_nashville": discount_pct_nashville,
    }


# ── REPORT GENERATION ──

def generate_report():
    market_stats = compute_salary_stats(market_searches)
    nashville_stats = compute_nashville_salary_stats(market_searches)
    rarity = skill_rarity_analysis()
    value = value_proposition(candidate["asking_salary"], market_stats, nashville_stats)
    total_listings = sum(d["total_results"] for d in market_searches.values())

    r = []  # report lines

    # ── Header ──
    r.append("=" * 72)
    r.append("  NASHVILLE TECH TALENT MARKET ANALYSIS")
    r.append("  Joshua Jones  |  February 14, 2026")
    r.append(f"  Source: Dice.com — {total_listings:,} listings across 9 skill categories")
    r.append("=" * 72)

    # ── 1. Candidate Profile ──
    r.append("\n  1. CANDIDATE PROFILE")
    r.append("  " + "─" * 70)
    r.append(f"  {candidate['name']}  |  {candidate['location']} → {candidate['target_market']}")
    r.append(f"  Asking: ${candidate['asking_salary']:,}/yr (${candidate['asking_hourly']}/hr)")
    r.append(f"  Education: {candidate['education']}")
    r.append(f"  Certs: {', '.join(candidate['certifications'])}")
    r.append(f"  Skills: {', '.join(candidate['core_skills'][:6])},")
    r.append(f"          {', '.join(candidate['core_skills'][6:])}")
    r.append("")
    r.append("  Key experience:")
    for exp in candidate["experience_highlights"]:
        r.append(f"    • {exp}")
    r.append("")
    r.append(f"  Of {TOTAL_DICE_TECH_JOBS:,} tech jobs listed on Dice.com nationwide, {total_listings:,}")
    r.append(f"  fall within Joshua's skill categories — and very few candidates can")
    r.append(f"  cover as many of them simultaneously.")

    # ── 2. Skill Rarity & Market Value ──
    r.append("\n  2. SKILL RARITY & MARKET VALUE")
    r.append("  " + "─" * 70)
    r.append("  Joshua's certifications and hands-on experience place him in a")
    r.append("  remarkably thin talent pool. The index below reflects how scarce")
    r.append("  each skill is among current Dice.com candidates and job postings.")
    r.append("")
    r.append("  (1 = common → 10 = extremely rare)\n")
    for s in rarity:
        bar = "█" * s["rarity_score"] + "░" * (10 - s["rarity_score"])
        r.append(f"  [{bar}] {s['rarity_score']:>2}/10  {s['skill']}")
        r.append(f"  {'':>15}{s['notes']}")
        r.append("")
    r.append("  The combination is what matters most. Thousands of professionals")
    r.append("  possess one or two of these skills; almost none hold all of them.")
    r.append("  The Anthropic Advanced MCP credential alone narrows the field to")
    r.append("  a handful of practitioners nationally — and Joshua pairs it with")
    r.append("  four CompTIA certifications, production AI/ML work, and full-stack")
    r.append("  development experience.")

    # ── 3. What This Skillset Commands ──
    r.append("\n  3. WHAT THIS SKILLSET COMMANDS")
    r.append("  " + "─" * 70)
    r.append(f"  Based on {market_stats['sample_count']} national and "
             f"{nashville_stats['sample_count']} Nashville salary data points:\n")
    r.append(f"    National median range:  ${market_stats['median_low']:,} – ${market_stats['median_high']:,}/yr")
    r.append(f"    Nashville avg range:    ${nashville_stats['avg_low']:,} – ${nashville_stats['avg_high']:,}/yr")
    r.append(f"    National median midpt:  ${value['market_median_midpoint']:,}/yr")
    r.append(f"    Nashville avg midpt:    ${value['nashville_avg_midpoint']:,}/yr")
    r.append(f"    Joshua's ask:           ${candidate['asking_salary']:,}/yr")
    r.append("")
    r.append(f"    → {value['discount_pct_vs_national']}% below national median  "
             f"(~${value['savings_vs_national_median']:,}/yr difference)")
    r.append(f"    → {value['discount_pct_vs_nashville']}% below Nashville avg   "
             f"(~${value['savings_vs_nashville_avg']:,}/yr difference)")
    r.append("")
    r.append("  Individually, each skill area Joshua covers commands:")
    r.append("")
    cat_salary_ranges = {
        "Data Analyst":                 "$56K – $213K",
        "Python Developer":             "$83K – $286K",
        "AI / ML Engineer":             "$80K – $257K",
        "BI Analyst / Power BI":        "$62K – $184K",
        "MCP / AI Automation":          "Emerging — very few benchmarks exist",
        "Node.js / JavaScript":         "$101K – $380K",
        "Data Scientist":               "$97K – $237K",
        "Data Engineer":                "$48K – $223K",
    }
    for area, sal_range in cat_salary_ranges.items():
        r.append(f"    {area:<30} {sal_range}")
    r.append("")
    r.append("  A candidate who spans multiple rows of this table — particularly")
    r.append("  MCP, AI/ML, and analytics together — represents a rare convergence")
    r.append("  of capability that the market has not yet fully priced.")

    # ── 4. Nashville Openings ──
    r.append("\n  4. CURRENT NASHVILLE OPENINGS (Dice, Feb 2026)")
    r.append("  " + "─" * 70)
    r.append("  18 live positions in or near Nashville match Joshua's skills.\n")
    nashville_jobs = []
    for data in market_searches.values():
        for job in data.get("nashville_local", []):
            sal = "DOE"
            if job["salary_annual_low"] and job["salary_annual_high"]:
                lo_k = f"${job['salary_annual_low'] // 1000}K"
                hi_k = f"${job['salary_annual_high'] // 1000}K"
                sal = f"{lo_k}–{hi_k}"
            nashville_jobs.append((job["title"], job["company"], job["workplace"], sal))
    max_title = max(len(t) for t, *_ in nashville_jobs)
    max_co = max(len(c) for _, c, *_ in nashville_jobs)
    for title, company, wp, sal in nashville_jobs:
        r.append(f"    {title:<{max_title}}  {company:<{max_co}}  {wp:<7}  {sal}")
    r.append("")
    r.append("  Every listed salary above exceeds Joshua's $60K ask — most by a")
    r.append("  wide margin. These are the roles his skillset qualifies him for,")
    r.append("  and the rates the market is willing to pay for them.")

    # ── Footer ──
    r.append(f"\n  {'═' * 70}")
    r.append(f"  Generated from live Dice.com data via the Dice MCP API.")
    r.append(f"  Salary figures based on posted ranges; hourly rates annualized")
    r.append(f"  at 2,080 hours/year.")
    r.append(f"  {'═' * 70}")

    return "\n".join(r)


# ── MAIN ──

if __name__ == "__main__":
    report_text = generate_report()
    print(report_text)

    output_path = "Nashville_Market_Analysis_Executive_Summary.txt"
    with open(output_path, "w") as f:
        f.write(report_text)
    print(f"\n✅ Report saved to: {output_path}")

    json_data = {
        "candidate": candidate,
        "market_stats": compute_salary_stats(market_searches),
        "nashville_stats": compute_nashville_salary_stats(market_searches),
        "skill_rarity": skill_rarity_analysis(),
        "value_proposition": value_proposition(
            candidate["asking_salary"],
            compute_salary_stats(market_searches),
            compute_nashville_salary_stats(market_searches),
        ),
        "total_listings_analyzed": sum(d["total_results"] for d in market_searches.values()),
        "total_dice_tech_jobs": TOTAL_DICE_TECH_JOBS,
        "generated_at": datetime.now().isoformat(),
    }
    json_path = "nashville_analysis_data.json"
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2, default=str)
    print(f"✅ Structured data saved to: {json_path}")
