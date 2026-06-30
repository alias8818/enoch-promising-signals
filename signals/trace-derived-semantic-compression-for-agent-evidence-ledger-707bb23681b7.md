# Trace-Derived Semantic Compression for Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-for-agent-evidence-ledger-707bb23681b7`
Run ID: `trace-derived-semantic-compression-for-agent-evidence-ledger-707bb23681b7-20260621T001802807473+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Across five seeds, trace_semantic was best at every tested budget. At budget 6, it reached 0.999 mean accuracy and 0.735 evidence retention versus 0.149 accuracy for the best naive baseline. At budget 4, it reached 0.799 accuracy versus 0.099 for the best naive baseline.

## Boundaries and scale limits

Synthetic-only; 5 seeds; 240 traces per seed; 1,200 claims per seed/policy/budget; no real LLM/tool traces; no natural-language summarizer; no adversarial/noisy/redacted evidence-marker setting; CPU-only local run.

## Claim scope

On deterministic synthetic agent traces with explicit structured claim/evidence markers, trace-derived semantic event selection preserves evidence-ledger claim verification accuracy substantially better than budget-matched head, tail, and random compression at 4-12 retained events out of 80.

## Why it stopped

No-paper closure: this is useful synthetic mechanism evidence, but not publication-grade validation on real or robust traces.

## Recommended next action

Run a bounded follow-up on noisy/redacted synthetic traces and a small real agent trace corpus, comparing trace-derived selection against embedding or LLM summarization at equal token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy and Real Trace Evidence-Ledger Compression Check
- Success threshold: At matched token/event budgets, trace-derived compression improves claim-verification accuracy by at least 20 percentage points over the best non-oracle baseline while keeping false-supported unsupported claims below 5%.
- Stop condition: Stop if noisy/redacted or real-trace accuracy is within 5 percentage points of naive/random baselines, or if false-supported unsupported claims exceed 10% at useful compression ratios.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-for-agent-evidence-ledger-707bb23681b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
