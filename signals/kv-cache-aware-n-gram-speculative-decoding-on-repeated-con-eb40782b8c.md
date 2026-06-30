# KV-cache-aware n-gram speculative decoding on repeated-context workloads

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-aware-n-gram-speculative-decoding-on-repeated-con-eb40782b8c`
Run ID: `kv-cache-aware-n-gram-speculative-decoding-on-repeated-con-eb40782b8c-20260609T220029165769+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram Cache Speculative Decoding on GB10: enoch://control-plane/projects/n-gram-cache-speculative-decoding-on-gb10-bed808c00b5d/runs/n-gram-cache-speculative-decoding-on-gb10-bed808c00b5d-20260609T170611151508+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef764dcfdc55

## What looked useful

Repeated token n-grams did not imply reusable KV state. In distilgpt2, replacing later repeated-span KV with earlier-span KV produced mean logit_linf 9.55, mean KL 0.231 nats, and a 12.5% greedy top-1 mismatch rate.

## Boundaries and scale limits

Tier 1 small direct test only: 512 randomized tiny-transformer cases, 64 sshleifer/tiny-gpt2 cases, and 24 distilgpt2 cases. No production serving benchmark, no long-context corpus, and no 7B+ model validation.

## Claim scope

Exact copying/reuse of earlier per-layer KV cache entries for a later matching token n-gram is not a safe exact shortcut in causal transformer decoding. This was tested on a controlled tiny transformer and on repeated-span prompts with distilgpt2.

## Why it stopped

Tier 1 direct mechanism test found that exact KV copying from repeated n-grams changes the next-token distribution; this is a useful no-paper negative result rather than full production validation.

## Recommended next action

Stop pursuing naive raw KV-copy reuse; if this line continues, run a bounded deepen test of a guarded KV-aware n-gram speculative decoder with exact target verification against a standard prompt-lookup baseline on GPT-2-small-class models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded KV-aware n-gram speculation with exact verification
- Success threshold: On at least 100 repeated-context prompts, the guarded variant must preserve target outputs exactly or within deterministic tie tolerance, reduce wall-clock decode latency by at least 10% versus standard prompt-lookup speculation, and show no increase in rejected-token target work.
- Stop condition: Stop if output equivalence fails on any non-tie case, if latency improvement is under 5%, or if implementation requires model-specific state transforms that are not portable across GPT-2-style positional settings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-n-gram-speculative-decoding-on-repeated-con-eb40782b8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
