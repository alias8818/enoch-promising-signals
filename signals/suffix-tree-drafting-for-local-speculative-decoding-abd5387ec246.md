# Suffix Tree Drafting for Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-drafting-for-local-speculative-decoding-abd5387ec246`
Run ID: `suffix-tree-drafting-for-local-speculative-decoding-abd5387ec246-20260604T104651107835+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05a6194bbd96

## What looked useful

Corpus-only suffix-occurrence drafting was weak on held-out WikiText and worse than a 4-gram control, but suffix occurrence that can match the current local context materially reduced verifier calls on held-out text and repeated structured logs. The mechanism appears useful for repetitive local contexts, not as a broad corpus-only drafter.

## Boundaries and scale limits

No optimized KV-cache serving implementation, no latency benchmark in a production speculative decoder, no larger target models, no non-greedy sampling, and only one natural held-out corpus plus one synthetic local-repetition workload.

## Claim scope

Bounded GPT-2 greedy speculative decoding simulation over 20 WikiText-2 validation prompts and 20 synthetic repeated structured-log prompts. Metrics are exact draft-token acceptance and emitted tokens per target verifier call for suffix-occurrence drafting versus unigram and 4-gram controls.

## Why it stopped

No-paper mixed result: the bounded proxy directly tested greedy verifier-call efficiency, but static suffix drafting failed the ordinary held-out text control and the positive signal is limited to context-aware/local-repetition behavior.

## Recommended next action

Run a bounded deepen follow-up with a real KV-cache speculative decoder on natural repetitive-context tasks and require end-to-end latency improvement over n-gram/cache-copy controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix drafting on natural repetitive local-context tasks
- Success threshold: At least 15% end-to-end latency improvement over the strongest non-suffix control on two natural repetitive-context workloads, with no regression on ordinary held-out text beyond 5% verifier-call efficiency.
- Stop condition: Stop as negative if context-aware suffix drafting fails to beat the strongest n-gram/cache-copy control on end-to-end latency or only improves synthetic repetition.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafting-for-local-speculative-decoding-abd5387ec246`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
