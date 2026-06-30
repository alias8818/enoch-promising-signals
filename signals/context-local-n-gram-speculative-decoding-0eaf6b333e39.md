# Context-Local N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-local-n-gram-speculative-decoding-0eaf6b333e39`
Run ID: `context-local-n-gram-speculative-decoding-0eaf6b333e39-20260603T142940803324+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/89f02b833a35

## What looked useful

Best local emitted/verifier-call proxy was 1.0313 on natural Gutenberg text, 6.0938 on in-domain repeated text, and 6.6398 on held-out context-only repeated text. The held-out context workload beat the global n-gram baseline by 6.09x, but natural text did not clear the 1.25 useful-signal threshold.

## Boundaries and scale limits

Single CPU-worker proxy benchmark over tokenized Gutenberg text and synthetic repetition corpora; no transformer verifier, no KV-cache batching, no production serving latency, and no broad long-context workload suite.

## Claim scope

Proxy corpus-continuation evidence shows context-local n-gram drafts are useful only when repeated continuations are present inside the active context; they are weak on ordinary natural prose and not superior to a global n-gram when the repetition is already in training.

## Why it stopped

Closed as no-paper proxy evidence: the mechanism is promising for context-copy workloads but the current run is not a full transformer or serving validation and falsifies the broad natural-text claim.

## Recommended next action

Run a bounded real-LM deepen follow-up using exact speculative decoding on long-context repetition prompts, with global n-gram and no-draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM validation of context-local n-gram speculative decoding on long-context repetition prompts
- Success threshold: Local n-gram drafting must exceed 1.25 emitted tokens per target verifier call and improve wall-clock decode latency by at least 10% versus no-draft while beating global n-gram on held-out context-copy prompts.
- Stop condition: Stop as negative if local n-gram drafting fails either the 1.25 emitted-token threshold or the 10% latency threshold on context-copy prompts, or if gains vanish after accounting for verifier batch cost.

## Evidence references

- Artifact root: `<local-path>/projects/context-local-n-gram-speculative-decoding-0eaf6b333e39`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
