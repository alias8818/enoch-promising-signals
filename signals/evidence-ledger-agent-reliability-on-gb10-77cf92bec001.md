# Evidence-Ledger Agent Reliability on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-on-gb10-77cf92bec001`
Run ID: `evidence-ledger-agent-reliability-on-gb10-77cf92bec001-20260614T023551977993+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34cc0b7659b0

## What looked useful

Across 108,000,000 medium-run synthetic episodes on GB10 CUDA, the baseline unsupported published claim rate averaged 0.363064 while the ledger unconditional unsupported rate averaged 0.004009, a mean 98.93% reduction; the worst medium cell still reduced unsupported claims by 96.34%. A high false-accept verifier stress run showed the failure boundary: at 10% verifier false accepts, worst-cell ledger unsupported publications rose to 9.80% unconditional but still reduced unsupported claims by 82.52% versus baseline.

## Boundaries and scale limits

Synthetic proxy only: no real LLM tool use, no real document retrieval, no natural-language entailment audit, no multi-step planning, and no production persistence. The result should not be generalized to real agent reliability without trace-based validation.

## Claim scope

In a synthetic one-claim publication model with explicit retrieval quality, citation drift, verifier false-accept, verifier false-reject, and retry-budget parameters, a pre-publication evidence ledger reduced unsupported published claims versus a mutable-scratchpad baseline across all tested grid cells.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, not a direct validation of real agent reliability.

## Recommended next action

Run a bounded real-trace follow-up: implement the same ledger and no-ledger baseline around a small local LLM/retrieval task set, then audit unsupported natural-language claims with an independent entailment checker or human labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence-ledger validation on small local agent tasks
- Success threshold: At least 50% relative reduction in audited unsupported published claims with ledger coverage >= 70% and no more than 10 percentage points absolute accuracy loss versus baseline.
- Stop condition: Stop if the ledger fails to reduce audited unsupported claims by 25% in a 100-task pilot or if verifier false accepts exceed 10% on audited ledger publications.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-gb10-77cf92bec001`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
