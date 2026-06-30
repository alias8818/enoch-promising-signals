# Small-transformer lookahead-Jacobi n-gram pool validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-lookahead-jacobi-n-gram-pool-validation-5b099719c5`
Run ID: `small-transformer-lookahead-jacobi-n-gram-pool-validation-5b099719c5-20260630T071408208853+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Lookahead-Jacobi Decoding with N-Gram Pool (CPU): enoch://control-plane/projects/lookahead-jacobi-decoding-with-n-gram-pool-cpu-462c0aab1d50/runs/lookahead-jacobi-decoding-with-n-gram-pool-cpu-462c0aab1d50-20260629T132712831482+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3f67e44b264

## What looked useful

The mechanism is viable in a controlled setting: Jacobi n-gram acceptance increased with iteration depth (about 1, 2, 3, 4 tokens for k=1..4) while prompt and random controls stayed near one token, and verification preserved exact greedy output.

## Boundaries and scale limits

CPU-only proxy; no trained small Transformer weights, no natural-language corpus, no GPU serving kernel, and no wall-clock speedup claim. Serial model-pass count was higher for Jacobi than autoregressive decoding.

## Claim scope

On a deterministic tiny fixed-weight causal decoder proxy with synthetic phrase cycles, Jacobi trajectory n-gram pools can provide exact verifiable multi-token greedy advances; 64 prompts x 32 tokens, window=4, k=4 accepted 4 tokens per outer step with 100% exact-match output.

## Why it stopped

Closed as no-paper useful signal because evidence is proxy-only and does not validate trained-model or serving-speed claims.

## Recommended next action

Run a bounded direct follow-up on an actual pretrained small Transformer such as GPT-2-small or TinyLlama with GPU/vectorized verification, measuring exact-match acceptance, wall-clock latency, and serial/pass-count overhead against greedy and speculative-decoding controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-Transformer lookahead-Jacobi n-gram acceptance and latency check
- Success threshold: At least 99.9% exact greedy equivalence, mean accepted tokens >=1.5, and measured wall-clock speedup or neutral latency versus greedy on a pretrained small Transformer workload.
- Stop condition: Stop if exact-match verification fails, acceptance remains <=1.1 tokens, or serial/batched overhead makes latency worse than greedy by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-lookahead-jacobi-n-gram-pool-validation-5b099719c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
