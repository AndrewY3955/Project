# Literature review

## Evidence status

Five journal-article records are listed in [`data/intake/papers_template.csv`](../data/intake/papers_template.csv), and six academic PDFs have been uploaded. Papers 1-5 have received full-text reviews; Paper 2 was reviewed from rendered page images because its 34-page PDF has no embedded text. Paper 6 is documented below as supplemental background, not counted as a journal article. The project owner certified the five selected papers' eligibility for the assignment on October 20, 2026. This is the owner's eligibility confirmation; the project did not independently audit each journal's peer-review process. The register structure passed validation after the latest edits.

## Paper summaries

### 1. Kuo, Kuo, and Chen (2022) - full text reviewed

**Citation:** Kuo, T.-C., Kuo, C.-Y., & Chen, L.-W. (2022). Assessing environmental impacts of nanoscale semi-conductor manufacturing from the life cycle assessment perspective. *Resources, Conservation and Recycling, 182*, 106289. https://doi.org/10.1016/j.resconrec.2022.106289

The nine-page article evaluates an embedded nonvolatile memory (eNVM) die using a functional unit of a die by technology node and mask layer. The case covers a confidential memory manufacturer’s two factories, 20 nm, 30 nm, and 40 nm process nodes, and 2018-2020. Its inventory includes electricity, diesel, natural gas, tap water, process gases, chemicals, auxiliary materials, and waste outputs. The authors use SimaPro 9.0 and ReCiPe 2016 (GWP100; IPCC2007) to assess climate change, water use, particulate matter, and mineral/metal resource use.

The paper reports lower impacts in the 20 nm case than in the 30 nm and 40 nm cases, and identifies manufacturing electricity and wafer use as important contributors. It reports reductions over 2018-2020, but the percentage statements in the paper are internally unclear; this review therefore does not repeat a specific percentage. The study is a single confidential case, with data from two factories. The stated boundary is cradle-to-grave for DRAM production; outsourced testing is excluded, and packaging data are identified as future work. These limits prevent generalization to all semiconductor companies, products, or fabs.

This paper supports showing technology node, mask layer, functional unit, and lifecycle boundary beside any product-level environmental indicator. It does not support using the case results as a universal ranking. Full text was reviewed; the paper identifies itself as an accepted full-length journal article, but the journal's peer-review policy was not independently verified.

### 2. Ruberti (2024) - full text reviewed from rendered pages

**Citation:** Ruberti, M. (2024). Environmental performance and trends of the world's semiconductor foundry industry. *Journal of Industrial Ecology, 28*(5), 1183-1197. https://doi.org/10.1111/jiec.13529

The image-only PDF has no embedded text, but the rendered article pages were navigable and readable. The open-access *Journal of Industrial Ecology* research article studies 2012-2021 company disclosures; its sample represents about 70% of global foundry revenue, with six foundries in the common-index comparison. It compiles CSR-report and related company/industry data for production, revenue, R&D, patents, Scope 1/2 GHG, energy, water, wastewater, and general/hazardous waste. To compare differing reported production units, the author constructs a common manufacturing index using wafer area and an approximate 30-mask-layer conversion.

Over 2012-2021, the article reports patents, wafer production, and revenue increases of 400%, 183%, and 172%. Absolute energy use increased 164%, water use 163%, general waste 568%, and hazardous waste 239%. On a per-MI basis, energy and water were broadly stable, hazardous waste rose 20%, and Scope 1/2 GHG emissions declined 32%, mainly attributed to renewable-energy investment. Absolute and normalized trends therefore tell different stories and must not be conflated.

The evidence is disclosure-derived, with known readability/transparency and comparability limits; the sample does not cover the full semiconductor value chain or every foundry. Availability determines which indicators can be compared; F-GHG data were omitted where unavailable, and Scope 3 disclosures were incomplete. The MI depends on conversion assumptions and is not a universal standard. Supporting data are available from the corresponding author on reasonable request; no formal uncertainty/sensitivity analysis was identified in the reviewed sections. The publisher identifies this as an open-access research article; peer-review process was not separately verified. It is relevant to dashboard trend/intensity design but does not justify treating normalized metrics as direct measurements.

### 3. Wang et al. (2023) - full text reviewed

**Citation:** Wang, Q., Huang, N., Chen, Z., Chen, X., Cai, H., & Wu, Y. (2023). Environmental data and facts in the semiconductor manufacturing industry: An unexpected high water and energy consumption situation. *Water Cycle, 4*, 47-54. https://doi.org/10.1016/j.watcyc.2023.01.004

The authors surveyed environmental stewardship information in 2021 or recent CSR/ESG reports for 28 semiconductor corporations selected using published industry information. TSEM's 2021 report was unavailable, so the study used its prior-year information. The article compiles reported water withdrawal and source, energy consumption and source, Scope 1/2 GHG emissions, ultrapure-water (UPW) use, and product-normalized indicators where available.

The 2021 total water withdrawal (7.89 × 10^8 m3) and energy consumption (1.49 × 10^11 kWh) represent 27 corporations. The GHG total (7.15 × 10^7 t CO2e; Scope 1: 2.74 × 10^7 and Scope 2: 4.41 × 10^7 t CO2e) represents 26; the article states that YMTC did not disclose GHG data. Nine corporations reported UPW use, and the product-normalized time series was calculated from data announced by six corporations. These varying denominators are essential context and should not be collapsed into a single coverage claim.

The study is based on corporate disclosures rather than a uniform, independently measured inventory. Reporting years and data availability differ, and the paper does not provide a formal uncertainty or sensitivity analysis in the reviewed text. Use its results as disclosure-derived industry context, not as directly comparable facility observations; none of its aggregates were added to this project's dataset. Full text was reviewed. The article declares funding and no known competing interests; peer-review process was not independently verified.

### 4. Ruberti (2023) - full text reviewed

**Citation:** Ruberti, M. (2023). The chip manufacturing industry: Environmental impacts and eco-efficiency analysis. *Science of the Total Environment, 858*, 159873. https://doi.org/10.1016/j.scitotenv.2022.159873

Ruberti compares six foundries (TSMC, UMC, GlobalFoundries, SMIC, PSMC, and HHS) using environmental and economic data from corporate social responsibility reports. The indicators include revenue, R&D, production, Scope 1 and 2 and fluorinated GHG emissions, energy, water withdrawal, wastewater discharge, and general and hazardous waste. Since company disclosures use different production units, the study calculates a common manufacturing index from wafer area using an assumed average of 45 mask layers, then reports normalized key environmental performance indicators and a comparative eco-efficiency assessment.

The study finds that larger company size, greater revenue per production unit, or more advanced technology do not consistently imply lower per-unit energy, water, waste, wastewater, or GHG impacts. Scope 2 was generally higher than Scope 1 in the compared data. Interpretation is constrained by selective CSR-report availability, the six-fab sample, and the index's simplifying assumptions; the authors excluded Scope 3 because only TSMC and UMC reported it. These disclosure-derived indicators are not independently measured values, and the manufacturing index should not be represented as a universal standard. Full text was reviewed. The article was accepted 27 October 2022 and published online 2 November 2022; peer-review process was not separately verified.

### 5. Frost and Hua (2019) - full text reviewed

**Citation:** Frost, K., & Hua, I. (2019). Quantifying spatiotemporal impacts of the interaction of water scarcity and water use by the global semiconductor manufacturing industry. *Water Resources and Industry, 22*, 100115. https://doi.org/10.1016/j.wri.2019.100115

Frost and Hua estimate direct fab feedwater (FW) and electricity-related water (ERW) withdrawals using Q4 2016 production data. The methods report 1,021 valid production-line records, while the results describe 1,020 analyzed facilities/lines; this internal count discrepancy should be retained rather than silently normalized. They combine technology-specific chip/wafer water and electricity intensities with facility geolocation and regional electricity water-use factors. The authors spatially aggregate the estimates and apply AWaRe scarcity characterization factors to direct FW for 202 watersheds; seasonal variation is also examined.

The analysis reports that electricity-related withdrawals dominate in many cases (10-50 times direct withdrawals in some settings). Nearly 47% of production was located in areas with above-global-average scarcity, and almost 13% in very water-scarce areas. These are modeled estimates, not direct corporate measurements. Production and technology assumptions, regional electricity factors, and potential operation below assumed capacity affect the estimate. The authors describe withdrawals as a conservative proxy that does not capture consumption, recycling/returns, or water quality; their analysis also excludes use-phase ERW and does not fully benchmark modeled facility data against observed facility data. Scarcity-weighted withdrawals are screening indicators, not measurements of physical scarcity or operational risk.

This paper supports clearly separating direct and electricity-related water, spatially and seasonally qualifying water indicators, and labeling modeled impacts separately from company-reported withdrawals. Full text was reviewed. The uploaded PDF confirms the journal and article metadata; peer-review process was not separately documented.

### Supplemental background: Boyd (2009) dissertation - full text reviewed

**Citation:** Boyd, S. B. (2009). *Life-cycle Assessment of Semiconductors* [Doctoral dissertation, University of California, Berkeley]. UC Berkeley Electronic Theses and Dissertations. https://escholarship.org/uc/item/8bv2s63d

This 242-page PhD dissertation develops hybrid life-cycle assessments for CMOS logic, flash memory, and DRAM. It combines process LCA for wafer production, electricity generation, water supply, and selected materials with economic input-output LCA for remaining materials. It examines seven CMOS technology generations, five flash generations, and six DRAM generations, using product-specific functional units and including sensitivity and uncertainty analyses.

The abstract reports that use-phase electricity dominates CMOS life-cycle impacts in all but one assessed category, with results especially sensitive to chip power demand, usage patterns, power-supply efficiency, and chip lifetime. It finds that unabated PFC emissions can substantially increase life-cycle global-warming impacts. For DRAM, declining impacts per GB do not translate to declining impacts for the changing memory requirements of an operating system, highlighting a possible rebound effect and the importance of functional-unit choice.

The thesis is an academic dissertation, not a peer-reviewed journal article, and should not be counted toward the assignment's five selected research papers unless the instructor explicitly accepts dissertations. Its analysis is historical (completed in 2009); it notes difficult-to-obtain life-cycle inventory data for high-purity and specialty chemicals, and uncharacterized fabrication VOCs where impact factors were unavailable. Results provide methodological and historical context, not current fab benchmarks. Full text and institutional repository metadata were reviewed.

## Cross-paper synthesis

The reviewed papers indicate that semiconductor environmental impacts depend on at least three levels of analysis: product/process life-cycle assessment, fab or foundry operational intensity, and geographically distributed water demand. Company disclosures and industry aggregates can support contextual indicators, but their definitions and coverage differ. These studies therefore support a dashboard that prioritizes visible scope and provenance over a single composite score or a simplistic company ranking.

The current seven observations cover some reported energy, water, and emissions indicators but do not reproduce the papers' product life-cycle models, manufacturing indices, water-scarcity factors, or process-level inventories. Do not imply that the dashboard validates or reproduces those studies.

## Literature-stage closeout

- Paper 2's rendered full-text review was completed despite zero embedded text; no replacement file is currently needed. Preserve the caveat that its summary came from visual review of rendered pages.
- Paper 6 is supplemental background, not counted as a peer-reviewed journal article unless the instructor explicitly accepts dissertations.
- The project owner certified Papers 1-5 as eligible for the assignment on October 20, 2026. This records the owner's confirmation and does not claim an independent audit of every journal's peer-review process.
- Register validation passed: five unique IDs and DOIs, twelve populated fields per row, and full-text review status for each paper.
- SHA-256 checks after the reviews: Paper 2 `D85268A3E56E68B728D5A4FCE07212456B2383A6B6B1C1C800D551834CD817F0`; Paper 5 `D2268ED0A9D9BEF83D8C38B79113050291970DF5ACD831E8E8C9374E6CD5FF12`; Paper 6 `0D06CCA9FEF4081B06AFC2B51622AD0CB681562463756EEFE62C9AAFF7FDEEE5`; raw synthetic dataset remains `BF494333C6FAF358B0758692288742F9816A251C55ABA1184FF862501ACE22C3`.
