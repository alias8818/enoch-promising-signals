# Evidence-ledger constraint for 124M agent tool use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-constraint-for-124m-agent-tool-use-d8529e99958d`
Run ID: `evidence-ledger-constraint-for-124m-agent-tool-use-d8529e99958d-20260604T162251125651+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/21130c243385

## What looked useful

Ledger constraints reduced unsupported accepted answers from 34.61% of accepted baseline outputs to 0% for citation_gate and ledger_copyout. Ledger_copyout improved aggregate all-task accuracy from 73.02% to 77.37%, while strict citation_gate lowered all-task accuracy to 60.72% because of abstention. The mechanism helps accepted-answer reliability but needs retry/repair for citation failures and cannot fix wrong tool observations faithfully logged in the ledger.

## Boundaries and scale limits

No 124M model was trained or evaluated; no real tool-use benchmark, natural-language parser, multi-step planning, or real API distribution was tested. The evidence is a deterministic synthetic proxy with 120000 tasks evaluated per policy across six noise conditions.

## Claim scope

Synthetic single-step tool-use traces show that append-only evidence-ledger validation can eliminate unsupported accepted answers under injected final-answer, citation, and tamper errors; a ledger-copyout policy can improve all-task accuracy when final-answer noise dominates.

## Why it stopped

Proxy-only useful signal, not direct 124M-agent validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should evaluate a 124M-class model on real or benchmarked tool-use traces with ledger validation plus retry/repair.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 124M tool-use ledger validation with retry repair
- Success threshold: Unsupported accepted answers <=1% and all-task success no worse than 5 percentage points below baseline, with accepted-answer accuracy improved by at least 10 percentage points.
- Stop condition: Stop if citation/repair failures reduce all-task success by more than 10 percentage points or unsupported accepted answers remain above 5% after ledger validation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-124m-agent-tool-use-d8529e99958d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
