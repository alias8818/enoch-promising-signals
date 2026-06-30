# Adafactor vs blockwise 8-bit Adam: CPU-only head-to-head on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adafactor-vs-blockwise-8-bit-adam-cpu-only-head-to-head-on-gpt-2-small-7145c87219c2`
Run ID: `adafactor-vs-blockwise-8-bit-adam-cpu-only-head-to-head-on-gpt-2-small-7145c87219c2-20260628T122341365125+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3118b0c19190

## What looked useful

Adafactor used 1,286,468 optimizer-state bytes and averaged 4.681 s/step; blockwise 8-bit Adam used 249,123,216 optimizer-state bytes and averaged 8.538 s/step. For CPU optimizer overhead on GPT-2-small shapes, Adafactor was 193.65x smaller in optimizer state and 1.82x faster in this NumPy benchmark.

## Boundaries and scale limits

No real GPT-2-small training, dataset, forward/backward pass, perplexity, or production optimizer package benchmark was run. Evidence is limited to three full-shape synthetic-gradient optimizer steps per optimizer.

## Claim scope

CPU-only optimizer-state memory and synthetic-gradient update overhead for Adafactor versus blockwise 8-bit Adam on exact GPT-2-small parameter shapes.

## Why it stopped

Bounded CPU-only optimizer-overhead benchmark completed; result is useful but not publication-grade because it is synthetic-gradient evidence rather than direct training-quality evidence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded action is a real PyTorch GPT-2-small-class training comparison with equal tokens and measured loss/perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPT-2-small-class CPU training comparison for Adafactor versus blockwise 8-bit Adam
- Success threshold: Adafactor keeps at least a 50x optimizer-state memory advantage and reaches within 5% of blockwise 8-bit Adam's final validation loss in the bounded equal-token run.
- Stop condition: Stop if dependency installation or projected CPU runtime exceeds the deployment budget, or if an initial 100-step pilot shows either optimizer is unstable or more than 20% worse in validation loss under matched settings.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-vs-blockwise-8-bit-adam-cpu-only-head-to-head-on-gpt-2-small-7145c87219c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
