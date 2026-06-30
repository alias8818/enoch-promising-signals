# Agent Reliability with Quantized Residual Memory Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-with-quantized-residual-memory-channels-3fa7f580ca2c`
Run ID: `agent-reliability-with-quantized-residual-memory-channels-3fa7f580ca2c-20260608T210801271353+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

Residual quantization was strongly beneficial only when the predictable prototype explained most target energy. At 3 bits in structured_low_residual it improved reconstruction success by 0.996 and reduced normalized MSE to 4.9% of full quantization. At 4 bits in structured_medium_residual it improved success by 0.966 and reduced normalized MSE to 27.1% of full quantization. In weak_structure the advantage disappeared, and in noisy_predictor the residual channel failed because prototype error dominated.

## Boundaries and scale limits

CPU-only synthetic benchmark; no learned agent, no LLM, no real tool-use traces, no long-horizon memory accumulation, no hardware-aware quantization, and no parameter-matched neural baseline.

## Claim scope

Synthetic vector-memory probe: under accurate cue-conditioned prototypes and small-to-medium residuals, equal-bit residual quantization substantially improves normalized reconstruction error and thresholded reconstruction success versus full-vector quantization.

## Why it stopped

Synthetic proxy supports a narrow mechanism but does not directly validate agent reliability or a learned architecture.

## Recommended next action

Stop as no-paper useful signal; the next bounded test should train a small recurrent or transformer memory model with learned residual channels on delayed-recall tasks and compare against parameter-matched full-memory quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Residual Memory Channels on Delayed-Recall Tasks
- Success threshold: Residual-channel model improves delayed-recall task success by at least 10 percentage points over full-memory quantization in structured conditions, with no comparable advantage in weak-structure controls, across at least three seeds.
- Stop condition: Stop if residual channels fail to beat full-memory quantization by 5 percentage points in structured conditions or if the effect also appears equally in weak-structure controls.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-with-quantized-residual-memory-channels-3fa7f580ca2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
