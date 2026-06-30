# Held-out operator-doctrine replay benchmark with real embedding baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-operator-doctrine-replay-benchmark-with-real-embe-40a8da2c48`
Run ID: `held-out-operator-doctrine-replay-benchmark-with-real-embe-40a8da2c48-20260620T172022385661+0000`

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

- Parent run decision: Human-authored operator-doctrine replay benchmark with embedding flat baselines: enoch://control-plane/projects/human-authored-operator-doctrine-replay-benchmark-with-emb-4b8f546702/runs/human-authored-operator-doctrine-replay-benchmark-with-emb-4b8f546702-20260620T165000404750+0000
- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on CPU: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76/runs/operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76-20260620T163942579555+0000

## What looked useful

Operator-specific doctrine contributed signal versus shuffled doctrine (+0.225 to +0.246 paired accuracy delta), but the deployable layered strategy tied flat embedding retrieval at 0.410 mean accuracy and trailed transcript_search at 0.533 mean accuracy.

## Boundaries and scale limits

Synthetic generated replay tasks only; no private production operator traces or external corpus; CPU-only short run; sentence-transformer MiniLM baseline only; not publication-grade validation.

## Claim scope

On a deterministic medium held-out operator-doctrine replay benchmark with 24 synthetic operators and fixed seeds 11,23,37, layered doctrine memory uses operator-specific doctrine better than a shuffled-doctrine control but does not improve over flat MiniLM embedding retrieval and underperforms lexical transcript search.

## Why it stopped

Tier-2 fixed-seed benchmark produced useful but non-paper-positive evidence: layered doctrine beat the shuffled control but failed to beat the real embedding baseline or the stronger lexical baseline.

## Recommended next action

Run one bounded deepen test that separates scenario normalization from doctrine aggregation, comparing hybrid lexical+embedding scenario retrieval plus layered doctrine against transcript_search and MiniLM flat retrieval on sanitized real replay traces or a harder no-leak synthetic fixture.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Scenario-normalized doctrine memory versus lexical and MiniLM retrieval
- Success threshold: Layered doctrine memory improves mean held-out accuracy by at least 0.08 over both flat embedding and transcript_search, with 95% paired bootstrap CI low greater than 0 on all fixed seeds.
- Stop condition: Stop if layered doctrine is tied with or worse than either real embedding or lexical baseline, or if gains only appear with oracle scenario labels or leaked doctrine fields.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-operator-doctrine-replay-benchmark-with-real-embe-40a8da2c48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
