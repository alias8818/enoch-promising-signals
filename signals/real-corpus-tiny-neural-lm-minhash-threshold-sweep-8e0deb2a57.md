# Real-corpus tiny neural LM MinHash threshold sweep

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-neural-lm-minhash-threshold-sweep-8e0deb2a57`
Run ID: `real-corpus-tiny-neural-lm-minhash-threshold-sweep-8e0deb2a57-20260610T051409098775+0000`

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

- Parent run decision: MinHash Dedup Threshold Has a Non-Trivial Optimum for Tiny LMs: enoch://control-plane/projects/minhash-dedup-threshold-has-a-non-trivial-optimum-for-tiny-lms-010467313810/runs/minhash-dedup-threshold-has-a-non-trivial-optimum-for-tiny-lms-010467313810-20260609T143413924106+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e1da85b33ea

## What looked useful

Real-corpus near-duplicate density in this WikiText-2 setting is too low for MinHash threshold tuning to materially affect tiny-LM validation loss: threshold 0.20 removed about 1.7% of documents and 0.63% of tokens, while mean validation loss was +0.0058 nats worse than unfiltered control.

## Boundaries and scale limits

Not a transformer-scale or web-scale result; only WikiText-2 line documents, 675k training tokens before filtering, 900 SGD steps per condition, and stochastic validation batches were tested.

## Claim scope

On a 5,000-document WikiText-2 raw line-level subset with a tiny NumPy neural next-token LM, MinHash threshold lowering increases real near-duplicate removals but does not improve validation loss relative to an unfiltered control across three seeds.

## Why it stopped

Controlled small direct real-corpus test found mechanism support but no measurable validation-loss improvement; evidence is useful but not paper-positive.

## Recommended next action

Stop this run as no-paper evidence; the bounded next useful test is a real high-duplication corpus slice where MinHash filtering removes at least 5% of tokens before LM training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: High-duplication real-corpus MinHash threshold sweep for tiny neural LMs
- Success threshold: An intermediate threshold removes at least 5% of training tokens and improves mean validation loss by at least 0.03 nats versus unfiltered control without overlapping the direction of seed noise.
- Stop condition: Stop if no threshold removes at least 5% of tokens on the selected real corpus or if all thresholds are within +/-0.02 nats of the unfiltered validation loss across three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-neural-lm-minhash-threshold-sweep-8e0deb2a57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
