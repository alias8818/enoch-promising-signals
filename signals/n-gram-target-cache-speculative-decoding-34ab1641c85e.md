# N-gram Target-Cache Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-target-cache-speculative-decoding-34ab1641c85e`
Run ID: `n-gram-target-cache-speculative-decoding-34ab1641c85e-20260523T145504379504+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/954a3eae6345

## What looked useful

For max_ngram=4 and max_draft=4, target_cache_last reduced target calls from 1152 greedy calls to 720 simulated verifier calls (1.60x call speedup) with 87.2% accepted/proposed tokens and 51.0% accepted/generated tokens. A shorter max_ngram=2 setting improved target_cache_last to 666 calls (1.73x) and 57.1% accepted/generated. Natural prompts showed a smaller but nonzero 1.34x call reduction; repetitive prompts reached 2.63x.

## Boundaries and scale limits

Small hand-written prompt set; trace-level verifier-call accounting only; no production cached verifier, no actual speculative tokens/sec benchmark, no public corpus-scale validation, and no comparison against neural draft models or tuned serving implementations.

## Claim scope

Trace-level GPT-2-small greedy decoding on 18 hand-written prompts x 64 generated tokens shows that an n-gram target-cache draft keyed by short suffixes can exactly match the target trace while reducing simulated verifier calls.

## Why it stopped

No-paper closure: current evidence is a useful trace-level mechanism signal, not a direct production speed or corpus-scale validation.

## Recommended next action

Run one bounded deepen follow-up: implement an exact cached/batched verifier for target-cache drafts and benchmark actual tokens/sec plus cache parity on a public GPT-2-small prompt corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact cached verifier for n-gram target-cache speculative decoding
- Success threshold: Exact output match plus at least 1.2x actual tokens/sec speedup over greedy cached GPT-2-small and at least 1.4x verifier-call reduction on at least 200 public prompts.
- Stop condition: Stop if cache/full-forward parity cannot be made exact locally, or if public-prompt verifier-call reduction falls below 1.2x before overhead accounting.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-target-cache-speculative-decoding-34ab1641c85e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
