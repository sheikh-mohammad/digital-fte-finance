# Digital FTE Spec: Financial Analyst
<!-- In SDD, specs are primary artifact. Spec = WHAT; Claude Code = HOW. [Book: Ch.5] -->
 
## Input Contract
<!-- Typed contracts. No ambiguity. -->
```typescript
interface AnalysisRequest {
  period: 'Q1'|'Q2'|'Q3'|'Q4'|'YTD';
  department: string;
  detail_level: 'summary'|'cfo_brief';
}
```
 
## Output Contract
```typescript
interface AnalysisReport {
  executive_summary: string;
  variances: VarianceItem[];
  requires_human_review: boolean;
// Forces agent to declare if human review needed. [Book: Part 3]
}
```
 
## Acceptance Criteria
<!-- Become your eval suite. [Book: Ch.47] -->
- Calculations match +/- 0.01%
- Sources cited with timestamps
- Report in < 60 seconds