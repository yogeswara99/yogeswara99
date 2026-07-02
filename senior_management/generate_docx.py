import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from build_docx import build_resume

OUT = os.path.join(os.path.dirname(__file__), 'export')

LANGUAGES = "English (Full Professional)  |  Hindi (Fluent)  |  Telugu (Native)  |  Arabic (Elementary)  |  Malayalam (Conversational)  |  Tamil (Conversational)"

EDU = [
    {"degree": "Bachelor of Technology, Electrical and Electronics Engineering (Distinction)",
     "school": "Amrita School of Engineering, Amrita Vishwa Vidyapeetham", "dates": "2010 - 2014"},
    {"degree": "Post Graduate Diploma, Business Administration - Marketing (Distinction)",
     "school": "Symbiosis Centre for Distance Learning", "dates": "2019 - 2021"},
]

# ---------------------------------------------------------------- MASTER
build_resume(
    filename=f"{OUT}/resume_master_general.docx",
    navy="14213D", accent="B08D57",
    name="Yogeswara Reddy Gondesi",
    title_line="Regional Sales Director  |  Channel & Business Development Leadership  |  MENA",
    proof_items=[
        "**11+ yrs** total career / **6+ yrs** in management",
        "**8 countries** - GCC, Levant & North Africa",
        "**15-20%** YoY channel revenue growth",
        "**15+ partner** distributor network owned",
        "**15-person** front-line sales force led (4 direct + distributor teams)",
        "**€5M** annual distributor agreement portfolio",
        "**€1.2M** largest single order negotiated",
        "Reports to **Management Board** (Germany HQ)",
    ],
    summary=(
        "Regional sales and channel leader with **11+ years** building and scaling B2B distribution networks across "
        "the GCC, Levant, and North Africa - including **6+ years in management** roles and **3+ years** at Manager "
        "level directing strategic sales for a multinational manufacturer, reporting directly into the company's "
        "global Management Board in Germany. Leads a **4-person in-house team** and, through weekly performance "
        "reviews, effectively directs a **15-person front-line sales force** spanning in-house and on-ground "
        "distributor sales staff. Proven ability to take a product line from zero market presence to an established, "
        "growing revenue stream, and to deliver sustained **15-20% year-on-year channel revenue growth** and "
        "**20-30% revenue growth** on new product launches through disciplined channel segmentation, partner "
        "development, and CRM-governed pipeline management. Engineering-trained (B.Tech, Electrical & Electronics "
        "Engineering) with a postgraduate business qualification (PG Diploma, Business Administration - Marketing), "
        "bringing equal fluency to technical specification discussions with consultants and EPC contractors, and to "
        "commercial negotiation with distributors and senior stakeholders. Owns commercial negotiation of a "
        "**€5M annual distributor agreement portfolio**, including the largest single order in the portfolio's "
        "regional history at **€1.2M**. Built and led a partner network spanning eight countries, and represented "
        "the business at flagship international exhibitions including Light + Building (Frankfurt) and The Big 5 "
        "(Riyadh). Now seeking a Regional Sales Director, Country Manager, or Head of Business Development mandate "
        "with a top-tier UAE-based organization, to own channel strategy and commercial performance at scale."
    ),
    competencies=[
        "Regional Channel Strategy & P&L Ownership", "Demand Generation and Joint Marketing Initiatives",
        "Distributor Network Development & Governance", "Commercial Negotiation, Pricing & Margin Management",
        "Business Target Agreement (BTA) / AOP Planning", "Credit, Inventory & Working Capital Management",
        "Quarterly Business Reviews & Executive Reporting", "Cross-Functional & Multi-Country Stakeholder Alignment",
        "Go-to-Market Strategy & New Product Launch", "Team Coaching, Enablement & Performance Management",
        "CRM-Led Sales Forecasting (MS Dynamics)", "Market Intelligence & Competitive Positioning",
        "Technical Consultative Selling (EPC / Consultant Engagement)",
    ],
    experience_blocks=[
        {
            "company": "OBO Bettermann Middle East and North Africa FZCO",
            "location": "Dubai, UAE - Electrical Infrastructure Products",
            "roles": [
                {
                    "title": "Manager, Technical & Strategic Sales",
                    "dates": "Apr 2023 - Present",
                    "bullets": [
                        "Own regional sales strategy across **8 MENA markets** (UAE, Kuwait, KSA, Qatar, Bahrain, Oman, Egypt, Lebanon), directing channel segmentation, partner development, and performance-based programs - delivering **15-20% year-on-year channel revenue growth**.",
                        "Lead and develop a **15+ distributor partner network** through structured Quarterly Business Reviews (QBRs), aligning partners to annual sales targets, joint demand-generation programs, and CRM-disciplined (MS Dynamics) forecasting.",
                        "Directed go-to-market execution for **3 major new product launches**, combining competitive analysis and pricing strategy to enter previously untapped segments - **20-30% revenue growth** in each new category within its first year.",
                        "Own commercial negotiation of a distributor agreement portfolio worth **€5M annually** - pricing, margin protection, credit terms, inventory and working-capital policy - sustaining long-term partnerships across highly competitive markets; personally negotiated and closed the largest single order in the portfolio's regional history at **€1.2M**.",
                        "Present regional performance, forecasts, and strategic recommendations directly to senior international leadership, including the company's **Management Board in Germany**, on channel health, investment priorities, and growth strategy.",
                        "Lead a **4-person in-house team** and, through weekly performance reviews, effectively direct a **15-person front-line sales force** (in-house plus on-ground distributor sales staff), coaching capability through structured training programs spanning technical product knowledge, consultative selling, and CRM discipline.",
                    ],
                },
                {
                    "title": "Assistant Manager, Technical & Sales",
                    "dates": "Jan 2020 - Apr 2023",
                    "bullets": [
                        "Built a new product vertical from **zero market presence** to an established, sustainably growing revenue line within three years - reaching **~70% of annual sales target by Year 3** - appointing and developing **7+ new distribution partners** across the region in the process.",
                        "Established sub-distribution and retail partner channels across the UAE, growing the active partner base by **~20%** and opening market penetration into product categories the network had not previously served.",
                        "Partnered with the Regional Director on market intelligence, competitive analysis, and pricing strategy feeding directly into annual business planning and Management Board presentations in Germany.",
                        "Represented the company at flagship international trade exhibitions - Light + Building (Frankfurt) and The Big 5 (Riyadh) - generating new distributor relationships and reinforcing brand presence regionally.",
                    ],
                },
            ],
        },
    ],
    early_career={
        "lines": [
            "Senior Technical Sales Engineer / Technical Sales Engineer, OBO Bettermann MENA FZCO - Jan 2018 - Dec 2019",
            "Senior Sales Engineer / Sales Engineer, Cupra International, Dubai - Nov 2014 - Dec 2017",
        ],
        "note": "Built the technical credibility and regional consultant/contractor network - spanning earthing, lightning protection, and surge protection systems - that became the foundation for the distribution and channel leadership scope of subsequent management roles.",
    },
    skills_line="CRM Pipeline Management (MS Dynamics)  |  Sales Forecasting & Reporting  |  Channel & Distributor Management  |  Contract Negotiation  |  Power BI  |  Tableau  |  Python & SQL  |  AI / Machine Learning  |  AutoCAD  |  MS Project",
    education=EDU,
    certifications=[
        "PMP® Certification Training - The Knowledge Academy",
        "Lean Six Sigma Green & Yellow Belt - The Knowledge Academy (Black Belt in progress)",
        "Advanced Certification in Artificial Intelligence and Machine Learning - IIT Kanpur (2022-2023)",
        "Certified Data Scientist - Edvancer Eduventures",
    ],
    languages=LANGUAGES,
)

# --------------------------------------------------------- ELECTRICAL
build_resume(
    filename=f"{OUT}/resume_electrical_infrastructure.docx",
    navy="1C2B39", accent="2C6E9E",
    name="Yogeswara Reddy Gondesi",
    title_line="Regional Sales Director  |  Power Distribution & Electrical Infrastructure  |  Middle East",
    proof_items=[
        "**11+ yrs** electrical infrastructure sales / **6+ yrs** management",
        "B.Tech **Electrical & Electronics Engineering**",
        "**15-20%** YoY channel revenue growth",
        "Earthing, Lightning & Surge Protection (**IEC 62305, IEEE Std. 80**)",
        "**8-country** distributor network",
        "**15-person** front-line sales force led (4 direct + distributor teams)",
        "**€5M** annual distributor agreement portfolio / **€1.2M** largest single order",
    ],
    summary=(
        "Regional Sales Director-track leader with **11+ years** building and leading electrical product "
        "distribution networks across the Middle East, including **6+ years** in management and **3+ years** at "
        "Manager level directing strategic sales for a multinational electrical infrastructure manufacturer, "
        "leading a **4-person in-house team** and, through weekly performance reviews, effectively directing a "
        "**15-person front-line sales force** spanning in-house and on-ground distributor staff. Bachelor of "
        "Technology in Electrical and Electronics Engineering (Distinction) provides the technical grounding to "
        "represent power distribution, earthing, lightning protection, and surge protection systems (**IEC 62305, "
        "IEEE Std. 80**) directly to consultants, EPC contractors, and end customers across the region. Proven track "
        "record in distribution channel strategy, partner appointment and development, channel segmentation and "
        "coverage modelling, and performance-based partner programs - delivering **15-20% year-on-year channel "
        "revenue growth** and **20-30% revenue growth** on new product launches. Skilled in quarterly business "
        "reviews, distributor sales-team training, commercial negotiation, inventory and working-capital "
        "management, and credit governance across an eight-country distributor network - owning a **€5M annual "
        "distributor agreement portfolio** and personally negotiating the largest single order in the portfolio's "
        "regional history at **€1.2M**. Reports directly to senior international leadership, including the "
        "company's Management Board in Germany."
    ),
    competencies=[
        "Distribution Channel Strategy & Execution", "Distributor Sales Team Training & Enablement",
        "Partner Identification, Appointment & Development", "Commercial Negotiation & Annual Agreement Management",
        "Channel Segmentation & Coverage Modelling", "Inventory Management & Working Capital Optimisation",
        "Performance-Based Partner Programs", "Credit Management & Sales Policy Compliance",
        "Annual Sales Target Delivery & Revenue Management", "Market & Competitive Analysis, Pricing Strategy",
        "Quarterly Business Reviews (QBRs) with Key Distributors", "EPC / Consultant / Contractor Technical Engagement",
    ],
    experience_blocks=[
        {
            "company": "OBO Bettermann Middle East and North Africa FZCO",
            "location": "Dubai, UAE - Electrical Infrastructure Products",
            "roles": [
                {
                    "title": "Manager, Technical & Strategic Sales",
                    "dates": "Apr 2023 - Present",
                    "bullets": [
                        "Develop and execute distribution strategy aligned with regional business goals across **8 Middle East markets** (UAE, Kuwait, KSA, Qatar, Bahrain, Oman, Egypt, Lebanon) - defining channel segmentation, coverage models, and performance-based partner programs for electrical infrastructure products across construction, industrial, and infrastructure verticals.",
                        "Identify, appoint, and develop new distribution partners in untapped market segments; lead a **15+ distributor partner network** through structured quarterly business reviews (QBRs) aligned to annual sales targets and joint demand-generation initiatives.",
                        "Deliver annual sales targets through country-level sales plans, monitoring pipeline and forecast accuracy via CRM (MS Dynamics) - achieving **15-20% year-on-year channel revenue growth**.",
                        "Execute go-to-market strategies for **3 major new product launches**, combining competitive analysis and pricing strategy to enter previously untapped segments - **20-30% revenue growth** in each new category within its first year.",
                        "Negotiate a distributor agreement portfolio worth **€5M annually** - pricing strategy, margin protection, credit management, inventory levels, and working-capital optimisation - across competitive Middle East markets; personally negotiated and closed the largest single order in the portfolio's regional history at **€1.2M**.",
                        "Support project business through the distributor network, engaging directly with consultants and contractors on technical specifications to strengthen brand positioning and drive specification wins on competitive projects.",
                        "Lead a **4-person in-house team** and, through weekly performance reviews, effectively direct a **15-person front-line sales force** (in-house plus on-ground distributor sales staff) against monthly and annual KPI targets.",
                        "Present regional distribution performance, forecasts, and strategic recommendations to senior international leadership including the **Management Board in Germany**.",
                    ],
                },
                {
                    "title": "Assistant Manager, Technical & Sales",
                    "dates": "Jan 2020 - Apr 2023",
                    "bullets": [
                        "Built distribution network from **zero** for the TBS product vertical across the Middle East - appointing and developing **7+ new distribution partners**, defining channel segmentation and coverage models, and reaching **~70% of annual sales target by Year 3**.",
                        "Established sub-distribution channels and retail partnerships across the UAE, growing active partner count by **~20%** and expanding into product categories previously not served by the network.",
                        "Represented OBO Bettermann MENA at major international exhibitions, including **Light + Building** (Frankfurt, Germany) and **The Big 5** (Riyadh, KSA) - generating new distributor relationships and reinforcing regional brand presence.",
                        "Conducted technical site visits, inspections, and surveys with regional partners to assess customer requirements and propose appropriate earthing, lightning, and surge protection solutions.",
                    ],
                },
            ],
        },
    ],
    early_career={
        "lines": [
            "Senior Technical Sales Engineer / Technical Sales Engineer, OBO Bettermann MENA FZCO - Jan 2018 - Dec 2019",
            "Senior Sales Engineer / Sales Engineer, Cupra International, Dubai - Nov 2014 - Dec 2017",
        ],
        "note": "Served as technical specialist for distribution partners, consultants, and EPC contractors on earthing, lightning protection, and surge protection systems - building the channel credibility and regional client network that underpins the subsequent distribution management career.",
    },
    skills_line="Electrical Systems & Power Distribution  |  Earthing & Lightning Protection (IEC 62305, IEEE Std. 80)  |  Surge Protection Devices  |  Industrial Controls & Infrastructure  |  CRM Pipeline Management (MS Dynamics)  |  Sales Forecasting & Reporting  |  Power BI  |  Tableau  |  AutoCAD  |  MS Project",
    education=EDU,
    certifications=[
        "PMP® Certification Training - The Knowledge Academy",
        "Lean Six Sigma Green & Yellow Belt - The Knowledge Academy (Black Belt in progress)",
        "Advanced Certification in Artificial Intelligence and Machine Learning - IIT Kanpur (2022-2023)",
    ],
    languages=LANGUAGES,
)

# ---------------------------------------------------------- ENERGY TRANSITION
build_resume(
    filename=f"{OUT}/resume_energy_transition.docx",
    navy="143332", accent="0E8A7D",
    name="Yogeswara Reddy Gondesi",
    title_line="Director, Business Development  |  Energy Transition & Industrial Electrification  |  MENA",
    proof_items=[
        "**11+ yrs** industrial B2B channel leadership",
        "Certified: **Green Hydrogen, Green Ammonia & Renewable Energy** (IESD India)",
        "**15-20%** YoY channel revenue growth",
        "B.Tech **Electrical & Electronics Engineering**",
        "**15-person** front-line sales force led (4 direct + distributor teams)",
        "**€5M** annual distributor agreement portfolio / **€1.2M** largest single order",
        "Reports to **Management Board** (Germany HQ)",
    ],
    summary=(
        "Industrial B2B sales and channel leader with **11+ years** building distribution and client networks across "
        "the GCC, Levant, and North Africa, now building toward Director-level roles at the intersection of "
        "industrial channel leadership and the region's energy transition. Currently Manager, Technical & Strategic "
        "Sales for a multinational electrical infrastructure manufacturer, owning a **15+ partner distributor "
        "network** across 8 countries and delivering **15-20% year-on-year channel revenue growth**, with direct "
        "reporting exposure to senior international leadership including the company's Management Board in Germany. "
        "Leads a **4-person in-house team** and, through weekly performance reviews, effectively directs a "
        "**15-person front-line sales force** spanning in-house and on-ground distributor sales staff. "
        "Engineering-trained (B.Tech, Electrical & Electronics Engineering) with a business qualification (PG "
        "Diploma, Business Administration - Marketing) and certification in **Green Hydrogen, Green Ammonia, and "
        "Renewable Energy** (IESD India), bringing both a proven commercial/channel playbook and a deliberately "
        "built technical foundation in decarbonization and industrial electrification to energy-transition client "
        "conversations. Skilled in CRM-governed forecasting, commercial negotiation, and cross-functional "
        "stakeholder alignment across multi-country, matrixed organizations - owning a **€5M annual distributor "
        "agreement portfolio** and personally negotiating the largest single order in the portfolio's regional "
        "history at **€1.2M**, capabilities directly transferable to a technically complex, standards-driven "
        "energy-transition portfolio."
    ),
    competencies=[
        "Energy Transition & Industrial Electrification", "Compliance & Sales Governance",
        "Green Hydrogen & Renewable Energy Fundamentals", "Market Segmentation & Strategic Positioning",
        "Regional Channel Strategy & Distributor Development", "Cross-Functional & Multi-Country Stakeholder Alignment",
        "Business Target Agreement (BTA) / AOP Planning", "Team Coaching, Development & Performance Management",
        "CRM-Led Bookings Forecasting (MS Dynamics)", "Go-to-Market Strategy & New Category Launch",
        "Industrial Client Engagement & Negotiation", "Technical Consultative Selling (EPC / Consultant Engagement)",
    ],
    experience_blocks=[
        {
            "company": "OBO Bettermann Middle East & North Africa FZCO",
            "location": "Dubai, UAE",
            "roles": [
                {
                    "title": "Manager - Technical & Strategic Sales",
                    "dates": "Apr 2023 - Present",
                    "bullets": [
                        "Lead regional sales activities across **8 MENA markets**, developing and executing annual sales targets and channel strategy - achieving **15-20% year-on-year channel revenue growth**.",
                        "Maintain accurate regional forecasts using CRM-driven pipeline management (MS Dynamics); lead a **4-person in-house team** and, through weekly performance reviews, effectively direct a **15-person front-line sales force** (in-house plus on-ground distributor sales staff) to ensure country and regional growth targets are met.",
                        "Manage and enforce sales policies, governance, and compliance procedures across the regional partner network, driving adoption of digital tools to improve pipeline visibility and performance reporting.",
                        "Executed **3 major product launch** go-to-market strategies with **20-30% revenue growth** in new categories - direct, transferable experience for introducing a new (energy-transition) portfolio into an established distributor and client network.",
                        "Lead client engagement, commercial negotiation, and issue resolution at senior levels across the GCC, Levant, and North Africa, owning a **€5M annual distributor agreement portfolio** and personally negotiating the largest single order in the portfolio's regional history at **€1.2M**.",
                        "Present bookings performance, pipeline forecasts, and strategic recommendations to senior international leadership including the company's **Management Board in Germany**.",
                    ],
                },
                {
                    "title": "Assistant Manager - Technical & Sales",
                    "dates": "Jan 2020 - Apr 2023",
                    "bullets": [
                        "Built a new product vertical from **zero market presence** to an established, sustainably growing revenue line within three years - reaching **~70% of annual target by Year 3** - appointing **7+ new distribution partners** across the region.",
                        "Collaborated with the Regional Director on market planning, data analysis, and executive reporting to the company's Management Board in Germany - direct exposure to multi-country governance and performance accountability.",
                        "Represented the company at major international industry exhibitions (Light + Building, Frankfurt; The Big 5, Riyadh), generating new client and partner relationships across the region.",
                    ],
                },
            ],
        },
    ],
    early_career={
        "lines": [
            "Senior Technical Sales Engineer / Technical Sales Engineer, OBO Bettermann MENA FZCO - Jan 2018 - Dec 2019",
            "Senior Sales Engineer / Sales Engineer, Cupra International, Dubai - Nov 2014 - Dec 2017",
        ],
        "note": "Built the industrial client relationships and technical consultative-selling foundation - spanning electrical infrastructure and industrial product categories - that underpins the subsequent channel-leadership career and the pivot toward energy-transition client engagement.",
    },
    skills_line="Green Hydrogen & Green Ammonia Fundamentals  |  Renewable Energy  |  CRM Pipeline Management (MS Dynamics)  |  Bookings Forecasting  |  Power BI  |  Tableau  |  Python & SQL  |  AI / Machine Learning  |  MS Project  |  AutoCAD",
    education=EDU,
    certifications=[
        "Green Hydrogen, Green Ammonia & Renewable Energy - IESD India",
        "Advanced Certification in AI & Machine Learning - IIT Kanpur (2022-2023)",
        "PMP® Certification Training - The Knowledge Academy",
        "Lean Six Sigma Green & Yellow Belt - The Knowledge Academy (Black Belt in progress)",
    ],
    languages=LANGUAGES,
)

print("ALL DONE")
