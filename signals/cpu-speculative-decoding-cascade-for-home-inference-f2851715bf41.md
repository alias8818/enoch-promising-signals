# CPU Speculative Decoding Cascade for Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-cascade-for-home-inference-f2851715bf41`
Run ID: `cpu-speculative-decoding-cascade-for-home-inference-f2851715bf41-20260628T211442010605+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2731a9e81bfb

## What looked useful

Cascades beat baseline target decoding in 60.38% of simulated cases, but only 0.43% both reached at least 1.20x baseline speedup and beat the best single-draft alternative by at least 5%. Median cascade gain versus best single draft was 0.773x.

## Boundaries and scale limits

No real LLM weights, llama.cpp integration, hardware counter profiling, or wall-clock tokens/sec serving measurement; acceptance probabilities and draft/verifier costs were parameterized.

## Claim scope

Deterministic normalized CPU-cost simulator over 9,450 cascade configurations shows two-stage speculative decoding cascades have a narrow useful region and usually underperform the best single-draft speculative alternative.

## Why it stopped

Proxy/mechanism evidence is mixed and not paper-ready: the cascade has a narrow favorable region, but typical cases lose to the simpler single-draft control.

## Recommended next action

Stop this run as a proxy useful-signal result; if continued, run a bounded llama.cpp CPU follow-up with real quantized small/medium/target model pairs and compare against a tuned single-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU llama.cpp acceptance and tokens/sec test for speculative cascade versus single draft
- Success threshold: Cascade achieves at least 1.20x baseline target tokens/sec and at least 1.05x tokens/sec over the best tuned single-draft speculative baseline on a fixed local prompt suite.
- Stop condition: Stop if measured cascade tokens/sec is below the best single-draft baseline by more than 5% after tuning block sizes 2, 4, and 8, or if model download/runtime exceeds the local CPU-only budget.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-cascade-for-home-inference-f2851715bf41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
