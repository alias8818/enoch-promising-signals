# Prompt-N-Gram Cache Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-cache-speculative-drafting-000f3d65bcea`
Run ID: `prompt-n-gram-cache-speculative-drafting-000f3d65bcea-20260607T010058250169+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ef1d873df424

## What looked useful

Across 64 examples per condition, n-gram 6 achieved 0.490 accepted draft tokens per target token and 0.750 coverage in copy-from-prompt contexts, versus 0.005 accepted draft tokens per target token and 0.011 coverage in natural-continuation controls. The copy signal was stable across n-grams 3 to 12; longer n-grams reduced accidental natural-continuation proposals.

## Boundaries and scale limits

No end-to-end speculative decoding implementation, KV-cache timing, sampling acceptance, larger model, RAG/code workload, or wall-clock speedup measurement was run. Results are a bounded mechanism probe, not serving validation.

## Claim scope

On Wikitext-2 test examples with distilgpt2 teacher-forced greedy validation, a prompt-local n-gram cache proposes target-agreeing draft spans in copy-from-prompt contexts but provides almost no useful coverage for natural continuations.

## Why it stopped

Bounded teacher-forced proxy supports the mechanism in copy-heavy contexts but is not a full validation of speculative decoding latency or throughput.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a real KV-cache speculative decoding benchmark on copy-heavy RAG/code prompts and require measured wall-clock speedup over vanilla decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache timing benchmark for prompt n-gram speculative drafting
- Success threshold: At least 1.15x wall-clock tokens/second improvement on copy-heavy prompts with no more than 5% slowdown on natural-continuation controls.
- Stop condition: Stop negative if direct KV-cache speculative decoding shows less than 1.05x speedup on copy-heavy prompts or more than 10% slowdown on controls after implementation-level profiling.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-cache-speculative-drafting-000f3d65bcea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
