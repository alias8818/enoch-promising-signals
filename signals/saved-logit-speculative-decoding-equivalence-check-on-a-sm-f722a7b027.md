# Saved-logit speculative decoding equivalence check on a small transformer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027`
Run ID: `saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027-20260614T115450339452+0000`

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

- Parent run decision: CPU Speculative Decoding Equivalence Probe: enoch://control-plane/projects/cpu-speculative-decoding-equivalence-probe-d816bc58b4c4/runs/cpu-speculative-decoding-equivalence-probe-d816bc58b4c4-20260614T040712060973+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

All 1728 causal cases matched baseline greedy decoding exactly, with zero causal failures. A leaky-attention control diverged in 1227 of 1296 non-oracle cases, supporting that causal masking is the mechanism behind equivalence. Mean forward-call speedup proxy was 3.086x, max 8.0x.

## Boundaries and scale limits

Tested only random-weight small Transformer models with vocab size 97, width 48, 2 layers, 4 heads, prompt lengths 3/7/13, generation lengths 24/40, block sizes 2/4/8, and 24 seeds. It does not cover trained pretrained models, sampling, GPU kernels, KV-cache serving implementations, batching, large models, or wall-clock throughput.

## Claim scope

In a deterministic NumPy small causal Transformer using greedy decoding, saved target logits from a single forward pass over prefix plus draft exactly reproduce standard greedy decoding when draft tokens are accepted only if they match the saved target argmax and the first mismatch is replaced by the saved target argmax.

## Why it stopped

Tier 1 controlled small direct test completed and supports the scoped mechanism, but evidence is not paper-positive because it uses a NumPy random-weight small model and forward-call proxies rather than trained-model serving measurements.

## Recommended next action

Run a bounded pretrained GPT-2-small-class follow-up with a real draft model, KV-cache-aware implementation, exact-token equivalence checks, and wall-clock/token-throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small saved-logit speculative decoding equivalence and throughput check
- Success threshold: At least 100 diverse prompts with zero token mismatches under deterministic greedy decoding, plus a statistically clear throughput improvement over greedy target decoding when draft acceptance rate is above 0.5.
- Stop condition: Stop if any reproducible deterministic greedy token mismatch appears in a correctly implemented causal target path, or if acceptance/throughput evidence shows no practical benefit despite preserved equivalence.

## Evidence references

- Artifact root: `<local-path>/projects/saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
