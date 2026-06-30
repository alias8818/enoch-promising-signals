# CPU N-gram Draft Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-speculation-d9a08e5784e0`
Run ID: `cpu-n-gram-draft-speculation-d9a08e5784e0-20260608T164243405023+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e6366c2e2979

## What looked useful

The mechanism is computationally cheap and produces some accepted tokens, but held-out acceptance is too weak for a broad CPU n-gram speculative decoding claim without a more repetitive domain or real-model evidence.

## Boundaries and scale limits

This run did not attach the drafter to a real LLM target, did not use production BPE tokenization, did not measure GPU verification latency or KV-cache effects, and evaluated only 500k train tokens and 50k held-out positions.

## Claim scope

On a bounded WikiText-2 raw proxy with regex tokenization, a CPU most-frequent n-gram drafter is fast but has sparse exact-match acceptance: best order-6 K=8 emitted 1.246 idealized tokens per target verification call with median accepted tokens 0.

## Why it stopped

Proxy evidence is useful but not paper-ready: the best idealized speedup was only 1.246x before real serving overhead, with median accepted tokens 0 and 0.026% full 8-token draft acceptance.

## Recommended next action

Run a bounded real-model deepen test with the same drafter attached to a small local GPT-2-class target and stop unless measured wall-clock decode latency improves by at least 10% without output-quality drift.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU n-gram speculative decoding latency test
- Success threshold: At least 10% wall-clock tokens/s improvement over no-drafter baseline on a fixed prompt suite, with no measurable output-quality regression and acceptance distribution stable across prompt categories.
- Stop condition: Stop if median accepted draft tokens remains 0 and wall-clock tokens/s improves by less than 5%, or if integration overhead erases the idealized target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-speculation-d9a08e5784e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
