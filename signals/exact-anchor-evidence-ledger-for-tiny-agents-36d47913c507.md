# Exact Anchor Evidence Ledger for Tiny Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507`
Run ID: `exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507-20260527T154913869242+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

With an 8-fact rolling memory, the baseline fell to 0.0 exact evidence rate after delay 8 while the exact-anchor ledger stayed at 1.0 across all delays; a 256-fact large-memory control recovered baseline performance to 1.0, isolating context eviction as the failure mode.

## Boundaries and scale limits

Tested only with synthetic single-fact questions, perfect extraction, exact entity-field keys, one CPU process, and 1000 trials per delay across delays 0-128; no real LLM extraction, natural document parsing, adversarial data, multi-hop reasoning, persistence, or production latency evaluation.

## Claim scope

In a deterministic synthetic tiny-agent stream benchmark, an exact anchor ledger preserves answer accuracy and exact evidence-citation validity after target evidence is evicted from a small rolling context.

## Why it stopped

No-paper useful signal: synthetic mechanism evidence supports the idea under context eviction, but real extraction and adversarial robustness remain untested.

## Recommended next action

Run a bounded real-LLM deepen benchmark that scores extracted exact spans, answer accuracy, and citation validity on natural-language delayed-evidence tasks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Exact Anchor Ledger Benchmark
- Success threshold: Ledger improves exact citation validity by at least 25 percentage points over no-ledger at long delays while keeping answer accuracy within 5 percentage points and adding less than 30% median latency.
- Stop condition: Stop if the ledger fails to improve exact citation validity by 10 percentage points on long-delay natural-language tasks or if extraction noise makes stored anchors invalid in more than 15% of answerable cases.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
