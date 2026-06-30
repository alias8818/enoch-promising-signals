# Dynamic Anchor Reset on Semi-Real Anchored Retrieval Text

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `dynamic-anchor-reset-on-semi-real-anchored-retrieval-text-4aa0209745`
Run ID: `dynamic-anchor-reset-on-semi-real-anchored-retrieval-text-4aa0209745-20260602T124330896338+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Learned Tiny-Model Dynamic Anchor Reset Probe: enoch://control-plane/projects/learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee/runs/learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee-20260601T014326214944+0000
- Parent run decision: Tiny Transformer Dynamic Anchor Reset Confirmation: enoch://control-plane/projects/tiny-transformer-dynamic-anchor-reset-confirmation-97b870418a/runs/tiny-transformer-dynamic-anchor-reset-confirmation-97b870418a-20260601T074843541629+0000

## What looked useful

Dynamic reset underperformed TF-IDF/fixed/periodic/oracle controls for one-term sparse queries. For two-term queries it slightly beat fixed-anchor and TF-IDF but did not beat periodic reset or oracle segment anchors, so the added reset mechanism was not justified.

## Boundaries and scale limits

Tested 8 fixed seeds, 480 real documents per seed, and 300 target queries per seed for q=1 and q=2 sparse queries. Did not test dense learned retrievers, LLM memory systems, production query logs, or larger corpora.

## Claim scope

Bounded CPU validation on semi-real 20 Newsgroups topic-drift streams with sparse TF-IDF target-document queries found no material benefit from dynamic anchor reset over simple controls.

## Why it stopped

No paper-ready effect: dynamic anchor reset failed to materially improve direct target retrieval and did not beat the simple periodic reset control.

## Recommended next action

Stop this follow-up: the bounded direct evidence is mixed/negative and the only meaningful next test would be a separate larger learned-retriever benchmark rather than another automatic depth-3 adjacent follow-up.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-anchor-reset-on-semi-real-anchored-retrieval-text-4aa0209745`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
