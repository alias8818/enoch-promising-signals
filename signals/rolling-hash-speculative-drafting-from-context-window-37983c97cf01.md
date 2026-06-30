# Rolling Hash Speculative Drafting from Context Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-hash-speculative-drafting-from-context-window-37983c97cf01`
Run ID: `rolling-hash-speculative-drafting-from-context-window-37983c97cf01-20260527T182901023549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4449d4107a57

## What looked useful

Exact rolling-hash context drafting works strongly on repeated boilerplate (mean accepted 11.60 tokens, 96.23% first-token hit, 56.45% full 16-token draft hit) but is weak on natural prose at practical suffix lengths (mean accepted about 0.14 tokens and under 10% first-token hit). This argues against a broad standalone paper claim, while preserving a narrow mechanism for template-heavy prompts.

## Boundaries and scale limits

No target LLM, no BPE tokenizer, no serving latency, no KV-cache measurement, and no code/chat/retrieval workload traces. The full bounded run evaluated 80,000 positions per configuration and 324 configurations in 192.73 seconds.

## Claim scope

A CPU-only proxy benchmark over regex-tokenized Tiny Shakespeare, Project Gutenberg Pride and Prejudice, and a synthetic repeated-boilerplate control tested exact rolling-hash suffix-copy drafting from the prior context window. Practical settings used suffix length at least 4 and draft length at least 8.

## Why it stopped

Bounded proxy evidence, not full validation, missed the predefined practical natural-prose threshold by a wide margin while passing only the repetitive synthetic control.

## Recommended next action

Stop this broad claim as a no-paper useful signal; if continuing, run a bounded real-tokenizer verifier test on template-heavy code/chat/retrieval traces rather than more natural-prose proxy sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer rolling-hash drafting on template-heavy prompts
- Success threshold: Mean accepted tokens per verification call >= 1.0 and p95 draft construction overhead below 5% of target verification time on at least two template-heavy workloads.
- Stop condition: Stop if practical suffix lengths still produce mean accepted tokens below 0.5 or if draft lookup overhead exceeds the saved verification work.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-hash-speculative-drafting-from-context-window-37983c97cf01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
