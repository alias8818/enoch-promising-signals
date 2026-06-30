# CPU N-Gram Speculative Decoding for Small LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-small-llms-ff9306fb4c55`
Run ID: `cpu-n-gram-speculative-decoding-for-small-llms-ff9306fb4c55-20260529T215601035700+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/03809f7c3eca

## What looked useful

N-gram speculation is a real CPU latency lever when prompts contain repeated local spans: accepted multi-token drafts reduce model calls enough to overcome verifier overhead. Draft length 1 is a useful negative control because it preserves exactness but does not reduce calls and slightly slows down.

## Boundaries and scale limits

Single model, single host, 8 short synthetic/local prompts, greedy decoding only, no concurrent serving, no natural benchmark corpus, no second model family, and no production KV-cache implementation analysis.

## Claim scope

On one CPU worker with offline distilgpt2, exact greedy-equivalent prompt/history n-gram speculative decoding reduced wall time on an 8-prompt, 32-token benchmark when draft length was at least 2; the best setting, max_draft=8, reached 1.52x total speedup with zero greedy-token mismatches.

## Why it stopped

This run produced bounded direct evidence and useful mechanism signal, but the evidence is too small and prompt-shaped for a paper claim.

## Recommended next action

Run a medium confirmation on a natural prompt corpus with distilgpt2 plus one second small LM, pre-registering success as zero mismatches and at least 1.2x median latency speedup on repeated/retrieval-like prompts without more than 5% slowdown on controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus confirmation of exact CPU n-gram speculative decoding for small LMs
- Success threshold: Zero mismatches; repeated/retrieval-like prompts have at least 1.2x median wall-clock speedup on both models; controls have no more than 5% median slowdown.
- Stop condition: Stop if either model shows any exactness mismatch, or if repeated/retrieval-like prompts fail to reach 1.1x median speedup after draft-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-small-llms-ff9306fb4c55`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
