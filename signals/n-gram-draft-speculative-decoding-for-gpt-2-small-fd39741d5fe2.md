# N-gram draft speculative decoding for GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-fd39741d5fe2`
Run ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-fd39741d5fe2-20260523T035905484135+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fdc9667bbfb

## What looked useful

For max_ngram=4, max_draft=4, verifier calls fell from 1152 baseline target decisions to 660 simulated speculative calls (1.75x theoretical call speedup) with 53.9% draft-token acceptance. Natural prompts showed 1.55x speedup; repetitive prompts showed 2.34x. Larger drafts reached about 1.99x call speedup but lower acceptance.

## Boundaries and scale limits

Small hand-written prompt set; trace-level acceptance and verifier-call accounting only; no optimized cached serving benchmark; no public corpus-scale validation; no comparison against neural draft models or tuned prompt-lookup baselines.

## Claim scope

Trace-level GPT-2-small greedy decoding on 18 hand-written prompts x 64 generated tokens shows that a longest-suffix n-gram prompt/history lookup draft can reduce simulated speculative verifier calls while exactly matching the target greedy trace.

## Why it stopped

No-paper closure: current evidence is a useful trace-level mechanism signal, not a production speed or corpus-scale validation.

## Recommended next action

Run one bounded deepen follow-up: implement an exact cached/batched verifier with cache/full-forward parity checks, then benchmark actual tokens/sec and call reduction on a public corpus such as WikiText-style prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cached verifier benchmark for n-gram speculative decoding on public GPT-2-small prompts
- Success threshold: On at least 200 public prompts with 64 or more generated tokens each, exact output match plus at least 1.2x actual tokens/sec speedup over greedy cached GPT-2-small and at least 1.4x verifier-call reduction.
- Stop condition: Stop if cache/full-forward parity cannot be made exact locally, or if verifier-call reduction remains below 1.2x on the public prompt sample.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-gpt-2-small-fd39741d5fe2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
