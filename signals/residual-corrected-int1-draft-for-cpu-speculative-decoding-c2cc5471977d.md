# Residual-corrected int1 draft for CPU speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-corrected-int1-draft-for-cpu-speculative-decoding-c2cc5471977d`
Run ID: `residual-corrected-int1-draft-for-cpu-speculative-decoding-c2cc5471977d-20260525T065110975648+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/278e45695bb5

## What looked useful

Bitpacked int1 delivered 4.8x-58.1x speedup over naive FP32, but top-1 agreement stayed between 8.6% and 24.2% and softmax overlap between 0.701 and 0.788. Preserving FP32 activations raised overlap to 0.869 at k=256 but ran slower than FP32 for residual-corrected settings.

## Boundaries and scale limits

No real LM, tokenizer, natural prompts, target verification loop, or end-to-end accepted tokens/sec measurement was run. The benchmark uses synthetic Gaussian activations and weights and naive FP32/reference kernels, so it is a mechanism proxy rather than a full speculative-decoding validation.

## Claim scope

On a bounded CPU synthetic logit-projection proxy with batch=128, hidden=1024, outputs=4096, bitpacked sign-activation/sign-weight int1 draft compute is much faster than naive FP32 but residual correction up to k=256 per output column does not recover strong top-1 or distribution agreement; weight-only int1 with FP32 activations improves agreement but loses speed once residual correction is added.

## Why it stopped

Proxy evidence is mixed/negative for the practical claim: the fast fully bitpacked path has weak agreement, while the more accurate FP32-activation residual path loses the CPU speed advantage.

## Recommended next action

Stop this run as no-paper useful signal; the only worthwhile next bounded test is a real tiny-LM accepted-tokens/sec benchmark with learned low-density residual correction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-LM accepted-token benchmark for learned low-density int1 residual drafts
- Success threshold: At k<=64 or comparable low correction cost, achieve at least 2x accepted tokens/sec over the FP32 draft/control while keeping acceptance rate within 80% of the control on the same prompts.
- Stop condition: Stop if a smoke run shows top-1 agreement below 40%, accepted-token throughput below 1.2x control, or residual correction cost exceeding the target verification savings.

## Evidence references

- Artifact root: `<local-path>/projects/residual-corrected-int1-draft-for-cpu-speculative-decoding-c2cc5471977d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
