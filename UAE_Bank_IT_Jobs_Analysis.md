# Bank IT Jobs in the UAE — Deep Analysis (Front-End & Back-End)

**Prepared for:** Indira Basava — IT Analyst, ~7 years at TCS (Mainframe application development & production support), Banking & Financial Services domain (Bank of America, JP Morgan Chase), currently UAE-based.
**Date:** July 2026
**Method:** Multi-agent research across UAE job boards (Bayt, Naukrigulf, Indeed UAE, GulfTalent, Glassdoor, Jooble, Salt, efinancialcareers), bank career portals (Emirates NBD, FAB, ADCB, Mashreq, DIB, ADIB, RAKBANK, CBD, Wio, Zand, YAP), vendor/case-study material, and UAE salary guides (Cooper Fitch, Michael Page, Hays). *Note:* most job boards block automated page fetches (HTTP 403), so tool/skill detail is synthesised from search-result excerpts of live listings plus verified careers-portal URLs. Treat named tools as "commonly appearing in real UAE listings," and salary figures as market-indicative, not audited.

---

## 0. How to read this document

The UAE banking-tech job market splits into two engineering families:

- **Front-end / client-side** — the web and mobile channels customers touch (internet banking, mobile apps, dashboards). *Framework-heavy, portfolio-driven, comparatively junior-friendly but crowded.*
- **Back-end / server-side / core-banking** — transactions, ledgers, APIs, integration, batch/EOD, databases. *Domain-gated, higher-paid, harder to fill — and where Indira's mainframe + PL/SQL + BFSI background transfers directly.*

Each role below lists **① Who hires · ② Seniority/frequency · ③ Prerequisite knowledge · ④ IT tools to master · ⑤ Certifications**. Section 5 maps the whole thing onto Indira's profile with a recommendation and a 6–12 month roadmap.

**Headline finding:** For Indira specifically, **back-end / core-banking is decisively the better bet than front-end.** UAE mainframe roles actually pay *above* the general-tech median (~AED 21k/mo avg), and banks are mid-transformation (COBOL→Java, mainframe→cloud) — precisely the environments that pay for people who understand the legacy they're modernising. Front-end would reset her to junior pay (AED 6–9k/mo) and discard her domain strengths.

---

## 1. Market snapshot (2025–2026)

### 1.1 Salary ranges (gross AED — effectively take-home; UAE has no income tax)

| Role | Junior (0–3 yrs) | Mid (3–6 yrs) | Senior (7+ yrs) |
|---|---|---|---|
| Front-end dev (JS/React/Angular) | 6–9k/mo | 10–16k/mo | 15–18k/mo |
| Back-end / Java dev | 10–14k/mo | 14–20k/mo | 22–35k+/mo |
| Core-banking dev (Temenos T24 / Finacle) | 12–16k/mo | 18–24k/mo | 25–35k+/mo |
| **Mainframe dev / prod support** (COBOL/JCL/DB2/IMS) | ~15k/mo | ~21k/mo | ~26k/mo |
| DevOps engineer | 12–14k/mo | 17–24k/mo | 22–28k+/mo |
| Data engineer | 9–13k/mo | 14–20k/mo | 18–28k+/mo |
| QA automation engineer | 8–12k/mo | 13–18k/mo | 18–24k/mo |

Average Dubai software engineer ≈ AED 264k/yr (22k/mo). Banking/tech were flagged as top-paying sectors with 3–5 months' bonus (Cooper Fitch 2025). **The mainframe band sits above the general-tech median** — legacy scarcity keeps it well-paid.

### 1.2 Most in-demand banking IT skills

1. **Cloud (AWS + Azure)** — top salary driver as banks migrate (AWS +25.9%, Azure +18.1% cert premium). AWS dominates fintech/consumer; Azure at Microsoft-stack banks.
2. **Cybersecurity** — CBUAE *mandates* frameworks; CISSP appears in ~78% of senior bank-security postings; 200+ new SOC roles expected in 2026.
3. **Data & AI/ML** — fraud detection, credit scoring, personalisation; ADCB runs production agentic AI.
4. **Core-banking engineering** (Temenos Transact, Finacle, Flexcube) — persistent, hard-to-fill, domain-gated.
5. **Full-stack / modern back-end** (Java/Spring, Node, microservices, APIs) — the most actively recruited mid-level band.

### 1.3 UAE core-banking platform landscape (useful domain signal)

| Bank | Core platform | Notes |
|---|---|---|
| Emirates NBD | **Infosys Finacle** (on Oracle Cloud/OCI) | Core consolidated home + international; Liv digital layer on Sitecore + Azure. |
| First Abu Dhabi Bank (FAB) | **Temenos** (Transact/T24) | Multi-entity across ~12 countries; extending to cloud core + Payments Hub. |
| ADCB | **Temenos** | ADCB Egypt live on Temenos Core + Payments Hub; strong AI (Azure AI Foundry). |
| Mashreq | **Oracle FLEXCUBE** (migrating off Temenos) | Replacing ~40 legacy systems globally; Neo Corp on microservices/API. |
| RAKBANK | Java/Spring microservices + Open Banking APIs | Public developer portal (developer.rakbank.ae); powers YAP. |
| CBD | Oracle Fusion Middleware / BPM on **Azure** | Azure re-platform of app infrastructure. |
| Wio Bank | **Mambu** on Microsoft Azure | Cloud-native, API-first; skill-first hiring. |
| Zand Bank | **Finacle on Azure** | GenAI/blockchain via Alibaba + Ant. |

**Transformation drivers (2025–26):** CBUAE Decree-Law No. 6 of 2025, **Aani** instant payments, **Jaywan** domestic card scheme, **Open Finance** consent rules, Article 149 fraud obligations — all forcing core upgrades, payments-hub modernization, and cloud migration. Mainframe-modernization market growing ~9.7% CAGR (BFSI the largest share).

### 1.4 IT-services firms & hiring realities

- **TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini, Kyndryl** all run UAE onshore ops and are the *primary staffing channel* for bank IT. They **do hire onshore in the UAE**, and often prefer candidates already in-country (visa efficiency, GCC experience) — an edge for Indira.
- **Emiratisation:** mainland firms with 20+ staff in finance face rising UAE-national quotas (penalty AED 108,000 per missing Emirati). In practice quotas are met with customer-facing/HR/business roles, **not deep-technical/legacy engineering** — so skilled expat IT hiring continues where local talent is thin (mainframe, core banking, cloud, security). Being already in-UAE with a transferable visa is an advantage.
- **Visa:** standard employment visa 2 yrs (3 for skilled; 5–10 under Green/Golden). Requires MoHRE-registered sponsor + medical + clean record.

---

## 2. FRONT-END / CLIENT-SIDE ROLES

Two technology camps: **Angular** dominates incumbent big banks (Emirates NBD, Mashreq, FAB, ADCB internal/web portals); **React / Next.js** dominates fintechs and digital banks (Wio); **Flutter** is the leading cross-platform mobile choice, with native **Swift/Kotlin** retained for security-critical flows. Market depth: ~90+ front-end and 100+ mobile listings UAE-wide at any time.

### 2.1 Angular Front-End / UI Developer (internet & digital banking web)
- **① Who hires:** Emirates NBD (confirmed: 4–8 yrs, Angular + React), Mashreq, FAB, ADCB. Backbone role for web banking portals and internal dashboards.
- **② Seniority/frequency:** The single most advertised front-end role at incumbent banks; typically 4–8 yrs.
- **③ Prerequisite knowledge:** TypeScript (advanced), JavaScript ES6+, HTML5, CSS3/SCSS; Angular (v15–19; legacy AngularJS still appears); **RxJS** (reactive), state management **NgRx**; REST/AJAX/JSON, JWT auth, some GraphQL; responsive design, **micro-frontend** architecture; OOP/data structures; UAE-specific **Arabic RTL** layout + **WCAG accessibility**; secure-coding awareness.
- **④ IT tools:** Angular CLI, Nx, Webpack, Gulp, Babel, npm; Jasmine, Karma, Cypress; **Git + Azure DevOps** (very common at UAE banks); AWS/Azure, Docker/K8s (some roles).
- **⑤ Certs/degrees:** CS/SE bachelor's preferred (not always mandatory); cloud certs (AWS/Azure) a plus.

### 2.2 React / JavaScript-TypeScript Developer (fintech & digital-bank web)
- **① Who hires:** Wio Bank (React/Node), digital cross-border payments platforms ("Senior Full-Stack Node.js & React | Leading UAE Bank"), fintechs; Emirates NBD (React alongside Angular).
- **② Seniority/frequency:** Very common in fintech; 4–6 yrs typical, senior 5+.
- **③ Prerequisite knowledge:** Deep JavaScript + TypeScript; React + **Redux/Redux Toolkit** (or Zustand), **TanStack Query**; **Next.js**; Tailwind CSS/SASS; REST + GraphQL, JWT; fintech regulatory/risk awareness; Arabic RTL + WCAG 2.2.
- **④ IT tools:** Webpack, Babel, **Vite**, npm; Git + CI/CD; AWS/Azure, microservices.
- **⑤ Certs/degrees:** CS/SE bachelor's preferred; fintechs (Wio) weight mindset/portfolio as much as credentials.

### 2.3 Mobile App Developer — Flutter (mobile banking / wallets)
- **① Who hires:** Banks + fintechs broadly (dominant cross-platform mobile stack); confirmed listings at Abu Dhabi banks and financial-services firms.
- **② Seniority/frequency:** Very common, growing; 3+ yrs Flutter/Dart, 5+ yrs total mobile for banks.
- **③ Prerequisite knowledge:** Flutter + Dart; secure banking features (digital wallets, payment flows, transaction history); **mobile security: SSL/certificate pinning, root/jailbreak detection, encrypted storage, biometric auth**, aligned to **OWASP Mobile Top 10**; API integration, state management.
- **④ IT tools:** Android Studio, Xcode, VS Code; mobile CI/CD, TestFlight/app-store release; Git; REST/Firebase.
- **⑤ Certs/degrees:** CS bachelor's typical; security awareness valued over formal certs. Roles often bundle visa + medical insurance.

### 2.4 Native iOS (Swift) Developer — banking apps
- **① Who hires:** Banks keeping native apps for security-critical flows (large incumbents), often paired with Android in one req.
- **② Seniority/frequency:** Common; 3–5+ yrs.
- **③ Prerequisite knowledge:** Swift (SwiftUI/UIKit), MVVM; banking security stack — Keychain, Secure Enclave, biometrics (Face/Touch ID), cert/SSL pinning, jailbreak/anti-tamper detection, code obfuscation, MFA; OWASP Mobile Top 10.
- **④ IT tools:** Xcode, Git, CI/CD, TestFlight, XCTest, REST APIs.
- **⑤ Certs/degrees:** CS bachelor's preferred; security depth prized.

### 2.5 Native Android (Kotlin) Developer — banking apps
- **① Who hires:** Same bank/fintech mobile teams as iOS.
- **② Seniority/frequency:** Common; 3+ yrs (5+ for major banks).
- **③ Prerequisite knowledge:** Kotlin, Coroutines/Flow (RxJava a plus); MVVM/MVI/Clean Architecture, Jetpack; XML layouts **and Jetpack Compose** (Material 3, StateFlow); banking security controls; cross-platform familiarity (React Native, Kotlin Multiplatform) a plus.
- **④ IT tools:** Android Studio, Gradle, Git, CI/CD, automated testing, release ops.
- **⑤ Certs/degrees:** CS bachelor's typical; no mandatory cert.

### 2.6 React Native Developer (cross-platform mobile)
- **① Who hires:** Fintechs + some banks wanting one JS codebase; overlaps with React web pool.
- **② Seniority/frequency:** Moderately common; 3+ yrs.
- **③ Prerequisite knowledge:** JavaScript/TypeScript, React + React Native, native-module bridging, API integration, mobile security basics, app-store release.
- **④ IT tools:** Node/npm, Metro bundler, Xcode + Android Studio, Git, CI/CD.
- **⑤ Certs/degrees:** CS bachelor's typical.

### 2.7 UI/UX Developer / Designer (design-to-code)
- **① Who hires:** Commercial Bank of Dubai (confirmed UX role), ADIB, bank/fintech design-system teams.
- **② Seniority/frequency:** Common; 3+ yrs, preferably financial services.
- **③ Prerequisite knowledge:** Figma (primary), Sketch, Adobe XD; design systems/UI libraries; wireframes/prototypes; implementation basics (HTML5/CSS3/JS + a framework); **Open Banking/Open Finance** journeys, consent flows, GCC financial-regulation awareness; accessibility + Arabic RTL.
- **④ IT tools:** Figma/Sketch/Adobe XD; front-end HTML/CSS/JS for handoff.
- **⑤ Certs/degrees:** Design or CS degree; **portfolio matters most**; Arabic a plus.

**Front-end recurring essentials:** JavaScript/TypeScript (web) or Dart/Swift/Kotlin (mobile) · secure coding + OWASP Mobile Top 10 · Git + Azure DevOps · AWS/Azure · Arabic RTL + WCAG accessibility · prior fintech/banking/payments domain as a repeated "plus."
**Career-switcher note:** Banks want 4–8 yrs + existing framework proficiency; direct entry for zero-experience is narrow. Realistic entry = build a React/Angular portfolio → IT-services firm or fintech (Wio is skill-first) → move into a bank. Emiratisation graduate programs are the main no-experience door and are usually reserved for UAE nationals.

---

## 3. BACK-END / SERVER-SIDE / CORE-BANKING ROLES

**Structural finding:** UAE retail/commercial banks have largely moved *off* classic z/OS mainframes onto packaged core platforms (Finacle, FLEXCUBE, Temenos). So direct "mainframe COBOL/JCL/IMS" jobs *at banks* are scarce — that demand sits with IT-services firms doing legacy support and **modernization**. The realistic bridge from a mainframe background is: **(a) core-banking config/dev (T24/Flexcube/Finacle)**, **(b) mainframe modernization (COBOL→Java)**, or **(c) Java/Spring after a deliberate reskill**.

### 3.1 Java / Spring Boot Backend Developer (microservices) — HIGHEST VOLUME
- **① Who hires:** Emirates NBD (cloud-native "Sahab" private cloud, microservices, Kafka), Mashreq, RAKBANK, plus every large bank via SIs; digital banks Zand (Java 17/21, Quarkus or Spring Boot) and Wio (skill-first, banking experience optional).
- **② Seniority/frequency:** The most common back-end posting; 4–6 yrs (mid) to 10+ (lead/architect). Scale/perf experience valued (ENBD ~2,000 TPS, 150M+ calls/day).
- **③ Prerequisite knowledge:** Java 8 → 17/21; Spring Boot / Spring / JPA-Hibernate; REST API design; microservices + event-driven design; reactive programming (fintechs); SQL + NoSQL modeling; DS&A for interviews; banking domain (accounts/payments/ledgers); PCI-DSS + secure coding/OWASP.
- **④ IT tools:** Spring Boot, Apache Camel, Kafka/ActiveMQ/JMS, Docker + Kubernetes/OpenShift, Git, Jenkins/GitLab CI, Maven/Gradle, IntelliJ, cloud (AWS/Azure/OCI), Grafana/Prometheus/ELK.
- **⑤ Certs:** Oracle Java (OCP), Spring Professional, a cloud associate (AWS/Azure).

### 3.2 Core-Banking Developer — Temenos T24 / Transact — STRONGEST DOMAIN MATCH FOR INDIRA
- **① Who hires:** Many UAE/Dubai/Abu Dhabi banks + their SIs (via GulfTalent, Bayt, Naukrigulf, NSI & Bluefin). 30–40 live T24 vacancies typical at any time.
- **② Seniority/frequency:** Very common; L3 developer (5+ yrs) to Technical Specialist (10+ yrs, R22+).
- **③ Prerequisite knowledge:** T24/Transact **AA (Arrangement Architecture)** + **TPH (Temenos Payment Hub)**; **INFOBASIC** programming (version/enquiry routines, template programming, **batch programming, multi-threaded routines** — batch/EOD maps *directly* to a mainframe batch background); **jBASE**; **Oracle SQL/PL-SQL**; Unix/Linux; SOAP/REST integration + **ISO8583**; **EOD operations** + production support.
- **④ IT tools:** **TAFJ** (Temenos App Framework for Java), TAFC, Integration Framework, IBM **WebSphere**, IBM **MQ**, Oracle/MS SQL, Unix/Linux, Java.
- **⑤ Certs:** **Temenos Learning Community (TLC)** certification — the recognised, differentiating credential; Oracle DB + Java certs complement.

### 3.3 Core-Banking Developer — Finacle (Infosys) & FLEXCUBE (Oracle)
- **① Who hires:** Emirates NBD (Finacle — production), Mashreq (FLEXCUBE across MENA); heavily staffed via Infosys/Oracle partner SIs. 80+ Finacle app-dev postings on Bayt UAE.
- **② Seniority/frequency:** Steady; senior "Product Engineer – Finacle" 10+ yrs, developer roles from ~3 yrs.
- **③ Prerequisite knowledge:** *Finacle* — customization & integration, REST API integration, scripting, banking functionality. *FLEXCUBE* — **PL/SQL (core — direct reuse of Indira's skill)**, Java, **Oracle WebLogic**, Flexcube architecture, banking process knowledge; batch/EOD.
- **④ IT tools:** Oracle DB + PL/SQL, WebLogic, Java, REST/SOAP, Unix/Linux, Finacle Scripting/FScript.
- **⑤ Certs:** Vendor product training (Infosys Finacle / Oracle FLEXCUBE); Oracle DB certs.

### 3.4 Mainframe Developer (COBOL / JCL / DB2 / CICS / IMS / z/OS) — NICHE, SI-DRIVEN
- **① Who hires:** Not UAE banks directly, mostly. IT-services firms: **Kyndryl** (Senior Mainframe App Developer, COBOL/z/OS), Synechron, Zone IT Solutions, Dicetek; recruiter pipelines (Salt "CICS/IMS SME"). Indeed UAE ~50+ mainframe/COBOL listings; Naukrigulf ~30 IBM-mainframe vacancies — mostly SI/client roles.
- **② Seniority/frequency:** Low volume, specialist; 2–5 yrs (app dev) to 8+ (IMS system programmer/SME).
- **③ Prerequisite knowledge:** COBOL, JCL, DB2, CICS, IMS/DB, VSAM, z/OS, Agile tooling.
- **④ IT tools:** z/OS, Endevor/ChangeMan, scheduler (CA7/Control-M), File-Aid, Xpediter, DB2 utilities.
- **⑤ Certs:** IBM Z / COBOL credentials.
- **Reality check:** COBOL stays globally in demand (retiring workforce, premium pay), but that demand concentrates in the US/Europe and in *modernization*, not on UAE bank payrolls. In the UAE, treat mainframe as a *bridge into modernization/SI work*, not a long-term bank track.

### 3.5 Mainframe Modernization Engineer (COBOL→Java / replatform) — BEST "USE WHAT I HAVE" PIVOT
- **① Who hires:** Kyndryl (AI-accelerated COBOL-to-Java refactoring; hiring modernization consultants in Dubai), plus TCS, Capgemini, Cognizant, Accenture, AWS Transform partners.
- **③ Prerequisite knowledge:** Deep legacy COBOL/JCL/DB2 (to decompose it) **plus** target Java/Spring Boot + REST APIs; refactoring tooling, test automation, data replication; strangler-fig migration patterns, APIs over legacy (z/OS Connect concepts).
- **④ IT tools:** AWS Transform / Blu Age, Micro Focus/OpenText, Kyndryl refactoring tooling, Java, Kafka, containers.
- **Why it fits:** the only role that *pays* for legacy knowledge while she learns Java — the ideal 12–18 month transition role.

### 3.6 API / Integration Developer (MuleSoft, Kafka, ESB)
- **① Who hires:** Banks + SIs; 120+ MuleSoft postings on UAE Indeed ("MuleSoft Application Support Engineer, banking, 4–8 yrs").
- **③ Prerequisite knowledge:** REST/SOAP/HTTP, Kafka; MuleSoft API-led connectivity, RAML, Mule 4, DataWeave, flow design; ISO20022/ISO8583; OAuth/mTLS security.
- **④ IT tools:** MuleSoft Anypoint, TIBCO, Apache Camel, Kafka, IBM MQ, API gateways.
- **⑤ Certs:** MuleSoft Certified Developer.

### 3.7 Database Developer / DBA — Oracle / PL/SQL — STRONG DIRECT MATCH FOR INDIRA
- **① Who hires:** Banks + SIs (VaporVM, Dicetek, CNS); Naukrigulf ~200+ Oracle PL/SQL and ~250+ DBA Dubai listings; banking domain often "essential."
- **③ Prerequisite knowledge:** Oracle SQL/**PL-SQL** (Indira already has this), performance tuning, Oracle E-Business Suite (some), SQL Server/MongoDB (some), UAE localization.
- **④ IT tools:** Oracle DB, PL/SQL, Toad/SQL Developer, WebLogic; increasingly MongoDB/Postgres.
- **⑤ Certs:** Oracle Certified Professional (OCP DBA/Developer).

### 3.8 .NET / C# Developer
- **① Who hires:** FAB, ADCB, DIB, CBD and SIs; ~77 .NET vacancies UAE (GulfTalent).
- **③ Prerequisite knowledge:** C#, .NET Core, ASP.NET, Web API, SQL Server, microservices, Azure; secure coding/PCI-DSS.
- **④ IT tools:** Visual Studio, .NET Core, SQL Server, Azure DevOps, Git.
- **⑤ Certs:** Microsoft Azure Developer Associate.

### 3.9 Payments / Cards Systems Developer (ISO8583, EMV, SWIFT)
- **① Who hires:** Banks, PSPs, acquirers, fintechs; 190+ SWIFT-payments roles (Indeed/Bayt). "Regional Payments Technical Lead" up to ~AED 20k/mo.
- **③ Prerequisite knowledge:** ISO8583 (auth/clearing/reversals), EMV, POS/ATM processing, **PCI-DSS**, ISO20022, SWIFT; overlaps with Temenos TPH.
- **④ IT tools:** Card switch platforms, HSMs, ISO8583 simulators.

### 3.10 DevOps / Cloud Engineer for banking
- **① Who hires:** Emirates NBD (Sahab private cloud), FAB, all large banks + SIs; 300+ DevOps UAE listings.
- **③ Prerequisite knowledge:** Docker + Kubernetes, CI/CD, IaC (Terraform, Ansible), AWS/Azure/GCP, SRE practices, regulated-cloud security/compliance.
- **④ IT tools:** Docker, Kubernetes/OpenShift, Terraform, Ansible, Jenkins/GitLab, Prometheus/Grafana.
- **⑤ Certs:** CKA, AWS/Azure DevOps, Terraform Associate.

### 3.11 Python / Node.js Backend (fintech-leaning)
- **① Who hires:** Wio, Zand, YAP and fintechs; "Senior Node.js Developer – leading UAE bank" is a live title.
- **③ Prerequisite knowledge:** Python (Django/Flask) or Node.js, REST APIs, microservices, cloud, open-banking APIs.
- **④ IT tools:** Node/npm or Python stack, Docker, cloud, Git, CI/CD.

**Back-end cross-cutting essentials:** microservices/event-driven/REST + batch/EOD · Oracle + PL/SQL dominant, plus SQL Server/MongoDB/Postgres · DS&A for interview loops · **PCI-DSS, ISO 27001, OWASP, UAE Central Bank regs, SWIFT CSP** · domain: accounts, loans, payments, cards, AML/KYC, ledgers, EOD.

---

## 4. Bank-by-bank hiring snapshot

| Bank | Careers portal | Representative IT roles | Stack signals |
|---|---|---|---|
| Emirates NBD | emiratesnbd.com/en/careers · emiratesnbd.talentera.com | Full-stack Java (Spring Boot, Kafka, Angular); Node/React; dedicated tech/digital/data track | Java, Spring Boot, React/Next/Node, Angular, GitLab, Docker, OpenShift, K8s, Jenkins, Spinnaker, Splunk; Oracle/Mongo/Couchbase/Elastic; AWS/Azure/GCP/OCI; Finacle core |
| First Abu Dhabi Bank | bankfab.com/en-ae/about-fab/careers · SmartRecruiters | Data Scientist, IT Security Engineer, software eng; **Ethraa** grad prog (UAE nationals) | Temenos T24; AI + cybersecurity emphasis; hybrid/remote |
| ADCB | adcbcareers.com | Software Engineer (distributed systems, Docker/K8s); **AI Engineer** (agentic AI) | LangGraph, Azure AI Foundry, Orkes Conductor, MCP; Docker/K8s; Temenos; Mawaheb/Ethraa grad tracks |
| Mashreq | mashreq.com/.../careers-portal | Full-stack, UI/UX, digital product (Neo); MGN hubs India/Egypt/Pakistan | Oracle FLEXCUBE core; microservices/API (Neo Corp); AI; **ACE** Emirati grad prog |
| RAKBANK | careers.rakbank.ae | Software Developer, IT Support, Cybersecurity Analyst | Java 8, Spring Boot, J2EE, microservices, REST, Kafka, K8s, AWS; Angular; Open Banking dev portal |
| CBD | cbd.ae/home/contact-us/careers | Senior Dev – Middleware/BPM; Group Lead – Core Apps; IT QA lead | Oracle Fusion Middleware, J2EE, BPM; Azure re-platform |
| DIB | careers.dib.ae | IT Specialist, SysAdmin, Support, Team Leader | Islamic-banking digital transformation |
| ADIB | adib.ae/en/pages/careers | Omni-channel microservice architect; UX/product design | Microservices; digital channels |
| Wio Bank | wio.io | Backend, frontend, DevOps, data, cybersecurity; **National Talent** track | Java/Python/Go/React/Node; AWS/Azure; Mambu core; **skill-first hiring** |
| Zand Bank | zand.ae careers | Senior Backend Engineers (cloud-native) | Finacle on Azure; GenAI/blockchain (Alibaba/Ant) |
| YAP | talent@yap.com | Senior QA, DevOps (remote) | Digital banking app; RAKBANK-powered |

**Most in-demand stacks across banks:** Java + Spring Boot + microservices (near-universal) · Kafka · REST/API-first · React/Next/Node + Angular · Docker/K8s/OpenShift/Jenkins/GitLab · **Azure most common cloud**, AWS strong, OCI at ENBD · Mongo/Couchbase/Elastic · rising AI (ADCB leads) · PCI-DSS/ISO 27001/SOC 2/OWASP.

---

## 5. Candidate fit — Indira Basava

**Profile:** ~7 yrs TCS (Systems Engineer / IT Analyst); mainframe app-dev + production support (JCL, PROC, PARM, IMS DB, CA7, z/OS, IBM Utilities, Endevor, QWS, ISTT, ALM); SQL & PL/SQL; **BFSI domain** (Bank of America, JP Morgan Chase) + ASDA retail; Agile/Scrum, JIRA; B.Tech ECE (2016); UAE-based; wants emerging tech.

### 5.1 How her skills transfer

| Existing skill | Transfers directly to |
|---|---|
| **PL/SQL** | Temenos T24 (Oracle SQL/PL-SQL required), FLEXCUBE (PL/SQL core), Oracle DBA/Developer — *immediate reuse* |
| **Batch / EOD / JCL / CA7 scheduling** | T24 batch programming & EOD, Finacle/Flexcube batch — conceptually identical |
| **Banking domain** | Every core-banking & payments role — the hardest thing to teach, and she has it |
| **IMS DB / DB2 data thinking** | Data modeling for core-banking config and Oracle work |
| **Endevor / change control** | Git + CI/CD discipline |

### 5.2 Roles she's closest to TODAY (best-first)
1. **Mainframe app developer / production-support at a bank's IT-services partner** (Kyndryl, IBM, TCS, DXC) — direct match; ~AED 18–24k/mo mid-level; ~70 UAE openings.
2. **Mainframe modernization consultant** (COBOL/JCL/IMS → Java/cloud) — Kyndryl + big SIs hiring in Dubai; her legacy fluency is the scarce half of the job.
3. **Application / production-support analyst, banking (batch + PL/SQL)** — natural lateral move that keeps her domain value.
4. **Core-banking (Temenos/Finacle) support/analyst** — not a today-match on tooling, but her BFSI domain + SQL make it the highest-ROI adjacent pivot.

### 5.3 Recommendation: BACK-END branch, aimed at banking back-end / core-banking modernization

**Why back-end over front-end:**
- Her PL/SQL, batch/data logic, and IMS/DB2 background map *directly* onto server-side/data work; almost none transfers to front-end.
- Banking's engineering weight is server-side (transactions, integration, batch, APIs, ledgers); bank front-end is comparatively thin and commoditised.
- The market is actively moving COBOL→Java and mainframe→cloud — she can occupy the **bridge role** (understands both sides) that pure-Java or pure-mainframe engineers cannot.
- Front-end junior pay (AED 6–9k) is a step *down* from her mainframe band (~AED 21k); back-end/modernization keeps her at or above it.

A strong domain-leveraged alternative: **Temenos Transact (T24) technical-consultant track** — monetises her banking domain immediately, uses SQL heavily, high demand/hard-to-fill (AED 20–25k+/mo), formal certification available.

### 5.4 6–12 month upskilling roadmap (Back-end / recommended)

- **Months 1–3 — Java + OOP foundation:** Java 17 + OOP → **Oracle Certified Professional, Java SE 17 (1Z0-829)**. Tools: IntelliJ, Maven/Gradle, Git/GitHub, JUnit. (Her SQL means the persistence layer comes fast.)
- **Months 3–6 — Spring & APIs:** Spring Boot REST APIs, Spring Data JPA, Spring Security → Spring Professional prep. **Oracle Database SQL Certified Associate (1Z0-071)** — quick win validating a skill she has. Build 2–3 portfolio projects: a REST banking-style microservice on Oracle/Postgres.
- **Months 6–9 — Cloud + integration:** **AWS Developer or Solutions Architect Associate** (highest UAE cert premium) or Azure AZ-900 → AZ-204 (for Mashreq/Wio Microsoft stack). **Docker + Kubernetes** basics, CI/CD (GitHub Actions/Jenkins), **Apache Kafka**.
- **Months 9–12 — Modernization specialisation (her differentiator):** **AWS Mainframe Modernization** (replatform + COBOL-to-Java) and/or IBM/Kyndryl patterns; APIs over legacy (z/OS Connect), strangler-fig migration. Target title: *Application Modernization Engineer* / *Java Back-end Engineer (Banking)*.
- **Parallel accelerator:** **Temenos Technical Consultant (TLC)** certification — pairs extremely well with Java + her BFSI domain.

**Cert priority order:** Oracle OCP SQL (quick win) → Oracle Java OCP → one cloud associate → Temenos TLC → later Spring Professional.

### 5.5 Honest gaps & how the UAE views a mainframe background
- **Gaps:** no production modern OOP/Java or Spring (biggest gap); no cloud/containers/CI-CD; no public code portfolio (critical for a career-changer — GitHub projects will matter more than the résumé line); B.Tech is ECE not CS (minor at 7 yrs, offset by a cert). Her Agile/Scrum + JIRA + BFSI domain are genuine transferable pluses.
- **Asset vs. legacy:** In UAE **BFSI specifically, mainframe is an asset** — systemic banks run heavy legacy estates *mid-transformation* and pay for people who understand what they're modernising; UAE mainframe pay sits above the general-tech median and modernization demand is rising (~9.7% CAGR, BFSI-led). It reads as "legacy" only in the wrong lane (greenfield digital banks / generic startups).
- **Winning framing:** *"Banking-domain engineer who knows the legacy core AND is building modern Java/cloud skills to modernise it."* That turns her background into the scarce bridge-role asset the UAE market is actively paying for over the next 3–5 years.

---

## 6. Where to apply

**Bank portals:** Emirates NBD (emiratesnbd.talentera.com) · FAB (careers.smartrecruiters.com/FirstAbuDhabiBank) · ADCB (adcbcareers.com) · Mashreq (mashreq.com/…/careers-portal) · RAKBANK (careers.rakbank.ae) · DIB (careers.dib.ae) · ADIB (adib.ae/en/pages/careers) · CBD (cbd.ae/home/contact-us/careers) · Emirates Islamic (emiratesislamic.ae/en/about-us/careers) · Wio (wio.io) · Zand · YAP (talent@yap.com).
**Job boards:** Bayt · Naukrigulf · GulfTalent · Indeed UAE (ae.indeed.com) · efinancialcareers · LinkedIn Jobs UAE · Glassdoor UAE.
**IT-services firms staffing banks (best near-term fit for Indira):** Kyndryl, TCS, Infosys, Wipro, Capgemini, Cognizant, Accenture, Synechron, Dicetek, Zone IT Solutions.

---

*Compiled from a multi-agent sweep of UAE job boards, bank career portals, vendor case studies, and 2025–26 salary guides. Job-board pages are bot-protected, so specific tool/skill detail is synthesised from live-listing search excerpts; salary ranges are market-indicative. Verify current openings and bands directly on the portals above.*
