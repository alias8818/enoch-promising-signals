# CPU N-Gram Speculative Decoding for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-5dea50d5ff67`
Run ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-5dea50d5ff67-20260521T231319877371+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

N-gram speculation achieved 1.069x mean tokens/s versus no-cache greedy but only 0.530x versus KV-cache greedy. Overall draft acceptance was 38.46%, concentrated in one prompt; six of eight rows accepted zero draft tokens.

## Boundaries and scale limits

Tested only GPT-2-small on CPU, deterministic argmax generation, 4 short prompts, 2 repeats, 24 generated tokens, 4 PyTorch CPU threads. Speculative verification was no-cache; a fully optimized KV-cache speculative verifier was not implemented.

## Claim scope

On this CPU worker, a simple prompt/history n-gram speculative decoder for GPT-2-small preserves greedy output and slightly improves over full-context no-cache greedy decoding, but it does not beat standard KV-cache greedy decoding.

## Why it stopped

Bounded direct GPT-2-small CPU evidence falsified the practical speedup claim for the implemented simple n-gram speculative decoder against the relevant KV-cache greedy control.

## Recommended next action

Stop this run as a no-paper useful signal; any next test should implement cache-aware speculative verification and require a sustained speedup over KV-cache greedy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculative decoding for GPT-2-small CPU
- Success threshold: At least 1.15x mean tokens/s versus KV-cache greedy with no output mismatches and no prompt subset accounting for all gains.
- Stop condition: Stop negative if speedup versus KV-cache greedy is below 1.05x or acceptance remains concentrated in fewer than half of prompts.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-gpt-2-small-5dea50d5ff67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
