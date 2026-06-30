# Merkle-Commitment Spot-Check Gradient Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-commitment-spot-check-gradient-verification-03b9cecb138b`
Run ID: `merkle-commitment-spot-check-gradient-verification-03b9cecb138b-20260629T120555379729+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4aed25db8fa9

## What looked useful

Across 24 medium scenarios, empirical detection was close to 1 - (1 - tamper_fraction)^spot_checks with mean absolute error 0.0110 and max error 0.0468; clean false rejects and Merkle proof failures were zero; mean proof verification was 4.84 us/check and commitment was 1.07 ms for 1024 x 129 and 7.39 ms for 4096 x 513 gradients.

## Boundaries and scale limits

Not tested on deep networks, transformer-scale training, optimizer-state commitments, adaptive adversaries, distributed transcripts, production per-example-gradient extraction, or cryptographic proof-system integration. Largest committed gradient matrix was about 8.0 MiB.

## Claim scope

On CUDA-generated toy/medium logistic-regression per-sample gradients up to 4096 x 513 float32 values, a SHA-256 Merkle commitment plus random verifier recomputation detects committed gradient-row corruptions at the expected independent spot-check sampling rate, with zero clean false rejects in this run.

## Why it stopped

No-paper useful signal: the local proxy supports the mechanism, but it is not direct or broad enough for a publication-grade claim about full-scale gradient verification.

## Recommended next action

Run a bounded direct-evidence follow-up on a small CNN or transformer block with per-example or verifiable microbatch gradients, measuring verifier overhead as a fraction of real training-step time and including structured/adaptive corruption controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deep-model Merkle spot-check gradient verification overhead
- Success threshold: Detection error within 5 percentage points of the sampling-law expectation, zero clean false rejects, and verifier overhead under 10% of baseline training-step time for the 95%-at-5%-tamper spot-check setting.
- Stop condition: Stop as negative if per-example or microbatch gradient extraction plus verifier recomputation exceeds 25% overhead on the small model or if clean false rejects/proof failures occur without an implementation bug fix.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-commitment-spot-check-gradient-verification-03b9cecb138b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
