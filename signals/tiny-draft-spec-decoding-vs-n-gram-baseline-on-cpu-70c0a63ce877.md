# Tiny Draft Spec-Decoding vs N-gram Baseline on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-draft-spec-decoding-vs-n-gram-baseline-on-cpu-70c0a63ce877`
Run ID: `tiny-draft-spec-decoding-vs-n-gram-baseline-on-cpu-70c0a63ce877-20260620T101402013331+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a0ad0c6bd9

## What looked useful

Tiny draft won all 6 paired conditions. Accepted tokens per verifier call were 1.951/3.727/5.734 vs 0.112/0.119/0.119 on license text and 1.802/3.165/4.518 vs 0.227/0.258/0.278 on Python stdlib for draft lengths 2/4/8.

## Boundaries and scale limits

Proxy only: no neural transformer target, no real tiny neural draft model, no tokenizer/KV-cache/llama.cpp integration, no end-to-end wall-clock decoding speedup measurement, and only two local text corpora.

## Claim scope

In a bounded CPU proxy with an order-5 count-LM target verifier, an order-3 tiny count-LM draft proposer produced more accepted speculative tokens per verifier call than a prompt-copy n-gram baseline on local license and Python-stdlib corpora.

## Why it stopped

Proxy-only evidence supports the mechanism but does not directly validate neural CPU speculative decoding or wall-clock speedup.

## Recommended next action

Stop this run as proxy-only useful signal; next run should repeat the comparison with a real CPU transformer target, a real tiny draft model, and the same n-gram baseline before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU transformer tiny-draft speculative decoding vs prompt n-gram baseline
- Success threshold: Tiny neural draft improves accepted tokens per verifier call by at least 1.5x and end-to-end tokens/s by at least 1.1x over prompt n-gram on both prompt sets within a bounded CPU run.
- Stop condition: Stop if tiny draft accepted tokens per verifier call is below prompt n-gram on either prompt set or if draft overhead eliminates throughput gains.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-spec-decoding-vs-n-gram-baseline-on-cpu-70c0a63ce877`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
