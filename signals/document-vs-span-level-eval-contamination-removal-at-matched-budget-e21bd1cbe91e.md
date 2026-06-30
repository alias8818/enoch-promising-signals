# Document vs span-level eval contamination removal at matched budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `document-vs-span-level-eval-contamination-removal-at-matched-budget-e21bd1cbe91e`
Run ID: `document-vs-span-level-eval-contamination-removal-at-matched-budget-e21bd1cbe91e-20260619T135002248509+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/616dd4252f11

## What looked useful

Both document-level and span-level removal reduced synthetic eval leakage accuracy from 1.000 to 0.000. At the same retained-token budget, naive span-level removal preserved colocated utility facts but did not improve total utility over document removal: all-utility accuracy was 0.749 for span-level versus 0.750 for document-level.

## Boundaries and scale limits

Does not test real corpora, fuzzy contamination matching, LLM training, tokenizer-specific budgets, or downstream generalization. Span-level budget matching used random sentence downsampling rather than an optimized retention policy.

## Claim scope

Synthetic exact-span contamination-removal benchmark with 240 documents, 60 contaminated documents, 30 matched-budget downsampling seeds, and exact-probe retrieval scoring.

## Why it stopped

No-paper useful signal: the matched-budget synthetic run found a tradeoff rather than a positive utility gain for naive span-level removal.

## Recommended next action

Run a bounded deepen test comparing random, stratified, and utility-aware span-level budget allocation against document removal on the same synthetic benchmark and one small real-text corpus with known contaminated spans.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-aware span decontamination versus document removal
- Success threshold: Span-level allocation must keep eval leakage accuracy at 0.000 and improve all-utility accuracy over document removal by at least 0.05 absolute across at least 20 seeds or an equivalent confidence interval.
- Stop condition: Stop if all span-level allocation policies remain within +/-0.01 all-utility accuracy of document removal or increase leakage above 0.000 at the matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/document-vs-span-level-eval-contamination-removal-at-matched-budget-e21bd1cbe91e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
