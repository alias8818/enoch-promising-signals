# GaLore vs AdamW Memory-Convergence Pareto on GPT-2-small-class

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-vs-adamw-memory-convergence-pareto-on-gpt-2-small-class-ee5517aac3ce`
Run ID: `galore-vs-adamw-memory-convergence-pareto-on-gpt-2-small-class-ee5517aac3ce-20260620T125216921280+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8623ab8e2ca7

## What looked useful

GaLore-style optimizer state was 0.151x to 0.580x AdamW in the proxy sweep. Best tuned GaLore finished at loss 16.2762 with 0.580x AdamW state, while best tuned AdamW reached 12.3543; a 0.151x-state GaLore point reached 19.6317. This indicates a real memory-saving tradeoff, not paper-ready Pareto dominance.

## Boundaries and scale limits

No GPU was available; no full GPT-2-small training, real corpus, validation set, mixed precision, activation memory telemetry, production GaLore package, or seed repeats were run. GPT-2-small memory numbers are shape estimates only.

## Claim scope

Bounded CPU proxy: a 2-layer, 128-wide GPT-style causal LM on synthetic next-token data for 40 steps, plus analytical optimizer-state accounting for GPT-2-small shapes. Evidence supports memory reduction but not tuned convergence Pareto dominance.

## Why it stopped

Bounded proxy and analytical memory accounting are insufficient for a paper-positive GPT-2-small claim, and tuned AdamW retained better convergence in the local sweep.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should use a production GaLore optimizer on a GPU-enabled GPT-2-small-class real-corpus run with validation loss and peak-memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production GaLore vs tuned AdamW on real GPT-2-small-class data
- Success threshold: At least one GaLore configuration uses <=0.60x AdamW optimizer/peak training memory and finishes within 10% relative validation-loss gap of the best tuned AdamW at equal tokens.
- Stop condition: Stop if no GaLore configuration with <=0.60x memory reaches within 20% relative validation-loss gap by the planned token budget, or if production optimizer behavior cannot be reproduced.

## Evidence references

- Artifact root: `<local-path>/projects/galore-vs-adamw-memory-convergence-pareto-on-gpt-2-small-class-ee5517aac3ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
