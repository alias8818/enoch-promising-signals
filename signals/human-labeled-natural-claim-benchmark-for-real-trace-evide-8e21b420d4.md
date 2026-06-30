# Human-labeled natural-claim benchmark for real-trace evidence-ledger gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `human-labeled-natural-claim-benchmark-for-real-trace-evide-8e21b420d4`
Run ID: `human-labeled-natural-claim-benchmark-for-real-trace-evide-8e21b420d4-20260602T135044728752+0000`

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

- Parent run decision: Evidence-ledger tool-agent hallucination reduction: enoch://control-plane/projects/evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa/runs/evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa-20260601T035540826753+0000
- Parent run decision: Real-trace evidence-ledger gating for tool-agent claims: enoch://control-plane/projects/real-trace-evidence-ledger-gating-for-tool-agent-claims-c14c28ee3d/runs/real-trace-evidence-ledger-gating-for-tool-agent-claims-c14c28ee3d-20260601T095030909877+0000

## What looked useful

Ledger gating raised selected gold-document recall from 0.4658 to 0.6195 and macro-F1 from 0.3602 to 0.3665 versus ungated top-k retrieval over five fixed seeds, while mean accuracy rose from 0.4333 to 0.4447 with uncertain bootstrap intervals.

## Boundaries and scale limits

CPU-only local benchmark; traces were constructed from SciFact cited/evidence documents, lexical retrieval candidates, and random noise rather than recorded production/tool traces; no external dataset replication or learned ledger scorer was tested.

## Claim scope

On full SciFact train/dev with constructed evidence traces, a heuristic ledger gate improved selected gold-document recall and modestly improved macro-F1 versus ungated lexical top-k retrieval, but the accuracy delta was small and bootstrap intervals crossed zero.

## Why it stopped

Tier-2 direct benchmark completed, but evidence supports only a mixed mechanism signal: evidence recall improves, downstream metric gains are small and statistically uncertain, and real-trace behavior is proxied rather than directly observed.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use non-gold constructed or recorded traces and a learned/calibrated ledger scorer with a preregistered macro-F1 threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gold-free recorded-trace ledger gate on SciFact plus a second natural-claim dataset
- Success threshold: Mean macro-F1 improves by at least 0.03 over the strongest ungated retrieval/reranking baseline and paired/bootstrap intervals exclude zero, with selected evidence recall not decreasing.
- Stop condition: Stop as negative if macro-F1 improvement is below 0.01, intervals cross zero on both datasets, or the ledger gate depends on gold labels/candidate leakage.

## Evidence references

- Artifact root: `<local-path>/projects/human-labeled-natural-claim-benchmark-for-real-trace-evide-8e21b420d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
