# N-gram speculative decoding without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-without-draft-model-9fc6af23be5c`
Run ID: `n-gram-speculative-decoding-without-draft-model-9fc6af23be5c-20260614T094301985128+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9845a53f1d57

## What looked useful

Exact greedy equivalence held in all successful runs. Prompt-only lookup reduced target calls by 64.06% on mixed fallback prompts and 45.70% on WikiText controls; update-history lookup improved reductions to 79.30% and 68.75%. Acceptance was high on copy-heavy prompts but weak on open continuation, and the naive verifier could be slower despite fewer target calls.

## Boundaries and scale limits

Tested only distilgpt2, greedy decoding, 4 hand-written prompts and 4 WikiText open-continuation prompts, 64 generated tokens each. The verifier recomputes full prefixes, so wall-clock speed is prototype-only and not representative of a production KV-cache implementation. No 7B+ model, batching, sampling, or serving integration was validated.

## Claim scope

A simple prompt/history n-gram proposer can preserve exact greedy decoding and reduce target serial calls on small GPT-2-class local prompts when generated text copies or repeats prompt/history spans.

## Why it stopped

Useful bounded mechanism evidence, but broad novelty is already covered by Prompt Lookup Decoding, Lookahead Decoding, N-Grammys, SSSD, and NASD/ANPD-like prior art, and this run is small/prototype-scale rather than publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; any next work should compare a production KV-cache implementation against existing prompt lookup or n-gram speculative baselines on real input-grounded tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production KV-cache n-gram speculative decoding versus existing prompt lookup baselines
- Success threshold: At least 1.3x median wall-clock speedup over greedy on input-grounded tasks with exact greedy-token equality and no worse than 0.95x on open-continuation controls.
- Stop condition: Stop if KV-cache implementation cannot maintain exactness, or if median wall-clock speedup is below 1.1x on input-grounded tasks after overhead profiling.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-without-draft-model-9fc6af23be5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
