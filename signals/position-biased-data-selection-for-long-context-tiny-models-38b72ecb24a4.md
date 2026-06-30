# Position-biased data selection for long-context tiny models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `position-biased-data-selection-for-long-context-tiny-models-38b72ecb24a4`
Run ID: `position-biased-data-selection-for-long-context-tiny-models-38b72ecb24a4-20260528T073732405549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1290e91868e3

## What looked useful

Edge-biased selection produced a compute-limited edge-bin accuracy advantage in two seeds and no advantage in one non-learning seed; at convergence all strategies reached essentially perfect accuracy, so the effect is an early-learning curriculum signal rather than a final capability gain.

## Boundaries and scale limits

No real language modeling, no decoder-only next-token LM, no contexts above 512 tokens, and only three seeds for the compute-limited checkpoint. The 600-step effect is high variance and disappears by 2000 steps.

## Claim scope

Synthetic length-512 retrieval probe with a 289,968-parameter Transformer encoder classifier; position-biased example selection was compared against uniform selection at fixed 600-step and converged 2000-step budgets.

## Why it stopped

The run produced a useful synthetic mechanism signal but not publication-grade evidence: the advantage is compute-limited, high variance at the cutoff, and absent after convergence.

## Recommended next action

Run a bounded decoder-only tiny-LM follow-up with causal next-token loss, 1k-4k contexts, real or semi-real retrieval documents, multiple seeds, and early budget-matched checkpoints; do not write a paper from this proxy result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Decoder-only validation of position-biased selection under early training budgets
- Success threshold: At an early budget-matched checkpoint, targeted position-biased selection improves its targeted bin accuracy by at least 5 percentage points over uniform in at least two of three seeds while mean accuracy is no worse than 2 percentage points below uniform.
- Stop condition: Stop if all strategies reach chance at the planned early checkpoints and a longer diagnostic shows no learning, or if convergence again removes all targeted advantages without any stable early-budget gain.

## Evidence references

- Artifact root: `<local-path>/projects/position-biased-data-selection-for-long-context-tiny-models-38b72ecb24a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
