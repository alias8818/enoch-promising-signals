# Local N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-n-gram-speculative-decoding-dbbd44c98f71`
Run ID: `local-n-gram-speculative-decoding-dbbd44c98f71-20260527T182513703598+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b7ed12583e47

## What looked useful

Primary run produced 18/18 exact greedy matches, 0.632 mean draft-token acceptance, 0.655 mean target-forward reduction, and 2.88x mean local speedup; a smaller n=2/draft=4 ablation produced 12/12 exact matches, 0.590 mean target-forward reduction, and 2.18x speedup.

## Boundaries and scale limits

Small model, small hand-built prompt set, greedy decoding only, single-process local Python implementation, no production serving engine, no real traffic traces, no 7B+ model, no batching or paged KV-cache evaluation.

## Claim scope

On a local distilgpt2/Hugging Face prototype with six short prompts, local n-gram speculative drafts preserved exact greedy outputs and reduced target-model forward passes versus cached greedy decoding.

## Why it stopped

This run produced a useful bounded mechanism signal but remains too small and prototype-local for a paper claim.

## Recommended next action

Run a serving-grade deepen test in vLLM or an equivalent inference stack on real repetitive and natural prompt traces, measuring exactness, acceptance, forward-pass reduction, end-to-end latency, and throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-grade local n-gram speculation on real traces
- Success threshold: At least 20% p50 latency reduction and no more than 5% p95 latency regression versus no-draft cached greedy on repetitive/code/log traces, with exact token equivalence in all tested rows and a neutral or positive aggregate result on natural traces.
- Stop condition: Stop if exact equivalence fails, KV-cache overhead erases forward-pass savings, or repetitive/code/log traces show less than 10% latency improvement after reasonable n-gram order and draft-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/local-n-gram-speculative-decoding-dbbd44c98f71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
