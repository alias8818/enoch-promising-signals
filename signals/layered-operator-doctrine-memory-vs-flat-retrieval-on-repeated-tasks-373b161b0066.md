# Layered operator-doctrine memory vs flat retrieval on repeated tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-373b161b0066`
Run ID: `layered-operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-373b161b0066-20260621T053152461696+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/72aaddea9ab3

## What looked useful

Layering is a routing-quality-gated retrieval mechanism: it produced +0.185 to +0.508 mean accuracy over flat retrieval in four conditions with usable doctrine signal, but -0.443 when the doctrine signal was unreliable and flat retrieval had strong doctrine markers.

## Boundaries and scale limits

Synthetic vectors only; no LLM embeddings, no real operator traces, no learned memory writer, no multi-step agent task success. Calibrated run used 50 seeds per condition and 1200 episodes per seed.

## Claim scope

In a synthetic repeated-task retrieval benchmark, layered operator-doctrine memory improves over flat kNN when doctrine routing is reliable and flat content retrieval aliases tasks across doctrines; it fails when doctrine routing is unreliable and flat retrieval already carries doctrine signal.

## Why it stopped

No-paper closure: this is a synthetic mechanism signal, not direct validation of real operator-doctrine memory in deployed repeated tasks.

## Recommended next action

Run a bounded direct-evidence follow-up on realistic repeated agent traces with a doctrine-router confidence fallback before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine-router confidence fallback on realistic repeated agent traces
- Success threshold: Confidence-gated or blended layered retrieval beats flat retrieval by at least 5 percentage points on ambiguous repeated tasks and is no worse than 2 percentage points below flat retrieval when doctrine routing confidence is low.
- Stop condition: Stop if doctrine-router confidence is not predictive of correctness or if fallback/blending cannot prevent regressions on low-confidence doctrine cases.

## Evidence references

- Artifact root: `<local-path>/projects/layered-operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-373b161b0066`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
