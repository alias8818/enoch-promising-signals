# Hadamard-Rotated 2-bit Weights with Scalar Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hadamard-rotated-2-bit-weights-with-scalar-residual-channel-872e4cfd3a35`
Run ID: `hadamard-rotated-2-bit-weights-with-scalar-residual-channel-872e4cfd3a35-20260630T005315958339+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf6e5946a388

## What looked useful

Across three full seeds and 12 matrices per seed, Hadamard+scalar reduced mean weight MSE to 0.382x plain 2-bit and random-input output MSE to about 0.382x plain 2-bit. However, Hadamard alone was already 0.384x plain 2-bit; the scalar residual channel improved Hadamard by only about 1.0% relative on average.

## Boundaries and scale limits

No end-to-end LM perplexity, real activation calibration, downstream accuracy, packed 2-bit kernel, or comparison against modern PTQ baselines was run. The scalar residual was evaluated as an oracle rank-1 correction, not as a production deployment path.

## Claim scope

Bounded proxy benchmark on synthetic matrices and six GPT-2-small weight matrices: randomized Hadamard rotation strongly improves rowwise 2-bit reconstruction and random-input layer-output MSE versus plain rowwise 2-bit; the scalar residual channel adds a small consistent improvement over Hadamard alone.

## Why it stopped

Proxy evidence is useful but not paper-ready; the scalar residual channel's incremental effect over Hadamard alone is small and was not validated end-to-end.

## Recommended next action

Run a bounded GPT-2-small perplexity deepen test using real calibration/evaluation text activations to determine whether the small scalar residual gain changes model-level quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small perplexity test for Hadamard 2-bit scalar residual weights
- Success threshold: Hadamard 2-bit plus scalar residual improves perplexity degradation by at least 5% relative versus Hadamard-only 2-bit and beats a same-overhead control on the same evaluation subset.
- Stop condition: Stop if scalar residual improves Hadamard-only perplexity degradation by less than 2% relative or loses to a same-overhead control.

## Evidence references

- Artifact root: `<local-path>/projects/hadamard-rotated-2-bit-weights-with-scalar-residual-channel-872e4cfd3a35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
