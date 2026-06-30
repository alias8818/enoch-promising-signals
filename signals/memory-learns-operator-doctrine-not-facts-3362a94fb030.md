# Memory learns operator doctrine not facts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-learns-operator-doctrine-not-facts-3362a94fb030`
Run ID: `memory-learns-operator-doctrine-not-facts-3362a94fb030-20260611T090728978523+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/79b0409ff79c

## What looked useful

Doctrine-style memory generalized better than episodic fact memory in clean-label regimes once training coverage reached 40+ cases, reaching 0.959 OOD accuracy at 160 cases with about 8% as many memory entries. The advantage disappeared or reversed under 5-15% noisy operator labels.

## Boundaries and scale limits

No real LLM memory system, natural-language operator traces, production doctrine drift, or large-scale training was tested; the doctrine learner is a simple greedy rule inducer.

## Claim scope

Synthetic categorical operator-policy benchmark comparing episodic case memory with induced compact doctrine rules on held-out feature combinations.

## Why it stopped

Proxy evidence is mixed: it supports doctrine abstraction under clean synthetic labels but early-falsifies the broad claim that doctrine memory reliably beats fact memory under noisy operator feedback.

## Recommended next action

Run a bounded deepen test with noise-aware doctrine extraction and realistic natural-language operator corrections before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noise-aware operator doctrine extraction from natural-language corrections
- Success threshold: At 5% and 15% noisy corrections, confidence-scored doctrine memory improves held-out accuracy by at least 5 percentage points over episodic memory while using no more than 25% of its memory entries.
- Stop condition: Stop if doctrine memory fails to match episodic held-out accuracy at 5% noise in two independent 30-seed sweeps or requires more memory entries than episodic storage.

## Evidence references

- Artifact root: `<local-path>/projects/memory-learns-operator-doctrine-not-facts-3362a94fb030`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
