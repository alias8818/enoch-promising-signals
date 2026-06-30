# Prompt-Lookup N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-n-gram-speculative-decoding-8f6de0dd92f4`
Run ID: `prompt-lookup-n-gram-speculative-decoding-8f6de0dd92f4-20260530T052251096655+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

Distilgpt2 on five handcrafted prompts with 32 generated tokens and n=3 prompt lookup reduced target calls by 64.375% with max_draft=4 and 70.0% with max_draft=8 while exactly matching greedy baseline output in all rows. Low-repetition control still reduced calls by 34.375%, while repeated/code-like prompts reached 65.625%-87.5%.

## Boundaries and scale limits

No optimized KV-cache serving kernel, batching, GPU latency measurement, public corpus sweep, sampling evaluation, or 7B+ target model. Results are mechanism and call-count evidence, not production latency validation.

## Claim scope

Bounded CPU experiment with real tiny-gpt2 and distilgpt2 target-model greedy verification on five handcrafted prompts. Prompt-lookup n-gram drafting preserved baseline greedy output and reduced target forward calls most on repeated, templated, and code-like contexts.

## Why it stopped

Evidence supports the mechanism in a small direct/proxy run but is not a full validation; production latency, batching, public-corpus robustness, and larger-model behavior remain untested.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should measure cache-aware wall-clock latency on a public prompt suite with GPT-2-small or a similar locally runnable target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware prompt-lookup latency on public repeated-context prompts
- Success threshold: At least 10% median wall-clock speedup and at least 20% median target-call reduction on repeated-context/code prompts, with zero greedy-output divergences and no regression larger than 5% median latency on low-repetition prompts.
- Stop condition: Stop as negative if output equivalence fails, if repeated-context/code prompts show under 5% median wall-clock speedup, or if low-repetition prompts regress by more than 10% median latency.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-n-gram-speculative-decoding-8f6de0dd92f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
