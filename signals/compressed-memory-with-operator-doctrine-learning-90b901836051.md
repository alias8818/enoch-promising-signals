# Compressed Memory with Operator Doctrine Learning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-memory-with-operator-doctrine-learning-90b901836051`
Run ID: `compressed-memory-with-operator-doctrine-learning-90b901836051-20260611T213921807663+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2dbc57aa11d0

## What looked useful

A compact learned doctrine model achieved 0.932 mean accuracy at 4096 training examples on rule-structured policies versus 0.580 for raw episodic kNN while using about 859x fewer bytes; on lookup-style exceptions it fell to 0.333 versus 0.984 for kNN despite about 1065x compression.

## Boundaries and scale limits

No real operator data, no natural-language memory compression, no long-horizon agent deployment, no GPT-2-small-class model training, and no robustness beyond 8 seeds over two synthetic regimes.

## Claim scope

Synthetic operator-correction benchmark only: compressed doctrine memory improves prediction per byte on stable rule-structured operator policies and fails on random local lookup exceptions.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and mechanism-scoped, not direct validation of real operator doctrine learning.

## Recommended next action

Run a bounded deepen follow-up on language-action operator correction traces comparing episodic RAG, compressed doctrine, and doctrine-plus-exception hybrid memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Doctrine and Exception Memory on Language-Action Operator Corrections
- Success threshold: Hybrid memory is within 3 percentage points of episodic retrieval on exception-heavy traces, beats doctrine-only by at least 10 points there, and retains at least 10x memory compression on rule-like traces.
- Stop condition: Stop if hybrid gating cannot beat doctrine-only by 5 accuracy points on exception-heavy traces or if compression falls below 3x versus episodic retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-memory-with-operator-doctrine-learning-90b901836051`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
