# Predictive Operator-Model Memory: Do Memory Stores Learn Reusable Doctrine on Repeated Tasks?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-operator-model-memory-do-memory-stores-learn-reusable-doctrine-on-repeated-tasks-041bf7fe32e2`
Run ID: `predictive-operator-model-memory-do-memory-stores-learn-reusable-doctrine-on-repeated-tasks-041bf7fe32e2-20260619T185602888445+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b52d97c3c692

## What looked useful

Memory stores do not automatically learn reusable doctrine: naive high-confidence rule storage overfits repeated specifics, while compressed rule memory recovers some reusable doctrine and improves accuracy over controls. Episodic retrieval remains a strong baseline and beats compressed doctrine at the largest train size.

## Boundaries and scale limits

20 random seeds, 1200 held-out synthetic tasks per seed, train sizes 24-384; no real operator traces, no external model memory API, no long-horizon persistence, no natural-language-only retrieval, no production drift.

## Claim scope

In a synthetic, feature-structured operator triage proxy, compressed doctrine-style memory can extract reusable rules from repeated solved tasks and beat no-memory plus shuffled-label controls, but it does not consistently beat raw episodic retrieval and has weaker macro-F1.

## Why it stopped

No-paper closure: this is a synthetic proxy with mixed results, not full validation of real operator-model memory stores.

## Recommended next action

Run a bounded direct follow-up on LLM-generated or real repeated operator traces with blinded held-out tasks, episodic retrieval baseline, shuffled-memory control, persistence checks, and macro-F1 success thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine memory on repeated natural-language operator traces
- Success threshold: Compressed doctrine memory improves held-out accuracy by at least 5 percentage points over episodic retrieval and improves or matches macro-F1 within 2 points across at least 5 independent task families.
- Stop condition: Stop as negative if compressed doctrine fails to beat episodic retrieval on accuracy or loses more than 5 macro-F1 points on two consecutive task families.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-memory-do-memory-stores-learn-reusable-doctrine-on-repeated-tasks-041b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
