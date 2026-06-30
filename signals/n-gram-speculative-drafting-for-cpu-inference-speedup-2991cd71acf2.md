# N-gram speculative drafting for CPU inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-drafting-for-cpu-inference-speedup-2991cd71acf2`
Run ID: `n-gram-speculative-drafting-for-cpu-inference-speedup-2991cd71acf2-20260607T112218390931+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de5906dc8f62

## What looked useful

Character-level n-gram drafting produced ideal target-pass reductions around 2.1x and modeled dense-proxy speedups up to 1.21x, but token-like word/punctuation settings were mostly below 1.0x and did not support a broad CPU inference speedup claim.

## Boundaries and scale limits

No real transformer target model, no BPE tokenizer, no KV-cache attention timing, no sampling-quality evaluation, and only up to 50k held-out replay tokens per dataset. Character-level positives should not be generalized to LLM subword decoding.

## Claim scope

Bounded local proxy: n-gram speculative drafting on held-out public text with character and word/punctuation tokenizations, using measured CPU dense-matrix batch costs as the target verification cost proxy.

## Why it stopped

Mixed proxy evidence only: useful mechanism signal on character-level replay, but insufficient and partly negative evidence for token-like CPU LLM inference.

## Recommended next action

Stop this proxy run; the next useful step is a bounded direct CPU transformer benchmark with a real tokenizer and wall-clock baseline/speculative decoding comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU transformer benchmark for n-gram speculative drafting
- Success threshold: At least 1.10x end-to-end wall-clock tokens/sec speedup over cached greedy baseline on two prompt sets, with identical greedy outputs and no single-prompt outlier carrying the aggregate.
- Stop condition: Stop if median speedup is below 1.05x on the first two prompt sets or if draft overhead exceeds 10% of total speculative runtime.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-drafting-for-cpu-inference-speedup-2991cd71acf2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
