# Senior Management Resume Package — UAE Top-Tier Firms

This folder contains everything requested: three tailored Senior Management resumes, and the six-lens diagnostic/optimization analysis behind the decisions made in them.

## Files

| File | What it is |
|---|---|
| `resume_master_general.html` | Sector-agnostic master resume — use this by default, or when applying through a headhunter/recruiter matching you against multiple mandates. |
| `resume_electrical_infrastructure.html` | Tailored for Eaton, Schneider Electric, ABB, Legrand, Hager, Siemens Smart Infrastructure — your strongest natural fit. |
| `resume_energy_transition.html` | Tailored for Siemens Energy, GE Vernova, Honeywell Energy — positioned honestly as a credentialed pivot, not overstated prior tenure. |
| `01_recruiter_diagnostic_report.md` | Raw 10-second-scan + recruiter-mindset assessment of your existing documents (Exercises 1, 2, 6). |
| `02_ats_keyword_optimization.md` | Keyword gap analysis and ATS formatting rules applied (Exercise 3). |
| `03_impact_statement_rebuilder.md` | Before/after bullet rewrites, plus follow-up questions to sharpen further (Exercise 4). |
| `04_market_positioning_notes.md` | How each target-firm cluster hires, and why the three variants are framed the way they are (Exercise 5). |
| `05_linkedin_optimization_guide.md` | Section-by-section LinkedIn rewrite. |
| `export/*.pdf` | Final, ready-to-send PDFs — the designed/colored version of each variant, rendered from the `.html` files. |
| `export/*.docx` | Final, ready-to-send Word versions — same content, rebuilt as a clean, editable, ATS-native Word document (see note below on why these look plainer than the PDFs). |
| `build_docx.py` / `generate_docx.py` | The scripts that generate the `.docx` files, kept for reproducibility if content changes again — run `python3 generate_docx.py` from this folder after editing `generate_docx.py`'s content blocks. |

## How to use the resumes
- **PDF (`export/*.pdf`):** ready to send as-is — this is the fully designed, colored version of each variant, one per sector.
- **DOCX (`export/*.docx`):** ready to send as-is, or to edit directly in Word — deliberately built as a clean, single-column, no-tables-no-textboxes document rather than a literal conversion of the styled HTML/PDF. This is intentional: heavily styled CSS (flex layouts, gradients, background badges) doesn't survive HTML→Word conversion reliably, and many corporate ATS portals and recruiters specifically prefer a plain, simply-formatted Word file over a "designed" one. Content, figures, and wording are identical to the PDF; only the visual styling is simpler.
- The `.html` source files remain in this folder too if you want to regenerate a PDF yourself later (open in a browser, Print → Save as PDF) after any manual edits.

**Title swapping:** each file's `<header>` has an HTML comment listing 3–4 alternate title lines for that variant, matching your four target titles (Regional Sales Director, Country Manager/GM, VP/Head of BD, Channel/Distribution Director). Swap the single `.title` div text to match how a specific job posting titles the role — nothing else needs to change.

## Photo — my recommendation
You asked me to decide rather than guess blind, so: **don't embed a photo in the resume file itself; keep one ready as a separate attachment.**
- All the target firms here (Eaton, Schneider, ABB, Siemens Energy, Honeywell, GE Vernova) are US/European-HQ'd multinationals. Their corporate career sites and ATS systems (Workday, SuccessFactors, Taleo) are built around US/EU hiring norms, where photos are typically *not* expected on the resume itself and can occasionally cause an ATS parser to mis-read the header block.
- In the UAE, local companies and boutique recruiters sometimes do expect a photo — but that's rarely the channel through which you'd reach a Regional Director role at one of these specific MNCs; you're far more likely to go through their corporate portal or an executive-search firm, both of which pull your photo from LinkedIn if they want one, not from the CV.
- Your LinkedIn photo (keep it — it's fine and professional) already covers the "local market expects a face" convention. Keeping the resume itself photo-free maximizes ATS reliability without losing anything, since anyone serious about you will look you up on LinkedIn anyway.
- If you do apply via a specific local recruiter who explicitly asks for a photo on the CV, add a simple `<img>` in the header — the HTML/CSS is built to accommodate one without redesign; just ask and I'll add it to a specific variant.

## Resolved
- **Certification issuer confirmed:** IESD India, for the Green Hydrogen/Green Ammonia/Renewable Energy credential — updated in `resume_energy_transition.html` and no longer a placeholder.
- **Team leadership scope confirmed:** a 4-person in-house team, plus weekly-reviewed oversight of on-ground distributor sales staff — effectively a 15-person front-line sales force. This is now reflected in the proof-strip, summary, and a dedicated bullet in all three resumes.
- **Portfolio size and largest order confirmed:** a €5M annual distributor agreement portfolio, including the largest single order closed at €1.2M. This is now the P&L-scale anchor in the proof-strip, summary, and commercial-negotiation bullet of all three resumes and the LinkedIn About rewrite — it directly answers the "how much business does this person actually own" question that Director/VP-BD-level readers screen for first.

## Open items before final submission
Once you have a live job description for a specific role, send it over — I'll run a one-to-one ATS gap check against that JD rather than the generic mapping in `02_ats_keyword_optimization.md`.

## Note on the existing `resume_eaton.html` / `resume_siemens.html` files in the repo root
Those earlier drafts are what this diagnostic was run against — the inconsistent years-of-experience figures and the unnamed "Industry Certified" credential originated there. The new files in this folder supersede them for senior-management positioning; the originals are left untouched in case you still need them for the specific applications they were built for.
