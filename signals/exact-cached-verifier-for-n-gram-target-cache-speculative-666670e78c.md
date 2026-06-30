# Exact cached verifier for n-gram target-cache speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-cached-verifier-for-n-gram-target-cache-speculative-666670e78c`
Run ID: `exact-cached-verifier-for-n-gram-target-cache-speculative-666670e78c-20260523T154135129868+0000`

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

- Parent run decision: N-gram Target-Cache Speculative Decoding: enoch://control-plane/projects/n-gram-target-cache-speculative-decoding-34ab1641c85e/runs/n-gram-target-cache-speculative-decoding-34ab1641c85e-20260523T145504379504+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/954a3eae6345

## What looked useful

Suffix-only n-gram target-cache verification is unsafe under real target logits: it false-accepted 24/24 cached proposals in constructed suffix collisions. Full-prefix exact cache lookup had 0/24 false accepts and gave a median 11.1x repeated-context verifier speedup in the small benchmark.

## Boundaries and scale limits

Small single-model GPU test only; greedy next-token verifier only; no full speculative decoding serving loop, batching, stochastic acceptance, KV-cache persistence, long natural traces, or 7B-class model validation.

## Claim scope

On a controlled small direct test with distilgpt2 greedy next-token verification, an exact full-prefix cached verifier matched conventional target verification and avoided suffix-only n-gram target-cache false accepts on 24/24 suffix-collision cases.

## Why it stopped

Useful mechanism evidence was obtained, but the validation is a controlled small direct test rather than publication-grade end-to-end speculative decoding evidence.

## Recommended next action

Run a bounded deepen follow-up by integrating the exact full-prefix cache into an actual speculative decoder and replaying natural prompt traces, requiring byte-identical outputs versus conventional verification plus measured end-to-end tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end exact cached verifier in a real speculative decoder
- Success threshold: Zero output mismatches or false accepts across at least 100 natural prompts, at least 10% end-to-end tokens/s improvement over fresh target verification on traces with at least 20% exact-prefix cache hit rate, and memory overhead below 2x target KV/logit cache for the tested window.
- Stop condition: Stop if any exact-cache accepted token differs from conventional target verification, or if cache hit rate stays below 5% on natural traces after prompt selection is fixed.

## Evidence references

- Artifact root: `<local-path>/projects/exact-cached-verifier-for-n-gram-target-cache-speculative-666670e78c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
